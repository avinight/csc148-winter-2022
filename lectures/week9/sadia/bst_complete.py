"""
BST module as we left it on Wed, Mar 24th.  Today we added the missing method
extract_max, thereby completing the 3-method sequence for BST tree deletion.
Phew! That was quite a bit of work.  The Representation Invariants played a
crucial role throughout.

Today, in particular, we found we could collapse two cases for extract max:
    - scenario (1), where the root is a leaf
    - scenario (2), where the root has no right child
The same code worked in both cases, but this was only because of the fact that
we never have a None for the left or right child unless this is an empty tree.
If a node is a leaf, it must have an empty tree for each child, and if it has
only one child, it has an empty tree for its other child.  These facts all
follow from the RIs.

This was subtle.  Make sure you see why these facts make it possible for the
if-block to handle scenario (1) as well as scenario (2).
"""

from __future__ import annotations
from typing import Optional, Any


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
        elif self._root == item:
            return True
        elif item < self._root:
            return item in self._left # or, self._left.__contains__(item)
        else:
            return item in self._right # or, self._right.__contains__(item)

    def insert(self, item: Any):
        """Insert <item> into this tree.

        Do not change positions of any other values.

        >>> bst = BinarySearchTree(10)
        >>> bst.insert(3)
        >>> bst.insert(20)
        >>> bst._root
        10
        >>> bst._left._root
        3
        >>> bst._right._root
        20
        """
        if self.is_empty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

        elif item <= self._root:
            self._left.insert(item)
        else:
            self._right.insert(item)

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
            pass
        elif self._root == item:
            self.delete_root()
        elif item < self._root:
            self._left.delete(item)
        else:
            self._right.delete(item)

    def delete_root(self):
        """Remove the root of this BST.

        Precondition: this BST is not empty.

        Notes:
        - We only call this when we've found the desired item at the root
          of a BST, so
            - it's obviously not empty (hence the precondition)
            - we don't need to return anything, because the client code is
              already *at* the desired item when it calls us for help.
        - The method does not need to use recursion itself, although it calls
          a helper that must either iterate or recurse.
        """
        if self._left.is_empty() and self._right.is_empty():
            # Know: this BST is a leaf.  Make it an empty tree.
            self._root = None
            # Need to do these steps to satisfy the RIs:
            self._left = None
            self._right = None
        elif self._left.is_empty():
            # Know: the root has one child, on the RHS.
            # We must mutate self rather than reassign it (think about why!).
            # "Promote" the right subtree.
            self._root, self._left, self._right = \
                self._right._root, self._right._left, self._right._right
        elif self._right.is_empty():
            # Know: the root has one child, on the LHS.
            # Again, we must mutate self.
            # "Promote" the left subtree.
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
        else:
            # Know: the root has two children.
            # Find the biggest value that is less than the root (i.e., the
            # biggest value on the LHS).  Delete it from the left subtree and
            # put it at the root to replace the value there that it was our
            # job to delete.
            self._root = self._left._extract_max()

    def _extract_max(self) -> Any:
        """Remove and return the largest value in this BST.

        Precondition: this BST is not empty.
        """
        if self._right.is_empty():
            # Remember the root value before we remove it.
            biggest = self._root
            # Remove that root value.
            # This code works properly even if the left subtree is empty!
            # But only because we represent that with an instance of an empty
            # BST.  If self._left was merely None, so you see what would go
            # wrong?
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
            return biggest
        else:
            # Know: right child is not empty.
            # The max in me is over there!
            return self._right._extract_max()


if __name__ == "__main__":
    print("BST")
