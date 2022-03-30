"""CSC148 Assignment 1: Sample tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 0.

Warning: This is an extremely incomplete set of tests! Add your own tests
to be confident that your code is correct.

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) University of Toronto
"""
from datetime import date
from io import StringIO
from a1 import *

# A string representing a simple 4 by 4 game board.
# We use this in one of the tests below. You can use it in your own testing, but
# you do not have to.
SIMPLE_BOARD_STRING = 'P-B-\n-BRB\n--BB\n-C--'


def simple_board_setup() -> GameBoard:
    """Set up a simple game board"""
    b = GameBoard(4, 4)
    b.setup_from_grid(SIMPLE_BOARD_STRING)
    return b


def test_simple_place_character() -> None:
    """Test GameBoard.place_character by placing a single Raccoon."""
    b = GameBoard(3, 2)
    r = Raccoon(b, 1, 1)
    assert b.at(1, 1)[0] == r  # requires GameBoard.at be implemented to work


def test_simple_at() -> None:
    """Test GameBoard.at on docstring example"""
    b = GameBoard(3, 2)
    r = Raccoon(b, 1, 1)
    assert b.at(1, 1)[0] == r
    p = Player(b, 0, 1)
    assert b.at(0, 1)[0] == p


def test_simple_str() -> None:
    """Test GameBoard.__str__ for the simple board in SIMPLE_BOARD_STRING."""
    b = simple_board_setup()
    assert str(b) == 'P-B-\n-BRB\n--BB\n-C--'


def test_simple_check_game_end() -> None:
    """Test GameBoard.check_game_end on the docstring example"""
    b = GameBoard(3, 2)
    Raccoon(b, 1, 0)
    Player(b, 0, 0)
    RecyclingBin(b, 1, 1)
    assert b.check_game_end() is None
    assert not b.ended
    RecyclingBin(b, 2, 0)
    score = b.check_game_end()
    assert b.ended
    assert score == 11  # will only pass this last one when done Task 5.


def test_simple_adjacent_bin_score() -> None:
    """Test GameBoard.adjacent_bin_score on the docstring example"""
    b = GameBoard(3, 3)
    RecyclingBin(b, 1, 1)
    RecyclingBin(b, 0, 0)
    RecyclingBin(b, 2, 2)
    assert b.adjacent_bin_score() == 1
    RecyclingBin(b, 2, 1)
    assert b.adjacent_bin_score() == 3
    RecyclingBin(b, 0, 1)
    assert b.adjacent_bin_score() == 5


def test_simple_player_move() -> None:
    """Test Player.move on docstring example."""
    b = GameBoard(4, 2)
    p = Player(b, 0, 0)
    assert not p.move(UP)
    assert p.move(DOWN)
    assert b.at(0, 1) == [p]
    RecyclingBin(b, 1, 1)
    assert p.move(RIGHT)
    assert b.at(1, 1) == [p]


def test_simple_recyclingbin_move() -> None:
    """Test RecyclingBin.move on docstring example."""
    b = GameBoard(4, 2)
    rb = RecyclingBin(b, 0, 0)
    assert not rb.move(UP)
    assert rb.move(DOWN)
    assert b.at(0, 1) == [rb]


def test_simple_raccoon_check_trapped() -> None:
    """Test Raccoon.check_trapped on docstring example."""
    b = GameBoard(3, 3)
    r = Raccoon(b, 2, 1)
    Raccoon(b, 2, 2)
    Player(b, 2, 0)
    assert not r.check_trapped()
    RecyclingBin(b, 1, 1)
    assert r.check_trapped()


def test_simple_raccoon_move() -> None:
    """Test Raccoon.move on docstring example."""
    b = GameBoard(4, 2)
    r = Raccoon(b, 0, 0)
    assert not r.move(UP)
    assert r.move(DOWN)
    assert b.at(0, 1) == [r]
    g = GarbageCan(b, 1, 1, True)
    assert r.move(RIGHT)
    assert (r.x, r.y) == (0, 1)  # Raccoon didn't change its position
    assert not g.locked  # Raccoon unlocked the garbage can!
    assert r.move(RIGHT)
    assert r.inside_can
    assert len(b.at(1, 1)) == 2  # Raccoon and GarbageCan are both at (1, 1)!


def test_simple_raccoon_take_turn() -> None:
    """Test Raccoon.take_turn on docstring example."""
    b = GameBoard(3, 4)
    r1 = Raccoon(b, 0, 0)
    r1.take_turn()
    assert (r1.x, r1.y) in [(0, 1), (1, 0)]
    r2 = Raccoon(b, 2, 1)
    RecyclingBin(b, 2, 0)
    RecyclingBin(b, 1, 1)
    RecyclingBin(b, 2, 2)
    r2.take_turn()  # Raccoon is trapped
    assert (r2.x, r2.y) == (2, 1)


def test_simple_smartraccoon_take_turn() -> None:
    """Test SmartRaccoon.take_turn on docstring example."""
    b = GameBoard(8, 2)
    s = SmartRaccoon(b, 4, 0)
    GarbageCan(b, 3, 1, False)
    GarbageCan(b, 0, 0, False)
    GarbageCan(b, 7, 0, False)
    s.take_turn()
    assert s.x == 5
    s.take_turn()
    assert s.x == 6


def test_simple_give_turns() -> None:
    """Test GameBoard.give_turns on docstring example."""
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    r = Raccoon(b, 1, 1)
    for _ in range(RACCOON_TURN_FREQUENCY - 1):
        b.give_turns()
    assert b.turns == RACCOON_TURN_FREQUENCY - 1
    assert (r.x, r.y) == (1, 1)  # Raccoon hasn't had a turn yet
    assert (p.x, p.y) == (0, 0)  # Player hasn't had any inputs
    p.record_event(RIGHT)
    b.give_turns()
    assert (r.x, r.y) != (1, 1)  # Raccoon has had a turn!
    assert (p.x, p.y) == (1, 0)  # Player moved right!


def test_move_rb_v5() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    rb3 = RecyclingBin(b, 2, 0)
    assert rb3.move(LEFT) is False
    assert rb1.move(RIGHT) is True
    assert b.at(0, 0) == []
    assert b.at(1, 0) == [rb1]
    assert b.at(2, 0) == [rb2]
    assert b.at(3, 0) == [rb3]
    assert rb2.move(RIGHT) is False
    assert rb3.move(RIGHT) is False
    assert b.at(0, 0) == []
    assert b.at(0, 1) == []
    assert b.at(0, 2) == []


# This concludes the test cases which were included in the assignment.
# The remaining test cases are those written by myself.

def test_smart_seek_garbage() -> None:
    """
    Test that smart raccoon will always seek the open garbage can and will end
    its turn inside the open garbage
    """
    gb = GameBoard(3, 3)
    assert gb.ended is False
    assert gb.turns == 0
    assert gb.to_grid() == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    p = Player(gb, 0, 0)
    sr = SmartRaccoon(gb, 2, 0)
    g = GarbageCan(gb, 1, 0, False)
    assert gb.to_grid() == [['P', 'O', 'S'], ['-', '-', '-'], ['-', '-', '-']]

    sr.take_turn()

    assert isinstance(gb.at(1, 0)[0], SmartRaccoon)
    assert isinstance(gb.at(1, 0)[1], GarbageCan)


def test_smart_player_in_way() -> None:
    """
    Test that smart raccoon will seek the garbage can even when the player is
    in the way (even after 100 turns!)
    """
    gb = GameBoard(3, 3)
    assert gb.ended is False
    assert gb.turns == 0
    assert gb.to_grid() == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    p = Player(gb, 1, 0)
    sr = SmartRaccoon(gb, 2, 0)
    g = GarbageCan(gb, 0, 0, False)
    assert gb.to_grid() == [['O', 'P', 'S'], ['-', '-', '-'], ['-', '-', '-']]

    for i in range(100):
        sr.take_turn()

    assert sr.x == 2
    assert sr.y == 0


def test_raccoon_trapped_in_garbage() -> None:
    """
    Test that smart raccoon will seek the garbage can even when the player is
    in the way (even after 100 turns!)
    """
    gb = GameBoard(3, 3)
    assert gb.ended is False
    assert gb.turns == 0
    assert gb.to_grid() == [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    p = Player(gb, 0, 0)
    sr = SmartRaccoon(gb, 2, 0)
    g = GarbageCan(gb, 1, 0, False)
    b1 = RecyclingBin(gb, 1, 1)
    sr.take_turn()
    assert sr.x == 1 and sr.y == 0
    b2 = RecyclingBin(gb, 2, 0)

    assert gb.to_grid() == [['P', '@', 'B'], ['-', 'B', '-'], ['-', '-', '-']]
    assert sr.inside_can is True
    assert sr.check_trapped() is True

    # Score should only be 1 from adjacent bins since raccoon is inside can and
    # not considered as trapped
    assert gb.check_game_end() == 1


def test_bin_score() -> None:
    """
    Test that bin score is calculated correctly given some complex bin clusters.
    """
    gb = GameBoard(8, 6)
    gb.setup_from_grid("RBBBB---\nB--BBB-\nB-----B-\nBBBB--O-\nB--B-B--\nB-O-----")

    # Score should be 19 from 9 adjacent bins and 1 trapped raccoon
    assert gb.check_game_end() == 19


def test_abs_v1() -> None:
    b = GameBoard(5, 4)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    rb3 = RecyclingBin(b, 0, 1)
    rb4 = RecyclingBin(b, 1, 1)
    rb10 = RecyclingBin(b, 1, 2)
    rb5 = RecyclingBin(b, 3, 0)
    rb6 = RecyclingBin(b, 3, 1)
    rb7 = RecyclingBin(b, 3, 2)
    rb8 = RecyclingBin(b, 3, 3)
    rb9 = RecyclingBin(b, 4, 1)
    assert b.adjacent_bin_score() == 5


def test_abs_v2() -> None:
    b = GameBoard(5, 4)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    rb3 = RecyclingBin(b, 0, 1)
    rb4 = RecyclingBin(b, 1, 1)
    rb10 = RecyclingBin(b, 1, 2)
    rb11 = RecyclingBin(b, 2, 0)
    rb5 = RecyclingBin(b, 3, 0)
    rb6 = RecyclingBin(b, 3, 1)
    rb7 = RecyclingBin(b, 3, 2)
    rb8 = RecyclingBin(b, 3, 3)
    rb9 = RecyclingBin(b, 4, 1)
    assert b.adjacent_bin_score() == 11


if __name__ == '__main__':
    import pytest

    pytest.main(['a1_sample_test.py'])
