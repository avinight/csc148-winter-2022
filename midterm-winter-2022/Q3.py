"""
Question (12 marks)

TO HAND IN: Add your code to this file and hand it in on MarkUs.  Be sure to
run the self-test on MarkUs to avoid failing all our tests due to a silly error.
--------------------------------------------------------------------------------
In this question, you will write code to implement plants so that
the doctest examples below run without error, and these specifications are
followed:
- There are 2 kinds of plants for now, but we plan to add more later.
- All plants have a height and a collection of items that have landed in them.
  Each item is represented simply by a string.
- Plants start out with no items in them, but can "receive" items.
- In addition to a height and items, deciduous trees have a number of leaves.
  Coniferous trees do not.
- Items can leave a plant. We'll say that a plant "releases" them. All
  plants do this the same: if the thing is in the plant, it is removed and a
  goodbye message is printed.
- All plants can return a string that is suitable for printing, but they each
  return something different, as shown below. You'll notice that a coniferous
  tree only shows you the first thing that landed in it. This is because of its
  dense branches.
- Because a coniferous tree is so dense, it also can only hold a limited number
  of things. This is specified when it is created.
- When a coniferous tree receives an item, it only keeps it if it still has
  capacity.
- A deciduous tree doesn't have a capacity limit, and can always hold onto
  things that it receives.
Any behaviour that is not specified by this description plus the doctests is
up to you.

We have started the code for you.
- You must not alter anything that is already written. Just add to it.
- No docstrings are required. But for full marks, you must provide type
  annotations that specify the return type and parameter types for each method.
- Part of the marks will be for avoiding repeated code where appropriate.
- Do not add any new attributes.

HINT: Run this module to check your code against these doctest examples:

>>> birch1 = DeciduousTree(10, 2500)
>>> print(birch1)
Height 10cm, with 2500 leaves, and containing: []
>>> pine1 = ConiferousTree(150, 2)
>>> print(pine1)
150cm tall, room for 2, holding 0, and with this visible: nothing
>>> for item in ['owl', 'kite', 'kitten']:
...     birch1.receive(item)
>>> print(birch1)
Height 10cm, with 2500 leaves, and containing: ['owl', 'kite', 'kitten']
>>> 'owl' in birch1 and 'kite' in birch1 and 'kitten' in birch1
True
>>> 'bear' not in birch1
True
>>> birch1.release('kite')
Bye bye kite!
>>> birch1.release('piano')
I do not have that
>>> print(birch1)
Height 10cm, with 2500 leaves, and containing: ['owl', 'kitten']
>>> for item in ['robin', 'ball', 'woodpecker']:
...     pine1.receive(item)
>>> print(pine1)
150cm tall, room for 2, holding 2, and with this visible: robin
>>> 'robin' in pine1 and 'ball' in pine1
True
>>> 'woodpecker' not in pine1
True

--------------------------------------------------------------------------------
This file is Copyright (c) 2022 University of Toronto
All forms of distribution, whether as given or with any changes, are
expressly prohibited.
--------------------------------------------------------------------------------
"""
from __future__ import annotations
from typing import List


class Plant:
    height: int
    items: List[str]

    def __init__(self, height: int) -> None:
        self.height = height
        self.items = []

    def receive(self, item: str) -> None:
        self.items.append(item)

    def release(self, item: str) -> None:
        if item in self.items:
            self.items.remove(item)
            print(f'Bye bye {item}!')
        else:
            print('I do not have that')

    def __contains__(self, item) -> bool:
        return item in self.items


class DeciduousTree(Plant):
    height: int
    items: List[str]
    leaves: int

    def __init__(self, height: int, leaves: int) -> None:
        Plant.__init__(self, height)
        self.leaves = leaves

    def __str__(self) -> str:
        return f'Height {self.height}cm, with {self.leaves} leaves, ' \
               f'and containing: {self.items}'


class ConiferousTree(Plant):
    height: int
    items: List[str]
    capacity: int

    def __init__(self, height: int, capacity: int) -> None:
        Plant.__init__(self, height)
        self.capacity = capacity

    def __str__(self) -> str:
        string = f'nothing'
        if self.items:
            string = f'{self.items[0]}'
        return f'{self.height}cm tall, room for {self.capacity}, ' \
               f'holding {len(self.items)}, and with this visible: ' + string

    def receive(self, item: str) -> None:
        if len(self.items) < self.capacity:
            self.items.append(item)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
