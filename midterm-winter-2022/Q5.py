"""
Question (6 marks)

We are adding another method to the LinkedList class.  It's almost written
but 4 lines are missing. Complete those lines so that the method is correct
according to its docstring.

Rules:
- For each TODO below, write a single expression or line of code as indicated,
  without changing its indentation.
- You must not change any other code in any way. E.g., you must not modify,
  delete or add to what is there.

TO HAND IN: Add your code to this file and hand it in on MarkUs.  Be sure to
run the self-test on MarkUs to avoid failing all our tests due to a silly error.

--------------------------------------------------------------------------------
This file is Copyright (c) 2022 University of Toronto
All forms of distribution, whether as given or with any changes, are
expressly prohibited.
--------------------------------------------------------------------------------
"""
from __future__ import annotations
from typing import Any, Optional


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

    def change_last(self, v: int) -> Optional[int]:
        """
        Change the last node in this linked list to contain v, and return the
        value that used to be there.

        If there are no nodes, change nothing and return None.

        >>> linky = LinkedList([5, 15, 10, 20])
        >>> linky.change_last(99)
        20
        >>> print(linky)
        [5 -> 15 -> 10 -> 99]
        >>> linky = LinkedList([5])
        >>> linky.change_last(99)
        5
        >>> print(linky)
        [99]
        >>> linky = LinkedList([])
        >>> linky.change_last(99) is None
        True
        >>> print(linky)
        []
        """
        if not self._first:  # TODO: Replace False with appropriate if-condition
            return None  # TODO: Replace pass with one line of code
        else:
            curr = self._first
            while curr.next is not None:
                # TODO: Replace False with appropriate while-condition
                curr = curr.next
            answer = curr.item  # TODO: Replace pass with one line of code
            curr.item = v
            return answer


if __name__ == '__main__':
    import doctest
    doctest.testmod()
