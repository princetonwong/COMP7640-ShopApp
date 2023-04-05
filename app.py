from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from Models import Customer, Order, OrderItem, Item, Shop
from Logging import defaultLogging
from Database import Database
from uuid import uuid4

app = Flask(__name__, template_folder='ui', static_folder='ui', static_url_path='/ui')
Bootstrap(app)
defaultLogging()

db = Database(
    user="root",
    password="my-secret-pw",
    host="139.59.124.127",
    port=3306,
    database="SHOPAPP"
)

#TODO: Index file - Provide links to all the functionalities.
@app.route("/")
def index():
    return render_template("index.html")

def __getShopQty(shops):
    qtyData = db.execute("SELECT `shopId`, COUNT(`itemId`) FROM `ShopItem` GROUP BY `shopId`")
    qty = {row[0]: row[1] for row in qtyData}
    for shop in shops:
        shop.qty = qty.get(shop.shopId, 0)
    return shops

# Shop management - Show all shops
@app.route("/shop/all")
def showAllShops():
    data = db.execute("SELECT * FROM `Shop`")
    shops = [Shop(*row) for row in data]

    shops = __getShopQty(shops)

    return render_template("shopsList.html",
                           shops=shops,
                           title="All Shops",
                           buttonText="➕ Add a new shop",
                           buttonLink="/shop/add"
                           )


# Shop management - Add a new shop to the database.
@app.route("/shop/add", methods=["GET", "POST"])
def addShop():
    if request.method == "POST":
        name = request.form.get("shopName")
        rating = float(request.form.get("rating"))
        location = request.form.get("location")
        shopId = uuid4()

        query = f"INSERT INTO Shop (shopId, name, rating, location) VALUES ('{shopId}', '{name}', {rating}, '{location}');"
        db.execute(query)
        return redirect("/shop/all")
    return render_template("addShop.html")

# Shop Management - Show a shop with an item
@app.route("/shop/all/<item_id>")
def showShop(item_id):
    itemData = db.execute(f"SELECT * FROM `Item` WHERE itemId = '{item_id}'")
    item = Item(*itemData[0])
    shopsData = db.execute(f"SELECT * FROM `Shop` WHERE shopId in (SELECT shopId FROM `ShopItem` WHERE itemId = '{item_id}')")
    shops = [Shop(*row) for row in shopsData]

    shops = __getShopQty(shops)

    return render_template("shopsList.html",
                           shops=shops,
                           title=f"Shops with {item.name}",
                           buttonText="/",
                           buttonLink="/")

# Item management - Show all items of a shop
@app.route("/item/all/<shop_id>")
def showAllItems(shop_id):
    shopData = db.execute(f"SELECT * FROM `Shop` WHERE shopId = '{shop_id}'")
    shop = Shop(*shopData[0])

    itemsData = db.execute(f"SELECT * FROM Item WHERE itemId in (SELECT itemId FROM `ShopItem` WHERE shopId = '{shop_id}')")
    items = [Item(*row) for row in itemsData]

    return render_template("itemsList.html",
                           items=items,
                           title=f"All Items of {shop.name}",
                           buttonText="➕ Add a new item to this shop",
                           buttonLink=f"/item/add/{shop_id}"
                           )


# Item management - Add a new item to the shop
@app.route("/item/add/<shopId>", methods=["GET", "POST"])
def addItem(shopId):
    if request.method == "POST":
        itemName = request.form.get("itemName")
        price = float(request.form.get("price"))
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        itemId = uuid4()
        db.execute(f"INSERT INTO `Item` (itemId, name, price, keyword1, keyword2, keyword3) VALUES('{itemId}', '{itemName}', {price}, '{keyword1}', '{keyword2}','{keyword3}');")
        db.execute(f"INSERT INTO `ShopItem` (shopId, itemId) VALUES ('{shopId}', '{itemId}');")
        return redirect(f"/item/all/{shopId}")

    shopData = db.execute(f"SELECT * FROM `Shop` WHERE `shopId` = '{shopId}'")
    shop = Shop(*shopData[0])
    return render_template("addItem.html", shop=shop)

# Item search - You can search items by keywords. (A keyword --> name or keyword fully matches)
@app.route("/item/search", methods=["GET", "POST"])
def searchItem():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        data = db.execute(f"SELECT * FROM `Item` WHERE `name` = '{keyword}' OR `keyword1` = '{keyword}' OR `keyword2` = '{keyword}' OR `keyword3` = '{keyword}'")
        items = [Item(*row) for row in data]
        return render_template("itemsList.html",
                               items=items,
                               title=f"Search results of {keyword}",
                               buttonText="",
                               buttonLink=f""
                               )
    return render_template("search.html")


#TODO: Item purchase - Record in database which customer purchases which item.
@app.route("/item/purchase/<int:item_id>", methods=["GET", "POST"])
def purchaseItem(item_id):
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        db.execute(f"INSERT INTO `Customer` (`name`, `phone`, `address`) VALUES ('{name}', '{phone}', '{address}');")
        customerId = db.execute(f"SELECT `id` FROM `Customer` WHERE `name` = '{name}' AND  `phone` = '{phone}' AND `address` = '{address}'")[0][0]
        db.execute(f"INSERT INTO `Order` (`customerId`) VALUES ('{customerId}');")
        orderId = db.execute(f"SELECT `id` FROM `Order` WHERE `customerId` = '{customerId}'")[0][0]
        db.execute(f"INSERT INTO `OrderItem` (`orderId`, `itemId`) VALUES ('{orderId}', '{item_id}');")
        return redirect(url_for("index"))
    return render_template("purchaseItem.html")


#TODO: Order canceling - Cancel some item(s) in an order
@app.route("/order/cancel/<int:order_id>", methods=["GET", "POST"])
def cancelOrder(order_id):
    if request.method == "POST":
        itemId = request.form.get("itemId")
        db.execute(f"DELETE FROM `OrderItem` WHERE `orderId` = '{order_id}' AND `itemId` = '{itemId}';")
        return redirect(url_for("index"))
    return render_template("cancelOrder.html")


#TODO: Order canceling - cancel the entire order.
@app.route("/order/cancel/<int:order_id>/all")
def cancelAllOrder(order_id):
    db.execute(f"DELETE FROM `OrderItem` WHERE `orderId` = '{order_id}';")
    db.execute(f"DELETE FROM `Order` WHERE `id` = '{order_id}';")
    return redirect(url_for("index"))


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5011)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)

