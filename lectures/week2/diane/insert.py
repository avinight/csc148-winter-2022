"""Testing: example with doctest

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This function looks pretty good, and it passes its own doctests.
Try running the module in PyCharm to observe that it does.  (And like I did
in class, you can change the expected result to something silly in order to
see what happens if a doctest fails.

We agreed that it would be foolish to believe this code works perfectly based
on that one doctest example.  See test_insert.py for some better testing of
the function.
"""
from typing import List


def insert_after(lst: List[int], n1: int, n2: int) -> None:
    """After each occurrence of <n1> in <lst>, insert <n2>.

    >>> lst = [5, 1, 2, 1, 6]
    >>> insert_after(lst, 1, 99)
    >>> lst
    [5, 1, 99, 2, 1, 99, 6]
    """
    i = 0
    while i < len(lst):
        if lst[i] == n1:
            lst.insert(i+1, n2)
        i += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
