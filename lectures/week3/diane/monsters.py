"""csc148, Winter 2021

Bonus example about inheritance and special methods.

1. Special methods.
Notice that our class Monster has defined the "special method" __str__.
This method is automatically called if we print a Monster.

>>> m1 = Monster('Antony')
>>> print(m1)
Antony Boo!

You can define a __str__ method in any class you write, and control how it is
shown when printed. This is true for any class -- it has nothing to do with
inheritance. See the Lecture Notes, section 2.7.

What happens if a class doesn't have a __str__ method and you print an instance
of the class? Make a prediction, based on your knowledge of how Python resolves
a method name (section 2.4) and then make the smallest possible example to test
your prediction.

2. Inheritance.
Currently, it has a big problem: Gremlins can't eat! Take a look at the code
and this demo, and see if you can fix it. If you fix it properly you should
be able to run the code in the __main__ block, which is currently commented out.

>>> # Eating works for Monsters: their hunger goes down and their energy goes
>>> # up when the eat.
>>> m1 = Monster('Antony')
>>> m1.name
'Antony'
>>> m1.hunger
100
>>> m1.energy
0
>>> m1.eat('garbage')
>>> m1.name
'Antony'
>>> m1.hunger
99
>>> m1.energy
1
>>> # But we get an error when a Gremlin eats:
>>> m2 = Gremlin('Cleopatra')
>>> m2.eat('garbage')
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
  File "/Users/dianehorton/Documents/courses/148-22s/csc148/lectures/week3/monsters.py", line 31, in eat
    self.hunger = self.hunger + 10
AttributeError: 'Gremlin' object has no attribute 'hunger'
"""
from typing import Any, List


class Monster:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hunger = 100
        self.energy = 0

    def eat(self, item: Any) -> None:
        self.hunger = self.hunger - 1
        self.energy += 1

    def sleep(self, minutes: int) -> None:
        self.energy += minutes

    def __str__(self) -> str:
        return self.name + " Boo!"


class Gremlin(Monster):
    def __init__(self, name: str) -> None:
        self.stuffy = 'Bunny'

    def eat(self, item: Any) -> None:
        # Eating makes Gremlins more hungry!
        self.hunger = self.hunger + 10

    def __str__(self) -> str:
        return self.name + 'Mwahaha!'


# if __name__ == '__main__':
#     m1 = Monster('Antony')
#     m2 = Gremlin('Cleopatra')
#     m3 = Gremlin('Julius')
#     zoo = [m1, m2, m3]
#
#     for creature in zoo:
#         creature.eat('garbage')
#         creature.sleep(5)
#
#     total = 0
#     for creature in zoo:
#         total += creature.hunger
#     print(total)
