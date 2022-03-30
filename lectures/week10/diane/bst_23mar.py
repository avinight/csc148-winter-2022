"""Binary Search Trees

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
BST code as of Wednesday, March 23.  Today we finished BST deletion.
- we finished designing delete_root via a worksheet.
- we turned that into code, along the way realizing another helper would be
  useful. We wrote delete_root assuming the helper existed, and then we
  "mmde it so" in the usual way: first analyze in a 3-column table, then turn
  into code.
- It worked the first time! I credit this to thinking before we code.

We then went on to analyze the efficiency of BSTs vs Python lists and general
trees.
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
        if self._left.is_empty() and self._right.is_empty():
            # Know: This BST is a leaf. "Deleting" it means turning it into an
            # empty tree.
            self._root = None
            self._left = None
            self._right = None
        elif self._left.is_empty():
            # Know: This BST has one child, on the right.
            # Promote it to be the root of this BST, making sure we re-use the
            # object that currently stores the root -- since other things may
            # refer to that id!
            self._root, self._left, self._right = self._right._root, \
                                                  self._right._left, \
                                                  self._right._right
        elif self._right.is_empty():
            # Know there is one child, on the left.
            self._root, self._left, self._right = self._left._root, \
                                                  self._left._left, \
                                                  self._left._right
        else:
            # Know: This tree is not empty and, in fact, the root has two
            # children. We chose to promote the largest value on the LHS.
            # NB: knowing the root has a left child means we are definitely
            # not calling _extract_max on an empty tree (i.e., we satisfy the
            # precondition). So this initial call is okay; we'll make sure
            # any recursive calls are as well.
            self._root = self._left._extract_max()

    def _extract_max(self) -> Any:
        """Remove and return the maximum item stored in this tree.

        Precondition: this tree is *non-empty*.
        """
        if self._right.is_empty():
            max_item = self._root
            self._root, self._left, self._right = self._left._root, \
                                                  self._left._left, \
                                                  self._left._right
            return max_item
        else:
            # Know: self._right is not an empty tree, so we are not calling
            # _extract_max on an empty tree.
            return self._right._extract_max()

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
