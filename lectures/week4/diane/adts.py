"""ADTs: Stacks and Queues and timing experiments, 4 February 2022

=== Copyright information ===
CSC148
Department of Computer Science
University of Toronto

=== Module description ===
Today we implemented a second version of stack, with the bottom of the stack at
the *end* of the list. We used the timing experiment below to see how the time
to do some pushing and popping (using the original stack implementation) changed
as we ran it on larger and larger stacks.  Then we ran the experiment again
using the second version of stack.  The results were strikingly different for
the two implementations. This lead us to explore how lists are implemented
by Python. (See my ipad notes on this.)

Try running the two experiments yourself and looking at the results.
"""
from typing import Generic, List, Optional, TypeVar, Any


class EmptyStackError(Exception):
    """Exception raised when an error occurs."""


###############################################################################
# Stacks
###############################################################################
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

        Raise an EmptyStackError if this stack is empty.

        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop()


class Stack2:
    """Alternate stack implementation.

    This implementation uses the *front* of the Python list to represent
    the top of the stack.
    """
    # === Private Attributes ===
    # _items:
    #     The items stored in the stack. The front of the list represents
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
        self._items.insert(0, item)

    def pop(self) -> Any:
        """Remove and return the element at the top of this stack.

        Raise an EmptyStackError if this stack is empty.

        >>> s = Stack()
        >>> s.push('hello')
        >>> s.push('goodbye')
        >>> s.pop()
        'goodbye'
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._items.pop(0)


###############################################################################
# Queues
###############################################################################
class Queue:
    """A first-in-first-out (FIFO) queue of items.

    Stores data in a first-in, first-out order. When removing an item from the
    queue, the most recently-added item is the one that is removed.
    """
    # === Private attributes ===
    # _items: a list of the items in this queue
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self._items = []

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.

        >>> q = Queue()
        >>> q.is_empty()
        True
        >>> q.enqueue('hello')
        >>> q.is_empty()
        False
        """
        return self._items == []

    def enqueue(self, item: Any) -> None:
        """Add <item> to the back of this queue.
        """
        self._items.append(item)

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
        if self.is_empty():
            return None
        else:
            return self._items.pop(0)


###############################################################################
# Timing experiments
###############################################################################
def push_and_pop(s: Stack) -> None:
    """Push and pop a new item onto the given stack."""
    s.push(1)
    s.pop()


# def setup_queues(qsize: int, n: int) -> List[Queue]:
#     """Return a list of <n> queues, each of the given size."""
#     # Experiment preparation: make a list containing <n> queues,
#     # each of size <qsize>.
#     # You can "cheat" here and set your queue's _items attribute
#     # directly to a list of the appropriate size by writing something like
#     #
#     # queue._items = list(range(qsize))
#     #
#     # to save a bit of time in setting up the experiment.
#     queue_list = []
#     for _ in range(n):
#         q = Queue()
#         # This line is cheating, but makes your experiment a bit faster.
#         q._items = list(range(qsize))
#         queue_list.append(q)
#     return queue_list


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all(config={'pyta-type-check': True})
    # import doctest
    # doctest.testmod()

    # Import the main timing function.
    from timeit import timeit

    # The stack sizes we want to try.
    STACK_SIZES = [1000, 10000, 100000, 1000000, 10000000]
    for stack_size in STACK_SIZES:
        # Uncomment the stack implementation that we want to time.
        # stack = Stack()
        stack = Stack2()

        # Bypass the Stack interface to create a stack of size <stack_size>.
        # This speeds up the experiment, but we know this violates
        # encapsulation!
        stack._items = list(range(stack_size))

        # Call push_and_pop(stack) 1000 times, and store the time taken in
        # <time>. The globals=globals() is used for a technical reason that
        # you can ignore.
        time = timeit('push_and_pop(stack)', number=1000, globals=globals())

        # Finally, report the result. The :>8 is used to right-align the
        # stack size when it's printed, leading to a more visually-pleasing
        # report.
        print(f'Stack size {stack_size:>8}, time {time}')

    # # Queue timing experiment.
    # QUEUE_SIZES = [10000, 20000, 40000, 80000, 160000]
    # TRIALS = 300
    #
    # for queue_size in QUEUE_SIZES:
    #     queues = setup_queues(queue_size, TRIALS)
    #     time = 0
    #     for queue in queues:
    #         time += timeit('queue.enqueue(1)', number=10, globals=globals())
    #     print(f'enqueue: Queue size {queue_size:>7}, time {time}')
    #
    # for queue_size in QUEUE_SIZES:
    #     queues = setup_queues(queue_size, TRIALS)
    #     time = 0
    #     for queue in queues:
    #         time += timeit('queue.dequeue()', number=10, globals=globals())
    #     print(f'dequeue: Queue size {queue_size:>7}, time {time}')
