"""CSC148 in-class exercise: Super Duper Manager, 26 January 2022

=== Module description ===
Today we used a worksheet to navigate through and understand the code, and
then to identify what needed to be done to implement the Car class, which
we completed successfully (except for docstrings, which I have added).  Notice
how figuring out these things made writing the code really easy.

We did "run file in Python console" and then took the Car class out for a
test drive. :-)
>>> bug = Car(100)
>>> # It should start out at the origin.
>>> bug.position
(0, 0)
>>> # Let's see if it starts out with the amount of fuel we specified when we
>>> # created it.
>>> bug.fuel
100
>>> # It should be able to move to this location, using 30 of its 100 units of
>>> # fuel, since cars go "up and over" along streets, rather than taking a
>>> # direct, diagonal, route.
>>> bug.move(5, 25)
>>> # Is it where it should be?
>>> bug.position
(5, 25)
>>> # Is the fuel correct?
>>> bug.fuel
70
"""
from __future__ import annotations
from math import sqrt
import random          # used to generate random numbers
from typing import Dict, Optional, Tuple


class Vehicle:
    """An abstract class for a vehicle in the Super Duper system.

    === Attributes ===
    position:
        The coordinates of this vehicle on a grid.
    fuel:
        The amount of fuel remaining for this vehicle.

    === Representation invariants ===
    - fuel >= 0
    """
    position: Tuple[int, int]
    fuel: int

    def __init__(self, initial_fuel: int,
                 initial_position: Tuple[int, int]) -> None:
        """Initialize a new Vehicle with the given fuel and position.

        Precondition: initial_fuel >= 0
        """
        self.fuel = initial_fuel
        self.position = initial_position

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be needed to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.
        """
        raise NotImplementedError

    def move(self, new_x: int, new_y: int) -> None:
        """Move this vehicle to a new position.

        Do nothing if this vehicle does not have enough fuel to move to the specified position.
        """
        needed = self.fuel_needed(new_x, new_y)
        if needed <= self.fuel:
            self.position = (new_x, new_y)
            self.fuel -= needed


""" Worksheet Answers:
4a) In the SuperDuperManager, the attribute _vehicles
4b) In the initializer
4c) 

5a) position and fuel
5b) no

6a) All of them! __init__, fuel_needed and move
6b) fuel_needed
6c) __init__: It must start the car out at (0, 0). We must re-define it, 
    otherwise, client code could do this:
        bug = Car(100, (-304, 35))
    move: We can accept as is.
"""


class Car(Vehicle):
    """A car in the Super Duper system.

    A car can only move vertically and horizontally, and uses
    one unit of fuel per unit distance travelled.

    === Attributes ===
    position:
        The coordinates of this vehicle on a grid.
    fuel:
        The amount of fuel remaining for this vehicle.

    === Representation invariants ===
    - fuel >= 0
    """
    position: Tuple[int, int]
    fuel: int

    def __init__(self, initial_fuel: int) -> None:
        """Initialize a new car with the given fuel.

        Cars always start at position (0, 0).

        Precondition: fuel >= 0
        """
        Vehicle.__init__(self, initial_fuel, (0, 0))

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be used to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.
        """
        return abs(self.position[0] - new_x) + abs(self.position[1] - new_y)


class SuperDuperManager:
    """A class responsible for keeping track of all vehicles in the system."""
    # === Private Attributes ===
    # _vehicles:
    #     Maps a string that uniquely identifies a vehicle to the corresponding
    #     Vehicle object.
    #     For example, _vehicles['car1'] would be a Vehicle object with the
    #     id_ 'car1'.
    _vehicles: Dict[str, Vehicle]

    def __init__(self) -> None:
        """Initialize a new SuperDuperManager.

        There are no vehicles in the system when first created.
        """
        self._vehicles = {}

    def add_vehicle(self, vehicle_type: str, id_: str, fuel: int) -> None:
        """Add a new vehicle with the given type, id_, and fuel to the system.

        Do nothing if there is already a vehicle with the given id.

        Preconditions:
          - <vehicle_type> is one of 'Car', 'Helicopter', or 'UnreliableMagicCarpet'.
          - fuel >= 0
        """
        # Check to make sure the identifier isn't already used.
        x = 10
        y = 'hello'
        if id_ not in self._vehicles:
            if vehicle_type == 'Car':
                self._vehicles[id_] = Car(fuel)
            elif vehicle_type == 'Helicopter':
                self._vehicles[id_] = Helicopter(fuel)
            elif vehicle_type == 'UnreliableMagicCarpet':
                self._vehicles[id_] = UnreliableMagicCarpet(fuel)

    def move_vehicle(self, id_: str, new_x: int, new_y: int) -> None:
        """Move the vehicle with the given id.

        The vehicle called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no vehicle with the given id,
        or if the corresponding vehicle does not have enough fuel to move.
        """
        if id_ in self._vehicles:
            self._vehicles[id_].move(new_x, new_y)

    def get_vehicle_position(self, id_: str) -> Optional[Tuple[int, int]]:
        """Return the position of the vehicle with the given id.

        Return a tuple of the (x, y) position of the vehicle.
        Return None if there is no vehicle with the given id.
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].position

    def get_vehicle_fuel(self, id_: str) -> Optional[int]:
        """Return the amount of fuel of the vehicle with the given id.

        Return None if there is no vehicle with the given id.
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].fuel


if __name__ == '__main__':
    name = 'Diane'
    s = SuperDuperManager()
    s.add_vehicle('Car', 714, 100)

