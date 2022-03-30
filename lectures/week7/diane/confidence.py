"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
A recursion function we'll use for discussing our confidence in
recursion itself.
"""
from typing import Union, List


def nested_sum(obj: Union[int, List]) -> int:
    """Return the sum of the numbers in obj.

    >>> nested_sum([[1, 2, 3], 4, [[5]]])
    15
    >>> nested_sum([])
    0
    """
    if isinstance(obj, int):
        return obj
    else:
        s = 0
        for sublist in obj:
            s += nested_sum(sublist)
        return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
