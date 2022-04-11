"""Trees (Code from lecture)

=== CSC148 Winter 2019 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the code for a general tree implementation.
"""
from __future__ import annotations
from typing import Any, List, Optional, Tuple, Union


class Tree:
    """A recursive tree data structure.

    Note the relationship between this class and RecursiveList; the only major
    difference is that _rest has been replaced by _subtrees to handle multiple
    recursive sub-parts.
    """
    # === Private Attributes ===
    # The item stored at this tree's root, or None if the tree is empty.
    _root: Optional[Any]
    # The list of all subtrees of this tree.
    _subtrees: List[Tree]

    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    #   This setting of attributes represents an empty tree.
    #
    #   Note: self._subtrees may be empty when self._root is not None.
    #   This setting of attributes represents a tree consisting of just one
    #   node.
    #
    # - (NEW) self._subtrees does not contain any empty trees.

    def __init__(self, root: Optional[Any], subtrees: List[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():
            return 0
        else:
            size = 1  # count the root
            for subtree in self._subtrees:
                size += subtree.__len__()  # could also do len(subtree) here
            return size

    def count(self, item: Any) -> int:
        """Return the number of occurrences of <item> in this tree.
        >>> t = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> t.count(3)
        1
        >>> t.count(100)
        0
        """
        if self.is_empty():
            return 0
        else:
            num = 0
            if self._root == item:
                num += 1
            for subtree in self._subtrees:
                num += subtree.count(item)
            return num

    def __str__(self) -> str:
        """Return a string representation of this tree.

        For each node, its item is printed before any of its
        descendants' items. The output is nicely indented.

        You may find this method helpful for debugging.
        """
        # First version is commented out. This had the problem that it doesn't
        # distinguish between different levels in the tree, and just prints out
        # every item on a new line.
        # if self.is_empty():
        #     return ''
        # else:
        #     s = f'{self._root}\n'
        #     for subtree in self._subtrees:
        #         s += str(subtree)  # equivalent to subtree.__str__()
        #     return s
        #
        # Instead, we call a recursive helper method.
        return self._str_indented()

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is
                # modified.
                s += subtree._str_indented(depth + 1)
            return s

    def to_nested_list(self) -> List:
        """Return the nested list representation of this tree.

        >>> t = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> t.to_nested_list()
        [3, [4], [1]]
        """
        if self.is_empty():
            return []
        # elif self._subtrees == []: -- redundant, next case covers this
        #    return [self._root]
        else:
            result = [self._root]
            for subtree in self._subtrees:
                result.append(subtree.to_nested_list())
            return result


def to_tree(obj: Union[int, List]) -> Optional[Tree]:
    """Return the Tree which <obj> represents.

    Return None if <obj> is not a valid representation of a tree.

    You may not access Tree attributes directly, since they're private.
    This function can be implemented only using the Tree initializer.

    >>> t = to_tree([3, [4], [1]])
    >>> t.to_nested_list()
    [3, [4], [1]]
    """
    if isinstance(obj, int):
        return None  # Invalid representation
    elif obj == []:
        return Tree(None, [])  # empty tree
    else:
        potential_root = obj[0]

        # 1. Check that <potential_root> is NOT a list.
        if isinstance(potential_root, list):
            return None

        potential_subtrees = obj[1:]
        subtrees = []
        for sublist in potential_subtrees:
            # 2. Check that <sublist> is a valid tree representation.
            subtree = to_tree(sublist)
            if subtree is None:
                return None
            else:
                subtrees.append(subtree)

        # If we've reached here, the nested list IS a valid representation!
        return Tree(potential_root, subtrees)
