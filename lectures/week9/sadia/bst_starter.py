"""Binary Search Trees

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the reference implementation for binary search trees.
"""
from __future__ import annotations
from typing import Any, List, Optional, Tuple


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every item, its value is >= all items stored in its left
    subtree, and <= all items stored in its right subtree.
    """
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[Any]
    # The left subtree, or None if the tree is empty.
    _left: Optional[BinarySearchTree]
    # The right subtree, or None if the tree is empty.
    _right: Optional[BinarySearchTree]

    # === Representation Invariants ===
    #  - If self._root is None, then so are self._left and self._right.
    #    This represents an empty BST.
    #  - If self._root is not None, then self._left and self._right
    #    are BinarySearchTrees.
    #  - (BST Property) If self is not empty, then
    #    all items in self._left are <= self._root, and
    #    all items in self._right are >= self._root.

    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty tree.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self) -> bool:
        """Return whether this BST is empty.

        >>> bst = BinarySearchTree(None)
        >>> bst.is_empty()
        True
        >>> bst = BinarySearchTree(10)
        >>> bst.is_empty()
        False
        """
        return self._root is None

    def items(self) -> list:
        """Return the items in this BinarySearchTree in sorted order"""

        if self.is_empty():
            return []
        else:
            return (
                    self._left.items() +
                    [self._root] +
                    self._right.items()
            )

    # -------------------------------------------------------------------------
    # Standard Container methods (search, insert, delete)
    # -------------------------------------------------------------------------
    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.

        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> 3 in bst
        True
        >>> 5 in bst
        True
        >>> 2 in bst
        True
        >>> 4 in bst
        False
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return item in self._left  # or, self._left.__contains__(item)
        else:
            return item in self._right  # or, self._right.__contains__(item)

    # def insert(self, item: Any) -> None:
    #     """Insert <item> into this tree.
    #
    #     Do not change positions of any other values.
    #
    #     >>> bst = BinarySearchTree(10)
    #     >>> bst.insert(3)
    #     >>> bst.insert(20)
    #     >>> bst._root
    #     10
    #     >>> bst._left._root
    #     3
    #     >>> bst._right._root
    #     20
    #     """
    #     pass

    # def delete(self, item: Any) -> None:
    #     """Remove *one* occurrence of <item> from this BST.
    #
    #     Do nothing if <item> is not in the BST.
    #
    #     >>> bst = BinarySearchTree(7)
    #     >>> left = BinarySearchTree(3)
    #     >>> left._left = BinarySearchTree(2)
    #     >>> left._right = BinarySearchTree(5)
    #     >>> right = BinarySearchTree(11)
    #     >>> right._left = BinarySearchTree(9)
    #     >>> right._right = BinarySearchTree(13)
    #     >>> bst._left = left
    #     >>> bst._right = right
    #     >>> bst.items()
    #     [2, 3, 5, 7, 9, 11, 13]
    #     >>> bst.delete(13)
    #     >>> bst.items()
    #     [2, 3, 5, 7, 9, 11]
    #     >>> bst.delete(9)
    #     >>> bst.items()
    #     [2, 3, 5, 7, 11]
    #     >>> bst.delete(2)
    #     >>> bst.items()
    #     [3, 5, 7, 11]
    #     >>> bst.delete(5)
    #     >>> bst.items()
    #     [3, 7, 11]
    #     >>> bst.delete(7)
    #     >>> bst.items()
    #     [3, 11]
    #     """
    #     pass

    # def delete_root(self) -> None:
    #     """Remove the root of this tree.
    #
    #     Precondition: this tree is *non-empty*.
    #     """
    #     pass

    # def extract_max(self) -> Any:
    #     """Remove and return the maximum item stored in this tree.
    #
    #     Precondition: this tree is *non-empty*.
    #     """
    #     pass

    # -------------------------------------------------------------------------
    # Additional BST methods
    # -------------------------------------------------------------------------
    def __str__(self) -> str:
        """Return a string representation of this BST.

        This string uses indentation to show depth.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            answer = depth * '  ' + str(self._root) + '\n'
            answer += self._left._str_indented(depth + 1)
            answer += self._right._str_indented(depth + 1)
            return answer


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all()
