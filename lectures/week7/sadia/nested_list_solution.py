"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Starter code for some recursive functions we'll write that operate on
nested lists.

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
            new_items = uniques(sublist)
            # Need to check whether each item in new_items is in s
            for item in new_items:
                if item not in s:
                    s.append(item)

        return s


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """Return whether the given item appears in <obj>.

    >>> nested_list_contains(1, 1)
    True
    >>> nested_list_contains(1, 3)
    False

    >>> nested_list_contains([1, [22], [2, [3, 4]]], 3)
    True
    """

    if isinstance(obj, int):
        # implement base case
        return obj == item
    else:
        # know: obj is a list
        for sublist in obj:
            if nested_list_contains(sublist, item):
                return True

        # know: we didn't find it, even after looking through every sublist!
        return False


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """Return the first (leftmost) number in <obj> at depth <d>.

    Return None if there is no item at depth d.

    Precondition: d >= 0.

    >>> first_at_depth(100, 0)
    100
    >>> first_at_depth(100, 3) is None
    True

    >>> first_at_depth([10, [[20]], [30, 40]], 2)
    30
    >>> first_at_depth([10, [[20]], [30, 40]], 0)
    None
    >>> first_at_depth([10, 30, 40], 8)
    None
    """

    if isinstance(obj, int):
        if d == 0:
            return obj
        else:
            return None

    else:
        # know: obj is a list
        if d == 0:
            # there is nothing at depth 0 in a list!
            return None

        for sublist in obj:
            item = first_at_depth(sublist, d-1)
            if item is not None:
            # if it's not None, we know it's an int cause of the type contract
                return item

        # if we reach here, we know: no sublist of obj contained an int at
        # depth-1. therefore, obj contains no int at depth d!!
        return None

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

    #if isinstance(obj, int):
    #    pass
    #else: # if it is a list
    # alternate if statement for the above:
    if isinstance(obj, list):
        for i in range(len(obj)):
            # know: each obj[i] is either an int or a list
            if isinstance(obj[i], int):
                obj[i] += 1 # using index this way MUTATES list, which is what we want :)
            else: # obj[i] is another nested list!
                add_one(obj[i])





if __name__ == '__main__':
    import python_ta
    python_ta.check_all()

    import doctest
    doctest.testmod()
