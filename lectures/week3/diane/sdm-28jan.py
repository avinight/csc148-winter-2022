"""CSC148 in-class exercise: Super Duper Manager, 28 January 2022

=== Module description ===
Last class we thought through and implemented the Car class. Today, we
thought through Helicopter and UnreliableMagicCarpet -- what methods they could
inherit as-is, and which ones needed to be redefined and why. See the annotated
worksheet for notes on that. As an exercise, implement those two classes.
It's good practise to type the whole class yourself, and they aren't very large.

Today we also looked at function collect. It takes advantage of the
fact that the public methods in class Vehicle define an interface that is common
across all subclasses of Vehicle. (It is common across them because they all
inherit those methods.) This means that the function can say:
        v.move(where[0], where[1])
without knowing exactly what v is. It only needs to know that it is some kind
of Vehicle. That's enough to guarantee that v will have a move method -- because
this is part of the common public interface that Vehicle defines.

I've added yet another type of vehicle: a broomstick to the code. Take a look
at class Broomstick and the small example in the main block. It shows that
function collect can even handle this new kind of vehicle that I hadn't even
thought of when I wrote the code for collect!
"""
from __future__ import annotations

from abc import ABC
from math import sqrt
import random          # used to generate random numbers
from typing import Dict, Optional, Tuple, List


class Vehicle:
    """An abstract class for a vehicle in the Super Duper system.  Because it
    is abstract, it should never be instantiated.

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

    def _clean_myself(self) -> None:
        pass

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be needed to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.
        """
        raise NotImplementedError

    def move(self, new_x: int, new_y: int) -> None:
        """Move this vehicle to a new position.

        Do nothing if this vehicle does not have enough fuel to move to the
        specified position.
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


class Broomstick(Vehicle):
    def fuel_needed(self, new_x: int, new_y: int) -> int:
        """Return how much fuel would be needed to move to the given position.

        Broomsticks are low emission vehicles -- they require only 1 unit of
        fuel no matter how far you fly!
        """
        return 1


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
          - <vehicle_type> is one of 'Car', 'Helicopter', or
            'UnreliableMagicCarpet'.
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


def collect(vehicles: List[Vehicle], where: Tuple[int, int]) -> int:
    """Move each of the vehicles to where, if the vehicle has enough fuel.
    Return the number that were moved successfully.

    >>> betsy = Car(10)
    >>> fred = Car(70)
    >>> lst = [betsy, fred]
    >>> collect(lst, (25, 25))
    1
    >>> betsy.position
    (0, 0)
    >>> fred.position
    (25, 25)
    """
    num_moved = 0
    for v in vehicles:
        v.move(where[0], where[1])
        # If v ended up at the desired position, count it.  Otherwise, it must
        # not have had enough fuel to go there.
        if v.position == where:
            num_moved += 1
    return num_moved


if __name__ == '__main__':
    # name = 'Diane'
    # s = SuperDuperManager()
    # s.add_vehicle('Car', 714, 100)

    b = Broomstick(55, (10, 10))
    c1 = Car(0)
    c2 = Car(40)
    lst = [b, c1, c2]

    # Collect even works when it has to handle a type of Vehicle (a broomstick)
    # that I hadn't even thought of when I wrote the code for collect!
    how_many_moved = collect(lst, (5, 5))
    print(f'{how_many_moved} of the {len(lst)} vehicles moved, and this is '
          f'where things are:')
    for v in lst:
        print(f'\tA vehicle of type {type(v)} is here: {v.position} '
              f'with fuel {v.fuel}')


