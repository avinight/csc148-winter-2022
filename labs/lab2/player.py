from typing import List


class Player:
    """A player.

    === Attributes ===
    name: the player's name
    history: the player's history of the past 100 games

    === Representation Invariants ===
    - len(self.history) <= 100

    === Sample Usage ===
    >>> new_player = Player("Abby")
    >>> new_player.add_score(3)
    >>> new_player.add_score(6)
    >>> new_player.add_score(3)
    >>> new_player.add_score(4)
    >>> new_player.add_score(5)
    >>> new_player.history
    [3, 6, 3, 4, 5]
    >>> new_player.avg_score(3)
    4.0
    >>> new_player.top_score()
    6
    """
    # Attribute types
    name: str
    history: List[int]

    def __init__(self, name: str) -> None:
        """Initialize this player's attributes."""
        self.name = name
        self.history = []

    def add_score(self, score: int) -> None:
        """Add a new score to this player's history.

        >>> new_player = Player("John")
        >>> new_player.add_score(3)
        >>> new_player.history
        [3]
        """
        if len(self.history) == 100:
            self.history.pop(0)
            self.history.append(score)
        else:
            self.history.append(score)

    def avg_score(self, n: int) -> float:
        """Return the average score of this player's most recent n games.

        >>> new_player = Player("Wendy")
        >>> new_player.add_score(3)
        >>> new_player.add_score(4)
        >>> new_player.add_score(5)
        >>> new_player.avg_score(3)
        4.0
        """
        s = 0
        for i in range(0, n):
            s += self.history[len(self.history) - 1 - i]
        return s / n

    def top_score(self) -> int:
        """Return this player's top score.

        >>> new_player = Player("Bryan")
        >>> new_player.add_score(0)
        >>> new_player.add_score(1)
        >>> new_player.add_score(29)
        >>> new_player.add_score(1)
        >>> new_player.top_score()
        29
        """
        max_score = self.history[0]
        for score in self.history:
            if score > max_score:
                max_score = score
        return max_score


if __name__ == '__main__':
    import doctest
    doctest.testmod()
