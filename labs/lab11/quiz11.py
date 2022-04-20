"""
Define a function remove_duplicates, which takes a sorted list, and returns a
new list with the same items as the original, but without duplicates. 
Note that this function does not mutate the original list.

Take advantage of the fact that the input list is sorted! Your algorithm should
run in time linear in the length of the list.
"""

def remove_duplicates(lst: List) -> List:
    """Return a sorted list containing the same values as <lst>, but without duplicates.

    Precondition: <lst> is sorted.

    >>> remove_duplicates([1, 2, 2, 2, 3, 10, 10, 20])
    [1, 2, 3, 10, 20]
    """
    # TODO: Implement this


if __name__ == '__main__':
	import doctest
	doctest.testmod()
