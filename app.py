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


# Shop management - Show all shops
@app.route("/shop/all")
def showAllShops():
    data = db.execute("SELECT * FROM `Shop`")
    shops = [Shop(*row) for row in data]
    return render_template("showAllShops.html", shops=shops)


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


#TODO: Item management - Show all items of a shop
@app.route("/item/all/<int:shop_id>")
def showAllItems(shop_id):
    data = db.execute(f"SELECT * FROM `Item` WHERE `shopId` = {shop_id}")
    items = [Item(*row) for row in data]
    return render_template("showAllItems.html", items=items)


#TODO: Item management - Add a new item to the shop.
@app.route("/item/add/<int:shop_id>", methods=["GET", "POST"])
def addItem(shop_id):
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        db.execute(f"INSERT INTO `Item` (`name`, `price`, `shopId`) VALUES ('{name}', '{price}', '{shop_id}');")
        return redirect(url_for("index"))
    return render_template("addItem.html")

#TODO: Item search - You can search items by keywords. (A keyword --> name or keyword fully matches)
@app.route("/item/search", methods=["GET", "POST"])
def searchItem():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        data = db.execute(f"SELECT * FROM `Item` WHERE `name` = '{keyword}' OR `keyword1` = '{keyword}' OR `keyword2` = '{keyword}' OR `keyword3` = '{keyword}'")
        items = [Item(*row) for row in data]
        return render_template("searchItem.html", items=items)
    return render_template("searchItem.html")


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

