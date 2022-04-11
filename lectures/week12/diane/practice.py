"""
A practice problem with recursion on a nested list. This one builds up a
value to return.
"""
from typing import Union, Dict, List


def create_depth_map(obj: Union[int, list]) -> Dict[int, List[int]]:
    """
    Return a dictionary whose keys are the depths of the items in <obj> and the
    value for a given key is a list of the items at that depth.

    The depth of an object in a nested list is the number of nested lists
    enclosing the object. The depth of a single int is 0.

    If no items occur at a given depth, that key should not appear in the
    dictionary.

    >>> create_depth_map(148) == {0: [148]}
    True
    >>> create_depth_map([]) == {}
    True
    >>> # To avoid a line over 80 characters, this example is in two steps:
    >>> answer = create_depth_map([19, [[22]], [-3, [8], 47]])
    >>> answer == {1: [19], 3: [22, 8], 2: [-3, 47]}
    True
    >>> create_depth_map([[],[[21]]]) == {3: [21]}
    True
    >>> create_depth_map([62, [8], [8, 8]]) == {1: [62], 2 : [8, 8, 8]}
    True
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
