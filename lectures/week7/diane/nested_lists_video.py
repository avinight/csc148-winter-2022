"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Nested list code we wrote on Wed 25 Feb 2021.

Pattern we can often use:

    if isinstance(obj, int):
        ...
    else:
        for sublist in obj:
            ... f(sublist) ...

"""
from typing import List, Optional, Union


# This function is traced on the first worksheet.
def flatten(obj: Union[int, list]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>.

    The integers are returned in the left-to-right order they appear
    in <obj>.

    >>> flatten(6)
    [6]
    >>> flatten([1, [-2, 3], -4])
    [1, -2, 3, -4]
    >>> flatten([[0, -1], -2, [[-3, [-5]]]])
    [0, -1, -2, -3, -5]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        for sublist in obj:
            s.extend(flatten(sublist))
        return s


# This function is traced on the first worksheet.
def uniques(obj: Union[int, List]) -> List[int]:
    """Return a (non-nested) list of the integers in <obj>, with no duplicates.

    >>> uniques([13, [2, 13], 4])
    [13, 2, 4]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        # Lookup the set built-in type
        for sublist in obj:
            # new_items = uniques(sublist)
            # # Need to check whether each item in new_items is in s
            # for item in new_items:
            #     if item not in s:
            #         s.append(item)
            s.extend(uniques(sublist))
        return uniques(s)


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.

    >>> nested_list_contains(1, 1)
    True
    >>> nested_list_contains(42, 1)
    False
    >>> nested_list_contains([1, [22], [2, [3, 4]], 98], 3)
    True
    >>> nested_list_contains([], 13)
    False
    """
    if isinstance(obj, int):
        return obj == item
    else:
        # Know: obj is a list.
        for sublist in obj:
            # We can't necessarily return after checking just this sublist.
            # An early sublist may say "no" even if a later one says "yes"!

            # if answer == True:
            #     return True
            # else:
            #     pass
            if nested_list_contains(sublist, item):
                return True
        # Know: we didn't find it, even after looking through
        # every sublist!  Therefore it's not there.
        return False


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """Return the first (leftmost) number in <obj> at depth <d>.

    Return None if there is no item at depth d.

    Precondition: d >= 0.
    """
    pass


def add_one(obj: Union[list, int]) -> None:
    """Add one to every number stored in <obj>. Do nothing if <obj> is an int.

    If <obj> is a list, *mutate* it to change the numbers stored.
    (Don't return anything in either case.)

    >>> lst0 = 1
    >>> add_one(lst0)
    >>> lst0
    1
    >>> lst1 = []
    >>> add_one(lst1)
    >>> lst1
    []
    >>> lst2 = [1, [2, 3], [[[5]]]]
    >>> add_one(lst2)
    >>> lst2
    [2, [3, 4], [[[6]]]]
    """
    pass


# A silly function. It expects a list of strings.  In the main block, we send
# it an empty list.  This is acceptable -- it is a list of strings in a trivial
# sense.
# This is analogous to the fact that we consider an empty list to satisfy our
# definition of a "nested list" (as defined in the csc148 Lecture Notes).
def gen(lst: List[str]) -> None:
    print('Silly!')


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()

    # import doctest
    # doctest.testmod()

    names = []
    gen(names)
