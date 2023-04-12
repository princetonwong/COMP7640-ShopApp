from flask import Flask, render_template, url_for, request, redirect, flash
from flask_bootstrap import Bootstrap
from Models import Customer, Order, OrderItem, Item, Shop
from Logging import defaultLogging
from Database import Database
from uuid import uuid4

# Use Flask to create a web server.
app = Flask(__name__, template_folder='ui', static_folder='ui', static_url_path='/ui')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
Bootstrap(app)
defaultLogging()

# Connect to the database.
db = Database(
    user="root",
    password="my-secret-pw",
    host="139.59.124.127",
    port=3306,
    database="SHOPAPP"
)


# Index file - Provide links to all the functionalities.
@app.route("/")
def index():
    return render_template("index.html")


# Utility functions - Aggregate COUNT(itemId) from the database and add it to the SHOP objects.
def __getItemQtyByShop(shops):
    qtyData = db.execute("SELECT `shopId`, COUNT(`itemId`) FROM `Item` GROUP BY `shopId`")
    qty = {row[0]: row[1] for row in qtyData}
    for shop in shops:
        shop.qty = qty.get(shop.shopId, 0)
    return shops


# Utility functions - Lookup shopName from the database and add it to the ITEM objects.
def __getShopNameByItem(items):
    shopNameData = db.execute("SELECT i.`itemId`, s.name FROM `Item` i INNER JOIN `Shop` s ON i.`shopId` = s.`shopId`")
    shopname = {row[0]: row[1] for row in shopNameData}
    for item in items:
        item.shopName = shopname.get(item.itemId, 0)
    return items


# Utility functions - Aggregate COUNT(orderId) from the database and add it to the ITEM objects.
def __getOrderQtyByItem(items):
    qtyData = db.execute("SELECT `itemId`, COUNT(`orderId`) FROM `OrderItem` GROUP BY `itemId`")
    orderQty = {row[0]: row[1] for row in qtyData}
    for item in items:
        item.orderQty = orderQty.get(item.itemId, 0)
    return items


# Utility functions - Aggregate SUM(quantity) from the database and add it to the ITEM objects.
def __getOrderItemQtyByItem(items):
    qtyData = db.execute("SELECT `itemId`, SUM(`quantity`) FROM `OrderItem` GROUP BY `itemId`")
    orderItemQty = {row[0]: row[1] for row in qtyData}
    for item in items:
        item.orderItemQty = orderItemQty.get(item.itemId, 0)
    return items


# Utility functions - Aggregate COUNT(orderId) from the database and add it to the CUSTOMER objects.
def __getOrderQtyByCustomer(customers):
    qtyData = db.execute("SELECT `customerId`, COUNT(`orderId`) FROM `Order` GROUP BY `customerId`")
    orderQty = {row[0]: row[1] for row in qtyData}
    for customer in customers:
        customer.orderQty = orderQty.get(customer.customerId, 0)
    return customers


# Utility functions - Aggregate COUNT(itemId) from the database and add it to the ORDER objects.
def __getItemsQtyByOrder(orders):
    qtyData = db.execute("SELECT `orderId`, COUNT(`itemId`) FROM `OrderItem` GROUP BY `orderId`")
    qty = {row[0]: row[1] for row in qtyData}
    for order in orders:
        order.itemsQty = qty.get(order.orderId, 0)
    return orders


# Shop management - Show all shops
@app.route("/shop/show")
def shopsList():
    data = db.execute("SELECT * FROM `Shop` order by name")
    shops = [Shop(*row) for row in data]

    title = "All Shops"
    buttonText = "➕ Add a new shop"
    buttonLink = "/shop/add"

    shops = __getItemQtyByShop(shops)

    return render_template("shopsList.html",
                           shops=shops,
                           title=title,
                           buttonText=buttonText,
                           buttonLink=buttonLink
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
        return redirect("/shop/show")
    return render_template("addShop.html")


# Item management - Show all items of a shop or an order.
@app.route("/item/show")
def showAllItems():
    shopId = request.args.get("shopId", None)
    orderId = request.args.get("orderId", None)

    # Item management - Show all items of a shop
    if shopId:
        shopData = db.execute(f"SELECT * FROM `Shop` WHERE shopId = '{shopId}'")
        shop = Shop(*shopData[0])

        itemsData = db.execute(
            f"SELECT * FROM Item WHERE shopId = '{shopId}' order by `name`")
        items = [Item(*row) for row in itemsData]

        title = f"All Items of {shop.name}"
        buttonText = "➕ Add a new item to this shop"
        buttonLink = f"/item/add?shopId={shop.shopId}"
        order = None

    # Item management - Show all items of an order
    elif orderId:
        orderData = db.execute(f"SELECT * FROM `Order` WHERE orderId = '{orderId}'")
        order = Order(*orderData[0])

        itemsData = db.execute(
            f"SELECT * FROM Item WHERE itemId in (SELECT itemId FROM `OrderItem` WHERE orderId = '{orderId}') order by `name`")
        items = [Item(*row) for row in itemsData]

        items = __getOrderItemQtyByItem(items)

        title = f"All Items of Order {order.orderId} from {order.customerId}"
        buttonText = "➕ Add a new item to this order"
        buttonLink = f"/orderItem/add?orderId={order.orderId}"

    # Item management - Show all items in database
    else:
        itemsData = db.execute("SELECT * FROM `Item` order by `name`")
        items = [Item(*row) for row in itemsData]

        title = f"All Items"
        buttonText = ""
        buttonLink = ""
        order = None

    items = __getShopNameByItem(items)
    items = __getOrderQtyByItem(items)

    return render_template("itemsList.html",
                           items=items,
                           title=title,
                           buttonText=buttonText,
                           buttonLink=buttonLink,
                           order=order
                           )


# Item management - Add a new item to the shop
@app.route("/item/add", methods=["GET", "POST"])
def addItem():
    shopId = request.args.get("shopId")
    if request.method == "POST":
        itemName = request.form.get("itemName")
        price = float(request.form.get("price"))
        keyword1 = request.form.get("keyword1")
        keyword2 = request.form.get("keyword2")
        keyword3 = request.form.get("keyword3")
        itemId = uuid4()
        db.execute(
            f"INSERT INTO `Item` (itemId, shopId, name, price, keyword1, keyword2, keyword3) VALUES('{itemId}', '{shopId}', '{itemName}', {price}, '{keyword1}', '{keyword2}','{keyword3}');")
        return redirect(f"/item/show?shopId={shopId}")

    shopData = db.execute(f"SELECT * FROM `Shop` WHERE `shopId` = '{shopId}'")
    shop = Shop(*shopData[0])
    return render_template("addItem.html", shop=shop)


# Item search - You can search items by keywords. (A keyword --> name or keyword fully matches)
@app.route("/item/search", methods=["GET", "POST"])
def searchItem():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        data = db.execute(
            f"SELECT * FROM `Item` WHERE `name` = '{keyword}' OR `keyword1` = '{keyword}' OR `keyword2` = '{keyword}' OR `keyword3` = '{keyword}'")
        items = [Item(*row) for row in data]

        items = __getShopNameByItem(items)
        items = __getOrderQtyByItem(items)

        return render_template("itemsList.html",
                               items=items,
                               title=f"Search results of {keyword}",
                               buttonText="",
                               buttonLink=f""
                               )
    return render_template("search.html")


# Customer management - Show all customers
@app.route("/customer/show")
def showAllCustomers():
    data = db.execute("SELECT * FROM `Customer`")
    customers = [Customer(*row) for row in data]

    customers = __getOrderQtyByCustomer(customers)

    return render_template("customersList.html",
                           customers=customers,
                           title="All Customers",
                           buttonText="➕ Add a new customer",
                           buttonLink="/customer/add"
                           )


# Customer management - Add a new customer to the database.
@app.route("/customer/add", methods=["GET", "POST"])
def addCustomer():
    if request.method == "POST":
        customerId = request.form.get("customerId")
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")

        # Check if the customer already exists
        if db.execute(f"SELECT * FROM `Customer` WHERE `customerId` = '{customerId}'"):
            flash(f"Customer <{customerId}> already exists", "error")
            return render_template("addCustomer.html")
        else:
            query = f"INSERT INTO Customer (customerId, name, phone, address) VALUES ('{customerId}', '{name}', '{phone}', '{address}');"
            db.execute(query)
            return redirect("/customer/show")
    return render_template("addCustomer.html")


# Purchase management
@app.route("/orderItem/add", methods=["GET", "POST"])
def addOrderItem():
    if request.method == "POST":
        orderId = request.form.get("orderId")
        itemId = request.form.get("itemId")
        quantity = int(request.form.get("quantity"))
        customerId = request.form.get("customerId")

        # Check if the purchase already exists
        if db.execute(f"SELECT * FROM `OrderItem` WHERE `orderId` = '{orderId}' AND `itemId` = '{itemId}'"):
            # Add quantity to the existing orderItem
            db.execute(
                f"UPDATE `OrderItem` SET `quantity` = `quantity` + {quantity} WHERE `orderId` = '{orderId}' AND `itemId` = '{itemId}';")
            flash(f"Item <{itemId}> already exists in order {orderId}, add {quantity}", "error")
            return redirect(f"/item/show?orderId={orderId}")

        # Add a new purchase
        else:
            db.execute(
                f"INSERT INTO OrderItem (orderId, itemId, quantity) VALUES ('{orderId}', '{itemId}', {quantity});")
            flash(f"Item successfully added", "error")
            return redirect(f"/item/show?orderId={orderId}")

    orderId = request.args.get("orderId")
    itemId = request.args.get("itemId")
    customerId = request.args.get("customerId")

    # (OrderID context is known) Load existing purchased items, load all items as options to choose
    if orderId:
        orderData = db.execute(f"SELECT * FROM `Order` WHERE `orderId` = '{orderId}'")
        order = Order(*orderData[0])
        itemsData = db.execute(f"SELECT * FROM `Item` order by `name`")
        items = [Item(*row) for row in itemsData]
        items = __getShopNameByItem(items)
        return render_template("addOrderItem.html", order=order, items=items, customerId=order.customerId)

    # (ItemID context is known) Load chosen item, load all customers as options to choose
    elif itemId:
        itemData = db.execute(f"SELECT * FROM `Item` WHERE `itemId` = '{itemId}'")
        item = Item(*itemData[0])
        customersData = db.execute(f"SELECT * FROM `Customer` order by `name`")
        customers = [Customer(*row) for row in customersData]
        return render_template("addOrderItem.html", order=None, item=item, customerId=None, customers=customers)

    # (None is known) Load all items as options to choose
    else:
        itemsData = db.execute(f"SELECT * FROM `Item` order by `name`")
        items = [Item(*row) for row in itemsData]
        items = __getShopNameByItem(items)
        return render_template("addOrderItem.html", customerId=customerId, items=items)


# Purchase management - Cancel a purchase
@app.route("/orderItem/cancel", methods=["GET"])
def cancelOrderItem():
    orderId = request.args.get("orderId")
    itemId = request.args.get("itemId")

    db.execute(f"DELETE FROM `OrderItem` WHERE `orderId` = '{orderId}' AND `itemId` = '{itemId}';")
    flash(f"Item successfully removed", "error")

    orderItemsCountData = db.execute(f"SELECT COUNT(*) FROM `OrderItem` WHERE `orderId` = '{orderId}';")
    orderItemsCount = orderItemsCountData[0][0]
    if orderItemsCount == 0:
        db.execute(f"UPDATE `Order` SET `status` = 'Cancelled' WHERE `orderId` = '{orderId}';")
        return redirect("/order/show")

    return redirect(f"/item/show?orderId={orderId}")


# Order management
@app.route("/order/show")
def showOrders():
    customerId = request.args.get("customerId")
    itemId = request.args.get("itemId")

    # Order management - Show all orders from a specific customer
    if customerId:
        data = db.execute(f"SELECT * FROM `Order` WHERE `customerId` = '{customerId}' order by `orderId`")
        orders = [Order(*row) for row in data]

        title = f"Orders of customer - {customerId}"
        buttonText = "➕ Add a new order"
        buttonLink = f"/orderItem/add?customerId={customerId}"
        customerId = customerId

    # Order management - Show all orders with a specific item
    elif itemId:
        data = db.execute(
            f"select * from `Order` where orderId in (SELECT orderId FROM `OrderItem` WHERE `itemId` = '{itemId}')")
        orders = [Order(*row) for row in data]

        title = f"Orders with item - {itemId}"
        buttonText = ""
        buttonLink = ""
        customerId = None

    # Order management - Show all orders
    else:
        data = db.execute("SELECT * FROM `Order` ORDER BY `orderId`")
        orders = [Order(*row) for row in data]

        title = "All Orders"
        buttonText = "➕ Add a new order"
        buttonLink = f"/order/add"
        customerId = None

    orders = __getItemsQtyByOrder(orders)

    return render_template("ordersList.html",
                           orders=orders,
                           title=title,
                           buttonText=buttonText,
                           buttonLink=buttonLink,
                           customerId=customerId
                           )


# Order management - Add a new order to the database.
@app.route("/order/add", methods=["GET", "POST"])
def addOrder():
    if request.method == "POST":
        customerId = request.form.get("customerId")

        # Check if the customer exists
        if not db.execute(f"SELECT * FROM `Customer` WHERE `customerId` = '{customerId}'"):
            flash(f"Customer <{customerId}> does not exist. Please add a new customer first.", "error")
            customerData = db.execute(f"SELECT * FROM `Customer` WHERE `customerId` = '{customerId}'")[0]
            customer = Customer(*customerData)
            return render_template("addOrder.html", customer=customer)

        db.execute(f"INSERT INTO `Order` (`customerId`, `status`) VALUES ('{customerId}', 'Pending');")

        itemId = request.form.get("itemId")
        orderId = db.execute(f"SELECT `orderId` FROM `Order` WHERE `customerId` = '{customerId}'")[0][0]
        db.execute(f"INSERT INTO `OrderItem` (`orderId`, `itemId`) VALUES ('{orderId}', '{itemId}');")

        return redirect("/order/show")

    customerId = request.args.get("customerId")
    itemData = db.execute(f"SELECT * FROM `Item` order by `name`")
    items = [Item(*row) for row in itemData]

    # (CustomerID context is known) Load chosen customer, load all items as options for first purchase in this order
    if customerId:
        customerData = db.execute(f"SELECT * FROM `Customer` WHERE `customerId` = '{customerId}'")[0]
        customer = Customer(*customerData)
        return render_template("addOrder.html", customer=customer, items=items)

    customersData = db.execute(f"SELECT * FROM `Customer` order by `name`")
    customers = [Customer(*row) for row in customersData]

    return render_template("addOrder.html", customers=customers, items=items)


# Order canceling - Mark entire order cancelled
@app.route("/order/cancel")
def cancelOrder():
    orderId = request.args.get("orderId")
    customerId = request.args.get("customerId")
    db.execute(f"UPDATE `Order` SET `status` = 'Cancelled' WHERE `orderId` = '{orderId}';")
    if customerId:
        return redirect(f"/order/show?customerId={customerId}")
    else:
        return redirect("/order/show")


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5011)
    args = parser.parse_args()
    port = args.port
    app.run(host='127.0.0.1', port=port)
