"""Linked List, 9 February

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
Today we implemented 3 linked list methods.  The first two only traversed the
linked list: __eq__ and __getitem__.  The third one was our first method to
mutate a linked list: insert.  We finished insert in the last moments of class
but couldn't test it because I foolishly had not included any doctests. That was
a bit anti-climactic!  I've added a basic doctest so you can test it now
yourself. Do you think it will work? Are you excited to find out?

There were three very important take-away lessons from this rather successful
coding experience today:
- While loops are easy to mess up. It really helps to first write down the
  condition under which the loop must stop, and then flip that around to get
  your while condition (the condition under which the loop must NOT stop).
- It really helps to write down what you know at key points, including after a
  while loop. There is often subtle logic implicit in the code. It's better to
  write it down explicitly. You can even use asserts to check your logic. This
  can save you from some subtle bugs.
- Whenever you saw apple.banana, you'd better be sure that apple is not None!
  Reasoning through that can not only avoid bugs, but we saw that it can
  help you with the logic of your program.

Short version: Think before you code. It will save you time.
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
    # You'll write these methods later.

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
        >>> lst1 == lst2   # Equivalent to lst1.__eq__(lst2).  Handy!!
        True
        >>> lst2.append(4)
        >>> lst1.__eq__(lst2)
        False
        >>> lst1 == lst2
        False
        """
        # We planned out the initialization and loop via a worksheet.
        curr1 = self._first
        curr2 = other._first
        while (curr1 is not None) and (curr2 is not None):
            if curr1.item == curr2.item:
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                return False
        # We can express what we know in an executable way.
        # This will catch errors in our logic.
        assert (curr1 is None) or (curr2 is None)

        # We don't know whether or not the lists are equivalent.
        # What DO we know?
        # Every pair of values we checked WAS ==
        # not((curr1 is not None) and (curr2 is not None))
        # (curr1 is None) or (curr2 is None) or both are None.
        # How can we tell if the lists have the same length?
        # They have the same lenght if both are None!
        # And since we know the values we checked (which were all of
        # the values in the 2 lists) were ==.

        # A not concise way to say this:
        # if (curr1 is None) and (curr2 is None):
        #     return True
        # else:
        #     return False

        # The concise way:
        return (curr1 is None) and (curr2 is None)

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
        curr = self._first
        i = 0
        # We need to iterate to reach the ith node.
        # Stopping condition(s):
        # 1. curr is None OR
        # 2. i == index
        # In other words: (curr is None) or (i == index)
        # Continuing condition: not ((curr is None) or (i == index))
        # DeMorgan's Law let's us simplify!
        # Continuing condition: (curr is not None) and (i != index)
        while (curr is not None) and (i != index):
            i += 1
            curr = curr.next
        # What do we know?
        # not((curr is not None) and (i != index))
        # in other words:
        # (curr is None) or (i == index) or both!

        # This solution is close, but doesn't work.
        # if i == index:
        #     return curr.item  # curr could be None!
        # else:
        #     raise IndexError

        if curr is None:
            # There is no item at that index. We ran out of Nodes.
            raise IndexError
        else:
            # We know curr is not None.
            # We already said we know that
            #      (curr is None) or (i == index) or both!
            # Therefore, i == index!
            return curr.item

    def insert(self, index: int, item: Any) -> None:
        """Insert at the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        >>> linky = LinkedList([0, 1, 2, 3, 4])
        >>> linky.insert(3, 99)
        >>> print(linky)
        [0 -> 1 -> 2 -> 99 -> 3 -> 4]
        """
        new_node = _Node(item)
        curr = self._first
        i = 0
        if index == 0:
            # Insert at the front
            self._first = new_node
            new_node.next = curr
        else:
            # loop to the right spot.
            # Stopping condition: (i == index-1) or (curr is None)
            # Continuing condition: not((i == index-1) or (curr is None))
            # DeMorgan's law gives us: (i != index-1) and (curr is not None)
            while (i != index - 1) and (curr is not None):
                curr = curr.next
                i += 1
            # We know that:
            # (i == index-1) or (curr is None) or both
            if curr is None:
                # The index was past the end of the list.
                # The logic is missing some things here.  Think about that.
                raise IndexError
            else:
                # We are at the node before where the new node
                # needs to go.
                rest_of_list = curr.next
                curr.next = new_node
                new_node.next = rest_of_list

    # def pop(self, index: int) -> Any:
    #     """Remove and return the item at position <index>.
    #
    #     Raise IndexError if index >= len(self) or index < 0.
    #
    #     >>> lst = LinkedList([1, 2, 10, 200])
    #     >>> lst.pop(1)
    #     2
    #     >>> lst.pop(2)
    #     200
    #     >>> lst.pop(148)
    #     Traceback (most recent call last):
    #     IndexError
    #     >>> lst.pop(0)
    #     1
    #     """
    #     pass

    # def remove(self, item: Any) -> None:
    #     """Remove the FIRST occurrence of <item> in this list.
    #
    #     Do nothing if this list does not contain <item>.
    #     (Note: Python lists actually raise a ValueError.)
    #
    #     >>> lst = LinkedList([1, 2, 3])
    #     >>> lst.remove(2)
    #     >>> str(lst)
    #     '[1 -> 3]'
    #     >>> lst.remove(2)
    #     >>> str(lst)
    #     '[1 -> 3]'
    #     >>> lst.remove(3)
    #     >>> str(lst)
    #     '[1]'
    #     >>> lst.remove(1)
    #     >>> str(lst)
    #     '[]'
    #     >>> lst.remove(1)
    #     >>> str(lst)
    #     '[]'
    #     """
    #     pass




























    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if items == []:  # No items, and an empty list!
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

    # You did this in Prep 5:
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


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()

    import doctest
    doctest.testmod()
