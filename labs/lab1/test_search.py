"""CSC148 Lab 1

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5) == 1


def test_search_empty() -> None:
    assert binary_search([], 1) == -1


def test_search_greatest() -> None:
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 40) == 8


def test_search_length_one() -> None:
    assert binary_search([1], 1) == 0


def test_search_near_middle() -> None:
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 15) == 3


def test_search_middle() -> None:
    assert binary_search([1, 2, 3], 2) == 1


if __name__ == '__main__':
    import pytest
    pytest.main(['test_search.py'])
