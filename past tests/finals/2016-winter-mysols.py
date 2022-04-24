from __future__ import annotations
from typing import Any, List, Optional, Tuple


class BinarySearchTree:
    _root: int
    _left: Optional[BinarySearchTree]
    _right: Optional[BinarySearchTree]

    def __init__(self, root: Optional[Any]) -> None:
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

    def extract_max(self) -> Any:
        """
        >>> t1 = BinarySearchTree(20)
        >>> t2 = BinarySearchTree(30)
        >>> t3 = BinarySearchTree(40)
        >>> t2._left = t1
        >>> t2._right = t3
        >>> t4 = BinarySearchTree(50)
        >>> t4._left = t2
        >>> t4.extract_max()
        50
        >>> print(t4._root)
        >>> t4._root == 30
        True
        """
        if self._right.is_empty():
            max_item = self._root
            self = self._left
            return max_item
        else:
            return self._right.extract_max()

    def items(self):
        if self.is_empty():
            return None
        elif self._right.is_empty() and self._left.is_empty():
            return [self._root]
        else:
            return [self._root] + [self._right.items()] + [self._left.items()]

    def prune(self, low: int) -> None:
        """
        Remove all values from this BST that are less than <low>
        Precondition: all values in this BST are integers
        >>> root = BinarySearchTree(None)
        >>> for x in [5, 3, 4, 1, 2]:
        ...     root.insert(x)
        >>> root.prune(3)
        >>> assert root.items() == [3, 4, 5]
        >>> me = BinarySearchTree(None)
        >>> for x in [13, 20, 17, 30, 18, 10, 5, 12, 11, 3]:
        ...     me.insert(x)
        >>> me.prune(18)
        >>> assert me.items() == [18, 20, 30]
        """
        if self.is_empty():
            return
        elif self._root < low:
            self._right.prune(low)
            self._root = self._right._root
            self._right = self._right._right
            self._left = self._right._left
        else:
            self._left.prune(low)

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

    def levels(self) -> List[Tuple[int, List]]:
        """Return a list of items in the tree, separated by level.
        @type self: BinarySearchTree
        @rtype: list[(int, list)]
        >>> t = BinarySearchTree(90)
        >>> t.levels()
        [(1, [90])]
        >>> t._left = BinarySearchTree(50)
        >>> t._right = BinarySearchTree(150)
        >>> t._right._right = BinarySearchTree(170)
        >>> t.levels()
        [(1, [90]), (2, [50, 150]), (3, [170])]
        >>> bst = BinarySearchTree(90)
        >>> l = [50, 150, 20, 75, 95, 175, 5, 25, 66, 80, 92, 111, 166, 200]
        >>> for i in l: bst.insert(i)
        >>> print(bst.levels())
        [(1, [90]), (2, [50, 150]), (3, [20, 75, 95, 175]), (4, [5, 25, 66, 80, 92, 111, 166, 200])]
        """
        if self.is_empty():
            return []
        # elif not(self._left or self._right):
        #     return [(1, [self._root])]
        # else:
        #     left_levels = self._left.levels()
        #     right_levels = self._right.levels()
        #     full_levels = []
        #     for level in left_levels:
        #         full_levels.append((level[0] + 1, level[1]))
        #
        #     for i in range(len(right_levels)):
        #         if i < len(left_levels) and right_levels[i][0] == left_levels[i][0]:
        #             full_levels[i][1].extend(right_levels[i][1])
        #         else:
        #             full_levels.append((right_levels[i][0] + 1, right_levels[i][1]))
        #     return [(1, [self._root])] + full_levels
        else:
            answer = [(1, [self._root])]
            new_answer_left = self._left.levels()
            new_answer_right = self._right.levels()

            for i in range(max(len(new_answer_left), len(new_answer_right))):
                vals = []
                if i < len(new_answer_left):
                    vals.extend(new_answer_left[i][1])
                if i < len(new_answer_right):
                    vals.extend(new_answer_right[i][1])
                answer.append((i + 2, vals))
            return answer

# Leetcode sol
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        >>> s = Solution()
        >>> t = TreeNode(90)
        >>> s.levelOrder(t)
        [[90]]
        >>> t.left = TreeNode(50)
        >>> t.right = TreeNode(150)
        >>> t.right.right = TreeNode(170)
        >>> s.levelOrder(t)
        [[90], [50, 150], [170]]
        """
        # Case 1: Empty tree
        if not root:
            return []
        # Case 2: Empty subtrees
        elif not(root.left or root.right):
            return [[root.val]]
        # Case 3: Non-empty subtrees
        else:
            # init recursive calls
            left_levels = self.levelOrder(root.left)
            right_levels = self.levelOrder(root.right)
            full_levels = []

            # loop through left
            for level in left_levels:
                full_levels.append(level)

            # loop through right
            for i in range(len(right_levels)):
                if i < len(left_levels):
                    full_levels[i].extend(right_levels[i])
                else:
                    full_levels.append(right_levels[i])

            # return left + root + right
            return [[root.val]] + full_levels


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_to_x(self, amount):
        # Add <amount> to this x attribute.
        self = A(self.x + amount, self.y)


if __name__ == '__main__':
    my_a = A(10, 20)
    print(my_a.x)
    my_a.add_to_x(13)
    print(my_a.x)

def nested_sum(obj):
    """Return the sum of the numbers in a nested list.
    Note that a nested list is one of two things:
      1. a number
      2. a list of (smaller) nested lists
    @type obj: int | list
    @rtype: int
    >>> nested_sum([4, [1, 2, 3], [10, [20]], 4])
    44
    """
    sum1 = 0
    if isinstance(obj, int):
        sum1 = sum1 + obj
    else:
        for lst_i in obj:
            nested_sum(lst_i)
        return sum1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
