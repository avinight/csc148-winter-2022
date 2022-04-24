from typing import Optional, List, Any


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

    def postorder(self):
        if self.is_empty():
            return []
        elif len(self._subtrees) == 1 and self._subtrees[0].is_empty():
            return [self._root]
        else:
            posord = []
            for subtree in self._subtrees:
                posord += subtree.postorder()
            posord.append(self._root)
            return posord

    def inorder(self):
        if self.is_empty():
            return []
        elif len(self._subtrees) == 1 and self._subtrees[0].is_empty():
            return [self._root]
        else:
            inord = []
            for subtree in self._subtrees[:int(len(self._subtrees) / 2)]:
                inord += subtree.inorder()
            inord.append(self._root)
            for subtree in self._subtrees[int(len(self._subtrees) / 2):]:
                inord += subtree.inorder()
            return inord

    def levelorder(self):
        if self.is_empty():
            return []
        else:
            levord = [self._root]
            for subtree in self._subtrees:
                levord += [subtree._root]
            for subtree in self._subtrees:
                levord += subtree.levelorder()[1:]
            return levord

    def preorder(self):
        if self.is_empty():
            return []
        else:
            preord = [self._root]
            for subtree in self._subtrees:
                preord += subtree.preorder()
            return preord
