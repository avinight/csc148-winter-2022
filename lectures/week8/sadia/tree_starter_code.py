"""Trees

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the code for a general tree implementation.

Here's our template for recursive tree methods:

    def f(self) -> ...:
        if self.is_empty():         # tree is empty
            ...
        elif self._subtrees == []:  # tree is a single value
            ...
        else:                       # tree has at least one subtree
            ...
            for subtree in self._subtrees:
                ... subtree.f() ...
            ...

Remember that these templates are merely a starting point for an outline.
They very often need to be adjusted to the situation!
"""
from __future__ import annotations

from typing import Any, List, Optional, Union
# Tuple may be imported too - just depending on how you implement
#  the average method's helper.


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

    # From the readings.
    def __init__(self, root: Optional[Any], subtrees: List[Tree]) -> None:
        """Initialize a new Tree with the given root value and subtrees.

        If <root> is None, the tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        self._subtrees = subtrees

    # From the readings.
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

    # From the readings.
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

    # From the readings.
    def __str__(self) -> str:
        """Return a string representation of this tree.

        For each node, its item is printed before any of its
        descendants' items. The output is nicely indented.

        You may find this method helpful for debugging.
        """
        # This commented-out version has the problem that it doesn't
        # distinguish between different levels in the tree; it just prints out
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

    # From the readings.
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

    # Lecture example.
    def preorder(self) -> str:
        """Return a string containing the items of this tree
        in preorder order.

        >>> t = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> t.preorder()
        '1 2 3'
        >>> t2 = Tree(-1, [Tree(0, []), t])
        >>> t2.preorder()
        '-1 0 1 2 3'
        """
        if self.is_empty():
            return ''
        else:
            s = str(self._root)
            for subtree in self._subtrees:
                s += ' ' + subtree.preorder()
            return s

    # Worksheet question.
    def leaves(self) -> List:
        """Return a list of all of the leaf items in the tree.

        >>> Tree(None, []).leaves()
        []
        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> t.leaves()
        [2, 5]
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.leaves()
        [4, 5, 6, 7]
        """
        # TODO implement me

    # Worksheet question.
    def average(self) -> float:
        """Return the average of all the values in this tree.

        Return 0.0 if this tree is empty.

        Precondition: this is a tree of numbers.

        >>> Tree(None, []).average()
        0.0
        >>> t = Tree(13, [Tree(2, []), Tree(6, [])])
        >>> t.average()
        7.0
        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.average()
        5.5
        """
        # TODO implement me (hint: define a recursive helper method)

    def __eq__(self, other: Tree) -> bool:
        """Return whether <self> and <other> are equal.
        """
        if self.is_empty() and other.is_empty():
            return True
        elif self.is_empty() or other.is_empty():
            return False
        else:
            if self._root != other._root:
                return False

            if len(self._subtrees) != len(other._subtrees):
                return False

            return self._subtrees == other._subtrees

    # Worksheet question.
    def to_nested_list(self) -> list:
        """Return the nested list representation of this tree.
        """
        # TODO implement me

    # From the prep summative.
    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this tree.

        >>> t = Tree(1, [Tree(2, []), Tree(5, [])])
        >>> 1 in t  # Same as t.__contains__(1)
        True
        >>> 5 in t
        True
        >>> 4 in t
        False
        """
        if self.is_empty():
            return False

        # item may in root, or subtrees
        if self._root == item:
            return True
        else:
            for subtree in self._subtrees:
                if item in subtree:
                    return True
            return False

    # -------------------------------------------------------------------------
    # Mutating methods
    # -------------------------------------------------------------------------

    # Worksheet question.
    def delete_item(self, item: Any) -> bool:
        """Delete *one* occurrence of the given item from this tree.

        Return True if <item> was deleted, and False otherwise.
        Do not modify this tree if it does not contain <item>.

        Note: See the slides for the start of this code,
        the worksheet implements the _delete_item helper (two ways - so you can
        implement both and just comment one of them out)
        """
        # TODO implement me


# Worksheet question
def to_tree(obj: Union[int, list]) -> Optional[Tree]:
    """Return the Tree which <obj> represents.

    Return None if <obj> is not a valid representation of a tree.

    You may not access Tree attributes directly, since they're private.
    This function can be implemented only using the Tree initializer.

    Hint: Don't call the initializer until you have all of a tree's subtrees!
    """
    # TODO implement me


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={'extra-imports': ['random'],
                                'disable': ['E1136'],
                                'pyta-reporter': 'ColorReporter'})
