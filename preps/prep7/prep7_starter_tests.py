"""CSC148 Prep 7: Recursion

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu and Diane Horton

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 David Liu and Diane Horton

=== Module description ===
This module contains sample tests for Prep 7.

Complete the TODO in this file.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here
"""
from prep7 import num_positives, nested_max, max_length

# TODO: Implement test cases that check the following cases:
#       - max_length on an int
#       - max_length on an empty list
#       - max_length on a nested list containing only integers
#         (i.e. there are no lists inside of the initial list.)


def test_max_length_int() -> None:
    """Tests max_length on an int."""
    assert max_length(3) == 0


def test_max_length_empty() -> None:
    """Tests max_length on an empty list."""
    assert max_length([]) == 0


def test_max_length_nested() -> None:
    """Tests max_length on a nested list containing only integers."""
    assert max_length([1, 2, 3, 4, 5]) == 5

# Below are provided sample test cases for your use. You are encouraged
# to add additional test cases (in addition to the ones required above.)
# WARNING: THIS IS AN EXTREMELY INCOMPLETE SET OF TESTS!
# Add your own to practice writing tests and to be confident your code is
# correct.


def test_num_positives_doctest_example() -> None:
    """Test num_positive on one of the given doctest examples."""
    assert num_positives([1, -2, [-10, 2, [3], 4, -5], 4]) == 5


def test_nested_max_doctest_example() -> None:
    """Test nested_max on one of the given doctest examples."""
    assert nested_max([1, 2, [1, 2, [3], 4, 5], 4]) == 5


def test_max_length_doctest_example() -> None:
    """Test nested_max on one of the given doctest examples."""
    assert max_length([1, 2, [1, 2], 4]) == 4


if __name__ == '__main__':
    import pytest
    pytest.main(['prep7_starter_tests.py'])
