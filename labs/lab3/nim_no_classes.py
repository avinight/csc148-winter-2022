"""
CSC148 Lab 3: Nim (with no classes!)

NOTE: You do NOT have to do anything in this file.
      Just run it and play the game!

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a simplified implementation of the number game, Nim,
but without the use of any classes.

The enemy player is computer-controlled and selects moves at random.

The minimum step in this game is 1, the maximum step is 3, and the goal
is 21.
"""
from random import randint

GOAL = 21
MIN_STEP = 1
MAX_STEP = 3

GAME_INSTRUCTIONS = """=== Game rules ===
A count starts at 0. On a player's turn, they add to the count an amount
between a set minimum and a set maximum. The player who brings the count
to a set goal amount is the winner.

In this implementation, you are one of the players, and the other is the
computer, who picks a random number.

The minimum that can be added is 1, and the maximum is 3. The goal is 21.
=== Game start ==="""


def get_player_move(current: int) -> int:
    """Use input() to get the player's move."""
    move = -1
    while move < MIN_STEP or move > MAX_STEP or (current + move > GOAL):
        try:
            move = int(input("Enter a move between 1 and 3: ").strip())
        except:
            # If an error is raised, just re-do this loop
            pass

    return move


def play_nim() -> None:
    """Plays a game of nim from start to end"""
    print(GAME_INSTRUCTIONS)

    current = 0
    turn = 0

    # Repeat this until the game is done
    while current < GOAL:
        # Generate a move depending on whose turn it is.
        # Consider the following questions:
        #    What changes would we have to make if we wanted two human players?
        #    What if we wanted two random players?
        #    If we wanted to use a strategic AI?
        if turn % 2 == 0:
            move = get_player_move(current)
        else:
            move = randint(MIN_STEP, MAX_STEP)

        current += move

        print("The move {} was made.".format(move))
        print("Current value is: {}".format(current))

        # Add to the number of turns
        turn += 1

    # We use the turn number to determine who's playing next (and thus, who
    # played last)
    if turn % 2 == 1:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost!")


if __name__ == '__main__':
    play_nim()
