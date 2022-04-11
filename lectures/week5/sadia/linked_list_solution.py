"""Linked List

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node.

Code template we can use:

    curr = self._first
    while curr is not None:
        # ... curr.item ...
        curr = curr.next

But don't try to shoe-horn every single thing into this template!  It's not
always suited to the task.
"""
from __future__ import annotations

from typing import Any, Callable, Optional, Union


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

    # This implementation of LinkedList has a fancier initializer
    # and a __str__ method that permit things like:
    #     >>> linky = LinkedList([1, 223, 30, 16])
    #     >>> print(linky)
    #     '[1 -> 223 -> 30 -> 16]'

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if not items:  # No items and an empty list!
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

    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.
        """
        if self._first is None:
            self._first = _Node(item)
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = _Node(item)

    def print_items(self) -> None:
        """Print the items in this linked list.
        """
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def __eq__(self, other: LinkedList) -> bool:
        """Return whether this list and the other list are equal.

        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst2 = LinkedList([])
        >>> lst1.__eq__(lst2)
        False
        >>> lst2.append(1)
        >>> lst2.append(2)
        >>> lst2.append(3)
        >>> lst1.__eq__(lst2)
        True
        """

        curr1 = self._first
        curr2 = other._first

        while not (curr1 is None or curr2 is None):
            if curr1.item != curr2.item:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        # (a) We know that curr1 is None or curr2 is None
        # (The assertion is just to check this.)
        assert curr1 is None or curr2 is None

        # if curr1 is None and curr2 is None:
        #     The lists have the same length
        # else:
        #     # We reached the end of one linst but not the other.
        #     # The lists don't have the same length
        return curr1 is None and curr2 is None

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        >>> linky = LinkedList([100, 4, -50, 13])
        >>> linky[0]          # Equivalent to linky.__getitem__(0)
        100
        >>> linky[2]
        -50
        >>> linky[100]
        Traceback (most recent call last):
        IndexError
        """

        # (a) How to initialize curr and i
        curr = self._first
        i = 0

        # (b) What's the stopping condition of the loop?
        # Stop when curr is None OR when i == index
        # Turn this into the loop condition
        while not (curr is None or i == index):
            # (c) Loop body
            curr = curr.next
            i += 1

        # (d) Use the stopping condition to remind yourself what you know
        #       about curr and i
        assert curr is None or i == index  # sanity check!

        # Write the post-loop code
        # Two cases to check: curr is None or i == index
        if curr is None:
            raise IndexError
        else:
            return curr.item

    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.
        """

        new_node = _Node(item)

        # (a) Decide whether to update self._first
        if index == 0:
            # Update self._first
            # new_node.next = self._first
            # self._first = new_node

            # Either order has the same effect:
            new_node.next, self._first = self._first, new_node
            # self._first, new_node.next = new_node, self._first

        # (b) and (c): iterate to get to the "right" node, and insert
        else:
            curr = self._first
            i = 0

            # Iterate to the (index-1)th node
            # So stop condition is curr is None or i == index - 1
            while not (curr is None or i == index - 1):
                curr = curr.next
                i += 1

            # assert stopping condition!!
            assert curr is None or i == index - 1
            # deal with two cases:
            if curr is None:
                raise IndexError
            else:
                # new_node.next = curr.next
                # curr.next = new_node
                curr.next, new_node.next = new_node, curr.next


    def pop(self, index: int) -> Any:
        """Remove and return the item at position <index>.

        Raise IndexError if index >= len(self) or index < 0.

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(148)
        Traceback (most recent call last):
        IndexError
        >>> lst.pop(0)
        1
        """

        if index < 0 or self._first is None:
            raise IndexError

        # Decide whether to update self._first
        if index == 0:
            # Update self._first
            item = self._first.item
            self._first = self._first.next
            return item

        # Iterate to get to the "right" node, and insert
        else:
            curr = self._first
            i = 0

            # Iterate to the (index-1)th node
            # So stop condition is curr is None or i == index - 1
            while not (curr is None or i == index - 1):
                curr = curr.next
                i += 1

            # deal with two cases:
            if curr is None or curr.next is None:
                raise IndexError
            else:
                item = curr.next.item
                curr.next = curr.next.next
                return item

    def remove(self, item: Any) -> None:
        """Remove the FIRST occurrence of <item> in this list.

        Do nothing if this list does not contain <item>.
        (Note: Python lists actually raise a ValueError.)

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(2)
        >>> str(lst)
        '[1 -> 3]'
        >>> lst.remove(3)
        >>> str(lst)
        '[1]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        >>> lst.remove(1)
        >>> str(lst)
        '[]'
        """

        prev = None
        curr = self._first

        while curr is not None and curr.item != item:
            prev = curr
            curr = curr.next

        # if this list does not contain <item>
        # -- then curr is None
        # what if it's the first item
        # -- then prev is None

        if curr: # this is the same as saying if curr is not None
            if prev is None:
                self._first = self._first.next
            else:
                prev.next = prev.next.next # or prev.next = curr.next






if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    import doctest

    doctest.testmod()
