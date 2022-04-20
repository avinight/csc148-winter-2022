"""Binary Search Trees

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
BST code as of Friday, March 18.  Today we continued work on BST deletion.
(Previously, we had used the worksheet to analyze cases in a 3-column table.)
Using the worksheet, we:
- noted that the delete method returns nothing
- reviewed the cases and decided to use a helper for case B (item to delete is
  at the root), since it is tricky.
- added case D (item is at the root and has no children).
- reviewed the cases and decided we needed A, B, and C to be separate, but
  maybe the helper method can handle B and D.

Then we started turning those ideas into code. We:
- wrote the delete method, assuming that there was a method to delete the root.
- designed the method that deletes the root

Finally, we started designing delete_root via a worksheet. Note that the
worksheet identifies the scenarios that would go in column 1 of a 3-column
table, and expands them out whe subtasks to walk us through the analysis
and start writing pieces of the code. The code is quite subtle in a couple of
ways. For one, we MUST re-use the BST object whose ID is passed in via self.
(Think that through!) And also the assignment statements to update _root, _left
and _right in various nodes of the BST must be thought through carefully. You
will be doing this sort of task a lot in Assignment 2, so use this BST deletion
code to build your skills.

We'll finish the worksheet, and the code, next week.
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

    def delete(self, item: Any) -> None:
        """Remove *one* occurrence of <item> from this BST.

        Do nothing if <item> is not in the BST.

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        >>> bst.delete(13)
        >>> bst.items()
        [2, 3, 5, 7, 9, 11]
        >>> bst.delete(9)
        >>> bst.items()
        [2, 3, 5, 7, 11]
        >>> bst.delete(2)
        >>> bst.items()
        [3, 5, 7, 11]
        >>> bst.delete(5)
        >>> bst.items()
        [3, 7, 11]
        >>> bst.delete(7)
        >>> bst.items()
        [3, 11]
        """
        if self.is_empty():
            # Know: item is not in this tree, obviously! So there is no
            # deleting to do. (And this method doesn't return anything, so we
            # don't even have to return False.
            # Note: We could restructure the code to remove this branch.
            pass
        elif self._root == item:
            # Know: this BST is not empty. Therefore, we satisfy the
            # precondition for delete_root. That method will have to make sure
            # it continues to be satisfied on any recursive calls.
            self.delete_root()
        elif item < self._root:
            self._left.delete(item)
        else:
            # Know: this BST is not empty, and item must be > self._root.
            self._right.delete(item)

    def delete_root(self) -> None:
        """Remove the root of this tree.

        Precondition: this tree is *non-empty*.
        """
        pass

    def extract_max(self) -> Any:
        """Remove and return the maximum item stored in this tree.

        Precondition: this tree is *non-empty*.
        """
        if not (self._right or self._left):
            s = self._root
            self._root = None
            return s
        else:
            return self._right.extract_max()

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

    # You wrote this in Prep9.
    def items(self) -> list:
        """Return all of the items in the BST in sorted order.

        >>> BinarySearchTree(None).items()
        []
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        """
        if self.is_empty():
            return []
        else:
            return self._left.items() + [self._root] + self._right.items()


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    #
    # import python_ta
    # python_ta.check_all()

    # Understanding parallel assignment:
    # We know that we can't swap x and y like this:
    x = 99
    y = 44
    x = y
    y = x   # The problem is that, by now, x has been changed.
    # At this point, both x and y are 44.
    print(f'The naive way did not work. x is {x} and y is {y}')

    # We can solve this by saving x's old value in a variable:
    x = 99
    y = 44
    temp = x   # Hang on to this!
    x = y
    y = temp   # Now y gets the original x value.
    print(f'Using a temp worked. x is {x} and y is {y}')

    # Python offers us "parallel assignment".  It saves things in temp variables
    # as needed behind the scenes.
    x = 99
    y = 44
    x, y = y, x
    print(f'Using parallel assignment worked. x is {x} and y is {y}')

    # We can do this with multiple variables.
    a = 1
    b = 2
    c = 3
    d = 4
    a, b, c, d = b, a, d, c
    print(f'Assigning 4 in parallel we get a = {a}, b = {b}, c = {c}, d = {d}')

    # It's as if we did this:
    a = 1
    b = 2
    c = 3
    d = 4
    temp1 = a
    temp2 = b
    temp3 = c
    temp4 = d
    a = temp2
    b = temp1
    c = temp4
    d = temp3
    print(f'Assigning 4 using temps we get a = {a}, b = {b}, c = {c}, d = {d}')
