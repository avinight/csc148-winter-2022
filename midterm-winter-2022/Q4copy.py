"""
Question (5 marks)

Implement the function below according to the docstring provided.

Rules:
- You may use the Stack and Queue classes provided in module 'adts' to
  create temporary Stack and/or Queue objects. These are the same Stack and
  Queue classes you have seen before.
- You must NOT create any other compound objects (lists, dictionaries, etc.)
- You may create variables to store individual values (counters, items that
  have been popped or dequeued, etc.)
- You may add doctest examples if desired.

Hint: You may find it helpful to use modular division by 2, that is, "% 2".

TO HAND IN: Add your code to this file and hand it in on MarkUs.  Be sure to
run the self-test on MarkUs to avoid failing all our tests due to a silly error.

--------------------------------------------------------------------------------
This file is Copyright (c) 2022 University of Toronto
All forms of distribution, whether as given or with any changes, are
expressly prohibited.
--------------------------------------------------------------------------------
"""
from adts import Stack, Queue


def remove_every_other(s: Stack) -> None:
    """Modify s to remove every other element, starting from the top-most
    element.

    Do NOT return a new stack. Modify the one that is given.

    Precondition: There is at least one item in s.

    >>> s = Stack()
    >>> s.push('one')
    >>> s.push('two')
    >>> s.push('three')
    >>> s.push('four')
    >>> s.push('five')

    >>> remove_every_other(s)
    >>> s.pop()
    'four'
    >>> s.pop()
    'two'
    >>> s.is_empty()
    True
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
