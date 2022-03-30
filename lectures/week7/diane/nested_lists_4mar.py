"""Recursion

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Nested list code as of Friday, March 4th.  Today we worked on first_at_depth.
We followed these steps:
1. Write doctest examples. Why write these before the code? If you don't, it's
   like getting in the car and saying "I'm driving to my appointment in Markham"
   but not having a clear idea of where exactly in Markham.  You might
   get to the right place eventually, but you'll probably waste time driving
   around a lot.
       It's only when you think through the scenarios carefully that you fully
   understand what your code needs to do. Notice how we had to think a bit
   about the empty list. Even a plain int could lead to two different outcomes
   depending on d. Taking the time to sort that out massively improves the
   chance that our code will work without us having to do a lot of debugging.
   Notice that it required us to read the docstring again carefully.
       Writing tests before code is so important that it has a name:
   Test-Driven Development. It is pretty standard in industry.
2. For a non-trivial example, write down the recursive calls that it will need
   to make. For each of them, write down what the call will do (will it mutate
   the arguments?) and/or what it will return if it works properly. We take
   the same attitude as in partial tracing: we don't worry about how that
   recursive call will iterate or recurse -- what do we care? We're lazy! Let's
   mind our own business and let the recursive call take care of its job.
3. Then, finally, write the code. I've left the recursive case for you to
   finish. Try to do that before Wednesday.


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
    >>> first_at_depth([], 0)
    None
    >>> first_at_depth([], 17)
    None
    """
    if isinstance(obj, int):
        if d == 0:
            return obj
        else:
            return None
    else:
        # Check first-at-depth on each sublist, with d-1
        # The first time we get something other than None, that's the answer!
        # If we never do, return None
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

    # import doctest
    # doctest.testmod()

    # names = []
    # gen(names)

    answer = num_positives([1, 2, -3, [4, 5], 6])
