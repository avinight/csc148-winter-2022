from typing import Tuple

GAME_INSTRUCTIONS = \
    "Candyland is a very simple children's game for two players. " \
    "The board has spaces from 0 to 100. On their turn, " \
    "a player advances a certain number of spaces. The first player to reach " \
    "spot 100 wins. We need to keep track of where the players " \
    "are so that we can report on the location of the " \
    "two players whenever needed. " \
    "We also want to be able to find out who the winner is: either one of the" \
    "players, both if it's a tie, or no one if the game isn't over yet."


class Player:
    """A candyland player.

    """
    # Attribute types
    name: str
    position: int

    def __init__(self, name: str) -> None:
        """Initialize this player's attributes."""
        self.name = name
        self.position = 0

    def move(self, move) -> None:
        if min_move < move < max_move
        return move


class Board:
    """A candyland board.

    """
    # Attribute types
    goal: int
    players: Tuple[Player, Player]
    turn = int
    min_step: int
    max_step: int

    def __init__(self, turn: int, min_step: int, max_step: int,
                 players: Tuple[Player, Player]) -> None:
        """Initialize this board's attributes"""
        self.goal = 100
        self.turn = turn
        self.min_step = min_step
        self.max_step = max_step
        self.players = players






