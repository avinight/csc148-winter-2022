"""ADTs: Stacks, Feb 2, 2022

**************************
Copyright information
**************************
CSC148
Department of Computer Science,
University of Toronto

**************************
Module description
**************************
This module contains a stack class you've seen before.  We tried popping from
an empty Stack and observed the error that is raised. It tells us that we called
list.pop on an empty list. This is true, because Stack's pop method calls
list's pop method on its instance variable that holds the stack contents.
But it is not a very helpful error message for the programmer of client code
to see: they don't care about how we implemented our stack, they just want to
use it.  Further, the error reveals details about our private instance variable.

We improved on this by having the pop method seize control of the error raised.
It notices that it is about to call pop on an empty list and instead raises our
own, custom error: PopEmptyStackError.  This gives client code a more helpful
error message and keeps our implementation details private.  It's super easy
to define a new error.  This will suffice:
    class DianeNeedsCoffeeError(Exception):
        pass
Any time we want to generate this error, we just say:
    raise DianeNeedsCoffeeError    # "raise" is a keyword in Python.
On Friday, we'll learn more about what happens
when an error is raised.

We made one further improvement: we added a __str__ method to our
PopEmptyStackError class. The string that it returns is automatically reported
whenever a PopEmptyStackError is raised.  This provides an even more helpful
message to the client code.
"""
from typing import Generic, List, Optional, TypeVar, Any


###############################################################################
# Stacks
###############################################################################

class PopEmptyStackError(Exception):
    pass

    def __str__(self) -> str:
        return 'Never pop an empty stack again or else!'


class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.
    """
    # === Private Attributes ===
    # _items:
    #     The items stored in this stack. The end of the list represents
    #     the top of the stack.
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this stack contains no items.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('hello')
        >>> s.is_empty()
        False
        """
        return self._items == []

    def push(self, item: Any) -> None:
        """Add a new element to the top of this stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if self.is_empty():
            raise PopEmptyStackError
        else:
            return self._items.pop()


if __name__ == '__main__':
    pass
