from timsort import find_runs3
from random import shuffle


def test_find_runs3() -> None:
    """Test find_runs3 on a list where n // 2 of the indices are reversed
    and the latter n / 2 indices are in ascending order."""
    lst = list(range(32, -1, -1)) + list(range(0, 33))
    runs = find_runs3(lst)
    assert runs == [(0, 64)]


def test_find_runs3_v2() -> None:
    """Test find_runs3 on a random list."""
    lst = list(range(32, -1, -1)) + list(range(0, 33))
    shuffle(lst)
    runs = find_runs3(lst)
    assert runs == [(0, 64)]


if __name__ == '__main__':
    import pytest

    pytest.main(['test_timsort.py'])
