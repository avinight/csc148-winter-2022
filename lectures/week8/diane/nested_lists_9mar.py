"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Nested list code as of Wednesday, March 9th. Today we finished first_at_depth
by implementing the recursive case.  We realized that an extra if-statement
was required to prevent us from making a recursive call with d = -1, which
would violate the method preconditions.

Then we wrote add_one, our first mutating method on a nested list. This one
had two wrinkles: (1) a recursive call where we pass an int can't possibly
mutate it, so we had to do the work of increasing by 1 ourselves (geez!)
(2) our first attempt, where we iterated through the items in the list did
not change the list at all. This was an instance of a classic list error
whose most simple example is this:
    >>> lst = [1, 2, 3, 4]
    >>> for item in lst:
    ...     item += 1
    ...
    >>> lst
    [1, 2, 3, 4]
You learned long ago to solve this problem by iterating over the indexes
instead:
    >>> for i in range(len(lst)):
    ...     lst[i] += 1
    ...
    >>> lst
    [2, 3, 4, 5]
To fix method add_one, we did the same thing.  See below.




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

    >>> first_at_depth(100, 0)
    100
    >>> first_at_depth(100, 3) is None
    True
    >>> first_at_depth([10, [[20]], [30, 40]], 2)
    30
    >>> first_at_depth([10, [[20]], [30, 40]], 0) is None
    True
    >>> first_at_depth([], 0) is None
    True
    >>> first_at_depth([], 17) is None
    True
    >>> first_at_depth([1, [2, [39], [3, 3]], 1, 1, [[[4]], 2, 2], 1], 3)
    39
    """
    if isinstance(obj, int):
        if d == 0:
            return obj
        else:
            return None
    else:
        # Know:
        # obj is a list.
        # d >= 0.

        # If d happens to be 0, suppose obj = [1, 2, [5, 6, [[[7]]]], 8]]]
        # In fact, doesn't matter what list obj is, there is nothing at depth 0
        # in it.  So we need to return None in the case where d is 0.
        if d == 0:
            return None
        else:
            # Check first-at-depth on each sublist, with d-1.
            # The first time we get something other than None, that's the
            # answer!
            # If we never do, return None.
            for sublist in obj:
                result = first_at_depth(sublist, d - 1)
                # If we get an int back, return it and stop looping.
                # But if we get None back, keep looping.
                # Note: another way to write this condition is to say
                # "if result". Python will treat None as False and an int
                # as True -- cool!
                if isinstance(result, int):
                    return result
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
    if isinstance(obj, int):
        pass
    else:
        # Know obj is a list
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                # Know sublist is an int.
                # It needs to be one bigger.
                obj[i] += 1
            else:
                # Know sublist is a list.
                add_one(obj[i])


def num_positives(obj: Union[int, list]) -> int:
    """
    Return the number of integers in obj.

    >>> num_positives(148)
    1
    >>> num_positives([])
    0
    >>> num_positives([19, [[22]], [-3, [8], 47]])
    4
    >>> num_positives([[],[[21]]])
    1
    >>> num_positives([62, [-8], [8, -8]])
    2
    """
    count = 0
    if isinstance(obj, int):
        if obj > 0:
            count = count + 1
    else:
        for sublist in obj:
            num_positives(sublist)
    return count


# A silly function. It expects a list of strings.  In the main block, we send
# it an empty list.  This is acceptable -- it is a list of strings in a trivial
# sense.
# This is analogous to the fact that we consider an empty list to satisfy our
# definition of a "nested list" (as defined in the csc148 Lecture Notes).
def gen(lst: List[str]) -> None:
    print('Silly!')


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()
    #
    # import doctest
    # doctest.testmod()
    #
    # names = []
    # gen(names)

    answer = num_positives([1, 2, -3, [4, 5], 6])

    # [11, 12, [21, [31, 32], 22], 13, [[32]], 14]
