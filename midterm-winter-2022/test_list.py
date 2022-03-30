from typing import List


def test_contains_empty() -> None:
    """Test that this linked list is empty."""
    lst = [1, 2, 3]
    new = [5, 6]
    lst.extend(new)
    for item in new:
        assert item in lst
        print(item)



