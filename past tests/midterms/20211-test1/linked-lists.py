"""
Question (10 marks)

Below is a new linked list method called insert_one_less_before. It has at least
one bug in its implementation. We have provided the parts of the LinkedList
class that you need for this question. Do NOT add to it or modify it, other
than as instructed below.

There are two parts to this question:

(a) Write a pytest function called test_demo_pass that the buggy implementation
    passes and another called test_demo_fail that the buggy implementation
    fails.

    Both tests must pass on a working implementation of the function (a version
    without any bugs).

    Both must be different from the doctest example provided, and must be
    meaningful test cases that check the method's behaviour relative to its
    docstring specification.

    Write these functions at the bottom of this file (under the TODO).

(b) Find and fix the bug(s) in the method insert_one_less_before.

Save your solution in a file called Q4_solution.py and submit it on MarkUs.

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

import doctest
from typing import Any, Optional
import pytest


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def insert_one_less_before(self) -> None:
        """For every original node n in this LinkedList, insert a new node
        preceding it and containing a value that is one less than value of
        node n.

        An original node is a node that was part of this LinkedList before
        any insertions by this method.

        Preconditions: This LinkedList contains only integers.

        >>> lst = LinkedList([2, 1, 4])
        >>> lst.insert_one_less_before()
        >>> str(lst)
        '[1 -> 2 -> 0 -> 1 -> 3 -> 4]'
        """
        # TODO: Find and fix the bug(s) in this method.
        if not (self._first is None):
            new_node = _Node(self._first.item - 1)
            new_node.next = self._first
            self._first = new_node

            curr = self._first.next
            while curr.next is not None:
                new_node = _Node(curr.next.item - 1)
                new_node.next = curr.next
                curr.next = new_node
                curr = new_node.next


# TODO: Write the two required pytest functions below.
#       - test_demo_pass should pass the buggy implementation provided and pass
#         on a working implementation.
#       - test_demo_fail should fail the buggy implementation provided but pass
#         on a working implementation.

def test_demo_pass() -> None:
    lst = LinkedList([2, 1, 4])
    lst.insert_one_less_before()
    assert str(lst) == '[1 -> 2 -> 0 -> 1 -> 3 -> 4]'


def test_demo_fail() -> None:
    lst = LinkedList([])
    lst.insert_one_less_before()
    assert str(lst) == '[]'


if __name__ == '__main__':
    doctest.testmod()
    # pytest.main(['Q4_solution.py'])
