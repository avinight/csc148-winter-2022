"""Trees

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
Tree code as of Wednesday, March 16.  Today we put method average aside for
the time being (we'll come back to it).  But notice that I've fixed the
method name below as it was used inconsistently -- with and without a
leading underscore.

We moved on to deletion in a general tree.  For delete_item, we:
- analyzed the cases
- realized that the case where the root is the item we want to delete
  is tricky, and decided to make a helper method that takes care of it.
- designed a helper method called _delete_root that would solve the problem.
- implemented both delete_item and _delete_root.
We didn't have a doctest example for testing our new methods, but I've added
some now. Review them to be sure you agree that this is the correct behaviour
for our methods, especially _delete_root.  Then run the doctests and check if
our code actually works!

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

import random
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

        >>> t = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> t.preorder()
        '3 4 1'
        """
        if self.is_empty():
            return ''
        else:
            s = ''
            for subtree in self._subtrees:
                s += ' ' + subtree.preorder()
            # By  moving this line here, the method becomes a "post-order"
            # traversal: deal with the root *after* the subtrees.
            s += str(self._root)
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
        if self.is_empty():
            return []
        elif not self._subtrees:
            # Know: self is a Tree.
            return [self._root]
        else:
            # Know: this tree has a root, and the root has
            # at least one child.
            all_my_leaves = []
            for subtree in self._subtrees:
                all_my_leaves.extend(subtree.leaves())
            return all_my_leaves

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
        if self.is_empty():
            return 0.0
        else:
            total, count = self._average_helper()
            return total / count

    def _average_helper(self) -> Tuple[int, int]:
        """Return a tuple (x, y) where x is the total of the values in this
        tree and y is the size of this tree.

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t._average_helper()
        (55, 10)
        """
        # Cases were worked out "on paper".  We still need to implement this.
        # Try it!  The doctest above will help you check it.
        pass

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
    # def to_nested_list(self) -> list:
    #     """Return the nested list representation of this tree.
    #     """
    #     if self.is_empty():
    #         return []
    #     else:
    #         s = [self._root]
    #         for subtree in self._subtrees:
    #             s.append(subtree.to_nested_list())
    #         return s

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

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t.delete_item(99)
        False
        >>> t.delete_item(6)
        True
        >>> 6 in t
        False
        >>> t.delete_item(1)
        True
        >>> 1 in t
        False
        >>> 3 in t
        True
        """
        if self.is_empty():
            return False
        elif self._root == item:
            # Can this handle case C, where there's one node that is the item?
            # Let's remember to think this through after we have the
            # _delete_root helper method written.
            # We must respect the precondition for _delete_root: the tree must
            # not be empty. But we know it's not because the first if-condition
            # failed above. Phew!
            self._delete_root()
            # Know: _delete_root must have succeeded because self._root == item
            # was true.
            return True
        else:
            # Know: tree is not empty and the root is not the item we want to
            # delete.
            for subtree in self._subtrees:
                successful = subtree.delete_item(item)
                if successful:
                    return True
            return False

    def _delete_root(self) -> None:
        """Delete the root item of this tree.

        Precondition: this tree is not empty.

        >>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
        >>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, []), Tree(9, []),\
                          Tree(10, [])])
        >>> t = Tree(1, [lt, rt])
        >>> t._delete_root()
        >>> t._root == 3
        True
        >>> t._subtrees[0]._root == 2
        True
        >>> t._subtrees[1]._root == 6
        True
        >>> len(t._subtrees) == 6
        True
        """
        if not self._subtrees:
            self._root = None
        else:
            # Know: this tree is not empty, and in fact the root has at least
            # one child.
            # Strategy: chose the last subtree of the root, and promote it's
            # root to be the overall tree root.  Hang its children off this
            # root.
            chosen_subtree = self._subtrees.pop()
            self._root = chosen_subtree._root
            self._subtrees.extend(chosen_subtree._subtrees)



# Worksheet question
# def to_tree(obj: Union[int, list]) -> Optional[Tree]:
#     """Return the Tree which <obj> represents.
#
#     Return None if <obj> is not a valid representation of a tree.
#
#     You may not access Tree attributes directly, since they're private.
#     This function can be implemented only using the Tree initializer.
#     """


# Benefit of representing an empty tree as an instance of Tree:
def do_something(t: Tree) -> None:
    # This would break if t could be None.
    # To prevent that, we'd need a "guard" -- an if-statement.
    # But since we can never have t be None -- instead an empty
    # tree is an instance of Tree! -- we don't need a guard.
    t.treeMethod()


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={'extra-imports': ['random']})
