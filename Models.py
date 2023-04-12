from dataclasses import dataclass

# Dataclass is a decorator that allows you to define a class with a constructor
# and other methods that are automatically generated for you.
# It is a way to define a class that is more concise and readable than the
# traditional way of defining a class.

# Specify all the attributes of the class and their types.
@dataclass
class Shop:
    shopId: str
    name: str
    rating: float
    location: str


@dataclass
class Item:
    itemId: str
    shopId: str
    name: str
    price: float
    keyword1: str
    keyword2: str
    keyword3: str


@dataclass
class Customer:
    customerId: str
    name: str
    phone: str
    address: str


@dataclass
class Order:
    orderId: int
    customerId: str
    status: str


@dataclass
class OrderItem:
    orderId: str
    itemId: str
    quantity: int