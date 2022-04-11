"""An implementation of quicksort and in-place quicksort.

=== CSC148 ===
Department of Computer Science,
University of Toronto
"""
from typing import Any, List, Tuple


###############################################################################
# Standard (non-mutating) quicksort
###############################################################################

def quicksort(lst: List) -> List:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    >>> quicksort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Pick pivot to be first element.
        # Could make lots of other choices here (e.g., last, random)
        pivot = lst[0]

        # Partition rest of list into two halves
        smaller, bigger = _partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def _partition(lst: List, pivot: Any) -> Tuple[List, List]:
    """Return a partition of <lst> with the chosen pivot.

    Return two lists, where the first contains the items in <lst>
    that are <= pivot, and the second is the items in <lst> that are > pivot.
    """
    smaller = []
    bigger = []

    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)

    return smaller, bigger


################################################################################
# In-place quicksort
################################################################################
def in_place_quicksort(lst: List, start: int, end: int) -> None:
    """Sort lst[start:end] in non-decreasing order.

   This is an in-place (mutating) version of quicksort; it DOES mutate the
   input list.

   >>> lst = [10, 2, 5, -6, 17, 10]
   >>> in_place_quicksort(lst, 0, len(lst))
   >>> lst
   [-6, 2, 5, 10, 10, 17]
    """

    if end - start < 2:
        pass
    else:
        # Partition rest of list into two halves
        pivot_index = _in_place_partition(lst, start, end)

        # Recurse on each partition
        in_place_quicksort(lst, start, pivot_index)
        in_place_quicksort(lst, pivot_index + 1, end)



def _in_place_partition(lst: List[int], start: int, end: int) -> int:
    """Mutate <lst> so that it is partitioned with pivot lst[0].

    Let pivot = lst[0].
    The elements of <lst> are moved around so that the final list looks like

        [x1, x2, ... x_m, pivot, y1, y2, ... y_n],

    where each of the x's is less than or equal to the pivot,
    and each of the y's is greater than the pivot.

    The *new index of the pivot* is returned

    Precondition: lst != [].

    >>> lst = [10, 3, 20, 5, -6, 30, 7]
    >>> _in_place_partition(lst, 0, 7)
    4
    >>> lst[4]  # Note that 10 is at index 4
    10
    >>> set(lst[:4]) == {3, 5, -6, 7}
    True
    >>> set(lst[5:]) == {20, 30}
    True
    """
    pivot = lst[start]
    small_i = start + 1
    big_i = end

    # The main loop
    while small_i < big_i:
        if lst[small_i] <= pivot:
            small_i += 1
        else:
            lst[small_i], lst[big_i - 1] = lst[big_i - 1], lst[small_i]
            big_i -= 1

    # At this point, all elements have been compared.
    # The final step is to move the pivot into its correct position in the list
    # (after the "smaller" partition, but before the "bigger" partition).
    lst[start], lst[small_i - 1] = lst[small_i - 1], lst[start]

    # return the boundary between smaller and bigger parts (i.e. pivot index)
    return small_i - 1



if __name__ == '__main__':
    import doctest

    doctest.testmod()

    import python_ta

    python_ta.check_all()
