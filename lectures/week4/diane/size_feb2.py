"""Stack size, Feb 2, 2022

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains various versions of a function for computing
the size of a stack, as seen on our worksheet.

We worked through the four versions of function size and discovered that none
of them were good implementations.  We then tried out the idea of using a
temporary queue to hold our stack contents while we popped it and counted,
and then restoring the stack to its original state from the queue.  A queue
seemed like a great idea because it keeps things in the same order the arrived
in.  But it didn't work!

I left you to trace on paper what would happen if we used a temporary stack
instead.  Try that, and based on your tracing, implement size correctly below.
"""

from stack_feb2 import Stack


def size_v1(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size_v1(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size_v1(s)
    3
    """
    count = 0
    for _ in s:
        count += 1
    return count


def size_v2(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size_v2(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size_v2(s)
    3
    """
    return len(s._items)


def size_v3(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size_v3(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size_v3(s)
    3
    """
    count = 0
    while not s.is_empty():
        s.pop()
        count += 1
    return count


def size_v4(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size_v4(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size_v4(s)
    3
    """
    copy = s
    count = 0
    while not copy.is_empty():
        copy.pop()
        count += 1
    return count


def size(s: Stack) -> int:
    """Return the number of items in s.

    >>> s = Stack()
    >>> size(s)
    0
    >>> s.push('hi')
    >>> s.push('more')
    >>> s.push('stuff')
    >>> size(s)
    3
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
