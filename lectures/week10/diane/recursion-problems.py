"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Demonstration of various ways that recursion can go wrong.

We talked through (and observed) the problems with examples 1, 2 and 3.
Exercise for you: Identify the problem with the binary search method.
The problem size (the difference between i and j) always gets smaller,
doesn't it? i and j get closer together on every iteration, until
eventually i == j.  Or do they?
"""

from typing import List

# ===== Example 1 =====


def nested_sum(obj) -> int:
    """Return the sum of all integers in obj.

    >>> nested_sum([1, 2, [3, 4, 5], [[6]], 7])
    28
    """
    answer = 0
    for sublist in obj:
        answer += nested_sum(sublist)
    return answer


# ===== Example 2 =====

def factorial(n):
    """Return n factorial.

    >>> factorial(5)
    120
    """
    return n * factorial(n-1)


# ===== Example 3 =====

def f(n: int) -> int:
    """Just a recursion demo.

    Precondition: n >= 0

    >>> f(4)
    6
    >>> f(5)
    6
    """
    if n == 0:
        return 1
    else:
        return n + f(n - 2)


# ===== Example 4 =====
#
# def bsearch(lst: List[int], i: int, j: int, item: int) -> bool:
#     """Return True iff item occurs in lst[i:j].
#
#     Precondition: i <= j.
#
#     >>> lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     >>> bsearch(lst, 0, 10, 7)
#     True
#     >>> bsearch(lst, 0, 10, 99)
#     False
#     >>> bsearch(lst, 0, 5, 99)
#     """
#     print(f'Searching [{i}:{j}]')
#     if i == j:
#         # Searching an empty sublist, so item cannot be there.
#         return False
#     else:
#         mid = (i + j) // 2
#         if item < lst[mid]:
#             # Go to the LHS. No need to include lst[mid] because item is less.
#             return bsearch(lst, i, mid, item)
#         else:
#             # To to the RHS.  Include lst[mid] because item is >= lst[mid].
#             return bsearch(lst, mid, j, item)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
