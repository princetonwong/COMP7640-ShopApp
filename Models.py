from dataclasses import dataclass


@dataclass
class Shop:
    shopId: str
    name: str
    rating: float
    location: str


@dataclass
class Item:
    itemId: str
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
    orderId: str
    customerId: str


@dataclass
class OrderItem:
    orderId: str
    itemId: str
    quantity: int