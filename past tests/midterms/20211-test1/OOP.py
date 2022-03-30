"""
Question [12 marks]

In this question, you will complete a program for a food ordering system that
allows customers to place orders at various restaurants.
- An order has a description of a food item (str) and a quantity (int).
- A customer has a username (str), age (int), and the total quantity (int) of
  all food items they have ordered.
- A restaurant has a name (str) and all the orders that have been placed by each
  specific customer.
You will need to write one class for each of these entities.

In the __main__ block below is an example of how we want to use these
classes. Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.  Any unspecified
behaviour is up to you -- it will not be tested.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool may be public, but all other attributes must be
private. You may add imports from the typing module, but do NOT add any other
imports.

Your code will be marked for correctness and design, as well as for having
class docstrings that follow the Class Design Recipe. Docstrings for your
methods are NOT required.

Save your solution in a file called Q5_solution.py and submit it on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from __future__ import annotations
from typing import List, Dict


class Order:
    """An order.
    === Attributes ===
    desc: An order's food description
    quantity: An order's quantity
    """
    desc: str
    quantity: int

    def __init__(self, desc: str, quantity: int) -> None:
        self.desc = desc
        self.quantity = quantity

    def __str__(self) -> str:
        return f'Order for {self.quantity} units of {self.desc}'


class Restaurant:
    """A restaurant.
    === Attributes ===
    name: The name of the restaurant.
    _orders: all the orders that have been placed by each
    specific customer.
    """
    name: str
    _orders: Dict[str, List[Order]]

    def __init__(self, name: str) -> None:
        self.name = name
        self._orders = {}

    def get_customer_orders(self, name: str) -> List[Order]:
        if name not in self._orders:
            return []
        return self._orders[name]

    def add_order(self, order: Order, name: str) -> None:
        if name not in self._orders:
            self._orders[name] = []
        self._orders[name].append(order)


class Customer:
    """A customer.
    === Attributes ===
    username: This customer's username
    age: This customer's age
    quantity: This customer's order quantity.
    """
    username: str
    age: int
    total_quantity: int

    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age
        self.total_quantity = 0

    def create_order(self, name: Restaurant, order: Order) -> None:
        name.add_order(order, self.username)
        self.total_quantity += order.quantity


if __name__ == "__main__":
    # Instantiate two restaurants
    subway = Restaurant('Subway')
    tim_hortons = Restaurant('Tim Hortons')

    # Instantiate two customers
    mario = Customer('mario123', 22)
    talia = Customer('talia999', 22)

    # mario123 orders a sub, 2 cokes, and 4 cookies.
    mario.create_order(subway, Order('turkey sub', 1))
    mario.create_order(subway, Order('coke', 2))
    mario.create_order(subway, Order('cookie', 4))

    mario_orders = subway.get_customer_orders('mario123')
    for o in mario_orders:
        assert isinstance(o, Order)
        print(o)
        # Output is (notice that the most recent orders are first):
        # Order for 4 units of cookie
        # Order for 2 units of coke
        # Order for 1 units of turkey sub

    # talia999 hasn't ordered anything from Subway (or any restaurant).
    assert subway.get_customer_orders('talia999') == []
    # diane321 isn't even a known customer.
    assert subway.get_customer_orders('diane321') == []
    # mario123 hasn't ordered anything from Tim Horton's.
    assert tim_hortons.get_customer_orders('mario123') == []

    # mario123 has ordered in total 7 units of food.
    assert mario.total_quantity == 7

    # talia999 has ordered in total 0 units of food.
    assert talia.total_quantity == 0
