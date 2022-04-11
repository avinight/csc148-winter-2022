"""Recursive sorting algorithms

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
In-place quicksort code as of Wednesday, April 6th.  Today we used the in-place
partition method from last week to implement an in-place quicksort.

We had to modify the partition method first, so that we could control what
portion of the list it works on, and so that it would report back information
about its outcome: where the (green) portion of the partitioned sublist
(all the values <= the pivot) ended up, and where the (blue) portion of the
partitioned sublist (all the values > the pivot) ended up.  We also realized
that someone needed to put the pivot in place. We had partition do it. This
meant that it could report back simply where the pivot ended up and that was
enough for us to find the "green" and "blue" sublists.

We encountered some fun errors when we doctested the code. Several were due
to having not changed the doctests to match the new code. We also hit an
infinite recursion error because had left the base case test as
    if len(lst) < 2
whereas it should have been checking just the size of the portion of the list
we're sorting.  So we changed it to
    if len(lst[start:end]) < 2
and the code worked!  But we realized this slicing is costly and came up with
this much faster alternative:
    if end - start < 2

We had left the doctest for _in_place_partition with an error in the expected
result.  I have fixed that. (A great exercise would be to go through partition
by hand on that example and see if you come up with the same answer.)
I also added in a 2nd doctest example based on one we'd traced through on the
slides for in-place partition.

Finally, we added a "wrapper" around the new quicksort, so that client code
doesn't have to worry about sending in a start and end. I have made the
version that takes start and end arguments and named it with an underscore so
it is a private helper, and repurposed its name for the client-friendly
version.
"""
from typing import Any, List, Tuple


###############################################################################
# Standard (non-mutating) mergesort and quicksort
###############################################################################
def mergesort(lst: List) -> List:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.

    >>> mergesort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves. Need a helper here!
        return _merge(left_sorted, right_sorted)


def _merge(lst1: List, lst2: List) -> List:
    """Return a sorted list with the elements in <lst1> and <lst2>.

    Precondition: <lst1> and <lst2> are sorted.
    """
    index1 = 0
    index2 = 0
    merged = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            merged.append(lst1[index1])
            index1 += 1
        else:
            merged.append(lst2[index2])
            index2 += 1

    # Now either index1 == len(lst1) or index2 == len(lst2).
    # assert index1 == len(lst1) or index2 == len(lst2)
    # The remaining elements of the other list
    # can all be added to the end of <merged>.
    # Note that at most ONE of lst1[index1:] and lst2[index2:]
    # is non-empty, but to keep the code simple, we include both.
    return merged + lst1[index1:] + lst2[index2:]


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

# Thinking through the correct expected result from the doctest example:
# 7, 4, -1, 42, 9, 18, 22, 8, 3
# 7


def _in_place_partition(lst: List[int], start: int, end: int) -> int:
    """Mutate lst[start:end] so that it is partitioned,
    using lst[start] as the pivot.

    Return the index of the pivot.

    >>> numbers = [7, 4, -1, 42, 9, 18, 22, 8, 3]
    >>> _in_place_partition(numbers, 0, len(numbers))
    3
    >>> numbers
    [3, 4, -1, 7, 18, 22, 8, 9, 42]
    >>> numbers = [10, 7, 20, 30, 3, 6]
    >>> _in_place_partition(numbers, 0, len(numbers))
    3
    >>> numbers
    [3, 7, 6, 10, 30, 20]
    """
    pivot = lst[start]
    small_i = start + 1
    big_i = end
    while small_i < big_i:
        if lst[small_i] <= pivot:
            small_i += 1
        else:
            # Know: lst[small_i] > pivot
            lst[small_i], lst[big_i - 1] = lst[big_i - 1], lst[small_i]
            big_i = big_i - 1
    # Know: small_i == big_i
    # Put the pivot into place between the two zones.
    lst[start], lst[small_i - 1] = lst[small_i - 1], lst[start]

    return small_i - 1


def in_place_quicksort(lst: List[int]) -> None:
    _in_place_quicksort(lst, 0, len(lst))


def _in_place_quicksort(lst: List[int], start: int, end: int) -> None:
    """Mutate lst so that it is sorted.

    >>> numbers = [10, 2, 5, -6, 17, 10]
    >>> _in_place_quicksort(numbers, 0, len(numbers))
    >>> numbers
    [-6, 2, 5, 10, 10, 17]
    """
    if end - start < 2:
        # Know: lst is sorted.
        pass
    else:
        # Partition rest of list into two halves
        pivot_index = _in_place_partition(lst, start, end)

        # Recurse on each partition
        _in_place_quicksort(lst, start, pivot_index)
        _in_place_quicksort(lst, pivot_index + 1, end)


################################################################################
# Insertion sort (for comparison only)
################################################################################
def insertion_sort(lst: list, start: int = 0, end: int = None) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    >>> lst = [10, 2, 5, -6, 17, 10]
    >>> insertion_sort(lst)
    >>> lst
    [-6, 2, 5, 10, 10, 17]
    """
    if end is None:
        end = len(lst)

    for i in range(start + 1, end):
        num = lst[i]
        left = start
        right = i
        while right - left > 1:
            mid = (left + right) // 2
            if num < lst[mid]:
                right = mid
            else:
                left = mid + 1

        # insert
        if lst[left] > num:
            lst[left + 1:i + 1] = lst[left:i]
            lst[left] = num
        else:
            lst[right+1:i+1] = lst[right:i]
            lst[right] = num


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
# import python_ta
# python_ta.check_all()
