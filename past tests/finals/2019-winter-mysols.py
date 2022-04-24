from typing import List, Tuple, Union
import labs

def consistent_depth(obj: Union[int, List]) -> bool:
    """Return True iff obj is nested to a consistent depth
    throughout.
    >>> consistent_depth(6)
    True
    >>> consistent_depth([1, 2, 3, 4])
    True
    >>> consistent_depth([1, 2, [3], 4])
    False
    >>> consistent_depth([[1], [2, 3], [4]])
    True
    >>> consistent_depth([1, [2, 3], 4])
    False
    >>> consistent_depth([[[1]], [[2], [3], [4], []]])
    True
    >>> consistent_depth([[1], [[2], [3], [4], []]])
    False
    """
    if isinstance(obj, int):
        return True
    else:
        c, depth = consistent_helper(obj)
        return c


def consistent_helper(obj: Union[int, List]) -> Tuple[bool, int]:
    """Return a tuple of c, depth."""
    if isinstance(obj, int):
        return True, 0
    else:
        depths = []
        depth = 1
        for elem in obj:
            depth = 1
            c, d = consistent_helper(elem)
            depth = depth + d
            depths.append(depth)
        return all(d == depths[0] for d in depths), depth


def insert_linked_list(self, other: LinkedList, pos: int) -> None:
    """Insert <other> into this linked list immediately before position pos.
    Do not make any new nodes, just link the existing nodes in.
    Preconditions:
        0 <= pos < len(self)
        len(other) >= 1
    >>> lst1 = LinkedList([0, 1, 2, 3, 4, 5])
    >>> lst2 = LinkedList([10, 11, 12])
    >>> lst1.insert_linked_list(lst2, 4)
    >>> str(lst1)
    ’[0 -> 1 -> 2 -> 3 -> 10 -> 11 -> 12 -> 4 -> 5]’
    >>> lst3 = LinkedList([99])
    >>> lst1.insert_linked_list(lst3, 0)
    >>> str(lst1)
    ’[99 -> 0 -> 1 -> 2 -> 3 -> 10 -> 11 -> 12 -> 4 -> 5]’
    """
    last = other._first
    if pos == 0:
        last.next = self._first
        self._first = other._first
    else:
        i = 0
        curr = self._first
        while curr is not None and i < pos - 1:
            curr = curr.next
            i += 1
        while last.next is not None:
            last = last.next
        last.next = curr.next
        curr.next = other._first


if __name__ == '__main__':
    import doctest
    doctest.testmod()
