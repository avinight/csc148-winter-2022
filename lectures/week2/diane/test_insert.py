"""Testing: a basic example, with a challenge for you!

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a few simple unit tests for insert_after.
The unit tests are implemented by a module called pytest, which is imported
in the main block.  Try running the module to witness that the tests
all pass.

Note that in order to run this file on your own computer,
you need to have followed our CSC148 Software Guide and installed
all of the Python requirements for the course, including pytest.

Challenge: Can you come up with a unit test that my insert_after function
doesn't pass?  Break my code!
"""
from insert import insert_after


def test_insert_after_at_front() -> None:
    """Test insert_after with one occurrence of n1 at the front of lst.
    """
    input_list = [0, 1, 2, 3]
    insert_after(input_list, 0, 99)
    expected = [0, 99, 1, 2, 3]
    assert input_list == expected


def test_insert_after_at_back() -> None:
    """Test insert_after with one occurrence of n1 at the end of lst.
    """
    input_list = [0, 1, 2, 3]
    insert_after(input_list, 3, 99)
    expected = [0, 1, 2, 3, 99]
    assert input_list == expected


def test_insert_after_middle() -> None:
    """Test insert_after with one occurrence of n1 in the middle of lst.
    """
    input_list = [0, 1, 2, 3]
    insert_after(input_list, 1, 99)
    expected = [0, 1, 99, 2, 3]
    assert input_list == expected


def test_insert_after_n1_equals_n2() -> None:
    """Test insert_after when n1 and n2 are the same."""
    input_list = [0, 1, 2, 3, 99]
    insert_after(input_list, 2, 2)
    expected = [0, 1, 2, 2, 3, 99]
    assert input_list == expected


if __name__ == '__main__':
    import pytest
    pytest.main(['test_insert.py'])
