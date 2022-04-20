from bst import BinarySearchTree


def test_rotate_left():
    bst = BinarySearchTree(7)
    left = BinarySearchTree(3)
    left._left = BinarySearchTree(2)
    left._right = BinarySearchTree(5)
    right = BinarySearchTree(11)
    right._left = BinarySearchTree(9)
    right._right = BinarySearchTree(13)
    bst._left = left
    bst._right = right
    print(bst)
    bst.rotate_left()
    print(bst)
    bst.rotate_left()
    print(bst)


def test_height():
    bst = BinarySearchTree(7)
    left = BinarySearchTree(3)
    left._left = BinarySearchTree(2)
    left._right = BinarySearchTree(5)
    right = BinarySearchTree(11)
    right._left = BinarySearchTree(9)
    right._right = BinarySearchTree(13)
    bst._left = left
    bst._right = right
    assert bst.height() == 3


if __name__ == '__main__':
    import pytest

    pytest.main(['bst_test.py'])
