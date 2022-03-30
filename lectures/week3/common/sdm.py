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


class Car(Vehicle):
    """A car."""

    def __init__(self, initial_fuel: int) -> None:
        Vehicle.__init__(self, initial_fuel, (0, 0))

    def fuel_needed(self, new_x: int, new_y: int) -> int:
        # why not just add new_x and new_y
        return abs(self.position[0] - new_x) + abs(self.position[1] - new_y)


class Helicopter(Vehicle):
    """A helicopter."""

    def __init__(self, initial_fuel: int) -> None:
        Vehicle.__init__(self, initial_fuel, (3, 5))

    def fuel_needed(self, new_x: int, new_y: int) -> float:
        return sqrt((new_x - self.position[0]) ** 2 +
                    (new_y - self.position[1]) ** 2)


class UnreliableMagicCarpet(Vehicle):
    """An unreliable magic carpet."""
    def __init__(self, initial_fuel: int) -> None:
        random_x = random.randint(-10, 10)
        random_y = random.randint(-10, 10)
        Vehicle.__init__(self, initial_fuel, (random_x, random_y))

    def fuel_needed(self, new_x: int, new_y: int) -> float:
        return 0

    def move(self, new_x: int, new_y: int) -> None:
        x = random.randint(new_x - 2, new_x + 2)
        y = random.randint(new_y - 2, new_y + 2)
        self.position = (x, y)


class SuperDuperManager:
    """A class responsible for keeping track of all vehicles in the system."""
    # === Private Attributes ===
    # _vehicles:
    #     Maps a string that uniquely identifies a vehicle to the corresponding Vehicle object.
    #     For example, _vehicles['car1'] would be a Vehicle object with the id_ 'car1'.
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
