"""
We've defined a BST method for you to implement below named closest.
In this method, we've given you a basic sketch of the different scenarios
you'll need to consider.

Your tasks are listed below.
    1. Implement the base case (when the BST is empty).
    2. Implement the case where the item == the root.
    3. Implement the case where item < root.
    4. Implement the case where item > root.

You may not add any additional methods to the BST.
We suggest you draw a BST and walk through an example before implementing this
method. Below is an example:
                         10
                      /     \
                    3        32
                  /  \\      /  \
                2     7   27    81
                               /  \
                             49    99

[Not graded] It may help to think through the following questions:
    - What is the expected result of BST.closest(20)?
    - What is the expected result of BST._left.closest(20)?
    - What is the expected result of BST._right.closest(20)?
    - Can the result of BST._left.closest(20) ever be closer to 20 than the
      root of our BST?

Submit your code on MarkUs and run the automated self-test.
Your grade on the quiz will be based solely on the results of the self-test.
(i.e. if you pass all of the tests, you get full marks on the quiz.)
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

    def closest(self, item: int) -> Optional[int]:
        """Return the value in this BST that is closest to <item>.

        By "closest" we mean the value that minimizes the absolute difference
        between itself and <item>. For example, if a tree contains 90, 100,
        and 115, the value closest to 104 is 100.

        If there is a tie, return the smaller value.
        Return None if this BST is empty.

        Precondition: this BST contains only integers.
        """
        if self.is_empty():
            ...
            return None  # TODO: Fill in the base case. (Task 1)
        elif item == self._root:
            return self._root  # TODO: Fill in the case where we found the item. (Task 2)
        elif item < self._root:
            ...  # TODO: Fill in the case where item < self._root (Task 3)

            # Hint: If item < self._root, are there any values in the right
            #       subtree that could be closer to item than self._root?
            left_closest = self._left.closest(item)
            # Remember to handle the case when calling closest on a subtree
            # that returns None.
            if left_closest is None:
                return self._root

            diff_from_root = abs(self._root - item)
            diff_from_left_closest = abs(left_closest - item)

            if diff_from_root >= diff_from_left_closest:
                return left_closest
            else:
                return self._root
            # Notice that we > is used here instead of >=
            # We can break ties using the assumption that the closest on the
            # left subtree is smaller than self._root
        else:
            ...  # TODO: Fill in the case where item >= self._root (Task 4)

            # Hint: If item > self._root, are there any values in the left
            #       subtree that could be closer to item than self._root?
            right_closest = self._right.closest(item)
            # Remember to handle the case when calling closest on a subtree
            # that returns None
            if right_closest is None:
                return self._root

            diff_from_root = abs(self._root - item)
            diff_from_right_closest = abs(right_closest - item)
            if diff_from_root <= diff_from_right_closest:
                return self._root
            else:
                return right_closest

            # Notice that we >= is used here instead of >
            # We can break ties using the assumption that the closest on the
            # right subtree is greater than self._root

    ############################################################################
    # Below are the other BST methods that are available to you.
    # Do NOT modify these methods.
    ############################################################################
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

    # You should not be using insert, but you may want to use it to test your
    # code.
    def insert(self, item: Any) -> None:
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
            # Make new leaf.
            # Note that self._left and self._right cannot be None when the
            # tree is non-empty! (This is one of our invariants.)
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)
        elif item <= self._root:
            self._left.insert(item)
        else:
            self._right.insert(item)
