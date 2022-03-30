"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
In this module, you will develop an implementation of the Queue ADT.
It will be helpful to review the stack implementation from lecture.

After you've implemented the Queue, you'll write two different functions that
operate on a queue, paying attention to whether or not the queue should be
modified.
"""
from typing import Any, List, Optional


# TODO: implement this class! Note that you'll need at least one private
# attribute to store items.
class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.
    """
    data: List

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self.data = []

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.

        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue('hello')
        >>> q.is_empty()
        False
        """
        return self.data == []

    def enqueue(self, item: Any) -> None:
        """Add <item> to the back of this queue.
        """
        self.data.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return the item at the front of this queue.

        Return None if this Queue is empty.
        (We illustrate a different mechanism for handling an erroneous case.)

        >>> q = Queue()
        >>> q.enqueue('hello')
        >>> q.enqueue('goodbye')
        >>> q.dequeue()
        'hello'
        """
        if self.data:
            return self.data.pop(0)
        return None


def product(integer_queue: Queue) -> int:
    """Return the product of integers in the queue.

    Remove all items from the queue.

    Precondition: integer_queue contains only integers.

    >>> q = Queue()
    >>> q.enqueue(2)
    >>> q.enqueue(4)
    >>> q.enqueue(6)
    >>> product(q)
    48
    >>> q.is_empty()
    True
    """
    t = 1
    while not integer_queue.is_empty():
        t = t * integer_queue.dequeue()
    return t


def product_star(integer_queue: Queue) -> int:
    """Return the product of integers in the queue.

    Precondition: integer_queue contains only integers.

    >>> primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> prime_line = Queue()
    >>> for prime in primes:
    ...     prime_line.enqueue(prime)
    ...
    >>> product_star(prime_line)
    6469693230
    >>> prime_line.is_empty()
    False
    """
    q1 = Queue()
    q2 = Queue()
    while not integer_queue.is_empty():
        integer = integer_queue.dequeue()
        q1.enqueue(integer)
        q2.enqueue(integer)

    while not q2.is_empty():
        integer = q2.dequeue()
        integer_queue.enqueue(integer)

    t = product(integer_queue)

    while not q1.is_empty():
        integer = q1.dequeue()
        integer_queue.enqueue(integer)

    return t


if __name__ == '__main__':
    import doctest
    doctest.testmod()
