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


def test_place_character_and_at() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 0, 0, False)
    p = Player(b, 0, 0)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0)[0] == g


def test_place_character_and_at_v1() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 0, 0, False)
    r = Raccoon(b, 0, 0)
    assert len(b.at(0, 0)) == 2
    assert b.at(0, 0) == [g, r]


def test_place_character_and_at_v2() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 0, 0, False)
    r = SmartRaccoon(b, 0, 0)
    assert len(b.at(0, 0)) == 2
    assert b.at(0, 0) == [g, r]


def test_place_character_and_at_v3() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 0, 0, True)
    r = Raccoon(b, 0, 0)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [g]


def test_place_character_and_at_v4() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 0, 0, True)
    rb = RecyclingBin(b, 0, 0)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [g]


def test_place_character_and_at_v5() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 0, 0, False)
    r = SmartRaccoon(b, 0, 0)
    r2 = Raccoon(b, 0, 0)
    assert len(b.at(0, 0)) == 2
    assert b.at(0, 0) == [g, r]
    assert (r2 in b.at(0, 0)) is False


def test_place_character_and_at_v6() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 0, 0, False)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [r]


def test_place_character_and_at_v7() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 0, 0, False)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [r]


def test_place_character_and_at_v8() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    assert b.at(0, 0) == []


def test_place_character_and_at_v9() -> None:
    b = GameBoard(2, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 1, 1, False)
    rb = RecyclingBin(b, 1, 0)
    p = Player(b, 0, 1)
    r2 = Raccoon(b, 0, 0)
    r3 = Raccoon(b, 0, 1)
    r4 = Raccoon(b, 1, 0)
    r5 = SmartRaccoon(b, 1, 1)
    assert len(b.at(0, 0)) == 1
    assert len(b.at(1, 1)) == 2
    assert len(b.at(0, 1)) == 1
    assert len(b.at(1, 0)) == 1
    assert b.at(0, 0) == [r]
    assert b.at(1, 1) == [g, r5]
    assert b.at(1, 0) == [rb]
    assert b.at(0, 1) == [p]


def test_place_character_and_at_v10() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 0, 0, False)
    r2 = Raccoon(b, 0, 0)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [r]


def test_place_character_and_at_v11() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g = GarbageCan(b, 5, 0, True)
    r = SmartRaccoon(b, 0, 0)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [r]


def test_place_character_and_at_v12() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 5, 5)
    assert len(b.at(5, 5)) == 0
    assert b.at(0, 0) == []


def test_place_character_and_at_v13() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g0 = GarbageCan(b, 0, 0, False)
    g = GarbageCan(b, 0, 0, False)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [g0]


def test_place_character_and_at_v14() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    g0 = GarbageCan(b, 0, 0, True)
    g = GarbageCan(b, 0, 0, False)
    assert len(b.at(0, 0)) == 1
    assert b.at(0, 0) == [g0]


def test_to_grid() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    assert grid == [['-', '-', '-'], ['-', '-', '-']]
    g = GarbageCan(b, 0, 0, False)
    grid = b.to_grid()
    assert grid == [['O', '-', '-'], ['-', '-', '-']]
    r = SmartRaccoon(b, 0, 0)
    r2 = Raccoon(b, 0, 0)
    grid = b.to_grid()
    assert grid == [['@', '-', '-'], ['-', '-', '-']]


def test_to_grid_v1() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    assert grid == [['-', '-', '-'], ['-', '-', '-']]
    g = GarbageCan(b, 0, 0, True)
    grid = b.to_grid()
    assert grid == [['C', '-', '-'], ['-', '-', '-']]
    r = SmartRaccoon(b, 0, 0)
    r2 = Raccoon(b, 0, 0)
    grid = b.to_grid()
    assert grid == [['C', '-', '-'], ['-', '-', '-']]


def test_to_grid_v2() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 0, 0, False)
    grid = b.to_grid()
    assert grid == [['S', '-', '-'], ['-', '-', '-']]


def test_to_grid_v3() -> None:
    b = GameBoard(3, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 1)
    g = GarbageCan(b, 0, 0, False)
    grid = b.to_grid()
    assert grid == [['O', '-', '-'], ['S', '-', '-']]


def test_to_grid_v4() -> None:
    b = GameBoard(3, 2)
    rb = RecyclingBin(b, 0, 1)
    g = Player(b, 0, 1)
    grid = b.to_grid()
    assert grid == [['-', '-', '-'], ['B', '-', '-']]


def test_to_grid_v5() -> None:
    b = GameBoard(2, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 1, 1, False)
    rb = RecyclingBin(b, 1, 0)
    p = Player(b, 0, 1)
    assert b.to_grid() == [['S', 'B'], ['P', 'O']]
    r2 = Raccoon(b, 0, 0)
    r3 = Raccoon(b, 0, 1)
    r4 = Raccoon(b, 1, 0)
    r5 = SmartRaccoon(b, 1, 1)
    assert b.to_grid() == [['S', 'B'], ['P', '@']]


def test_str() -> None:
    b = GameBoard(2, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 1, 1, False)
    rb = RecyclingBin(b, 1, 0)
    p = Player(b, 0, 1)
    assert str(b) == 'SB\nPO'
    r2 = Raccoon(b, 0, 0)
    r3 = Raccoon(b, 0, 1)
    r4 = Raccoon(b, 1, 0)
    r5 = SmartRaccoon(b, 1, 1)
    assert str(b) == 'SB\nP@'


def test_str_v1() -> None:
    b = GameBoard(2, 2)
    grid = b.to_grid()
    r = SmartRaccoon(b, 0, 0)
    g = GarbageCan(b, 1, 1, True)
    rb = RecyclingBin(b, 1, 0)
    p = Player(b, 0, 1)
    r2 = Raccoon(b, 0, 0)
    r3 = Raccoon(b, 0, 1)
    r4 = Raccoon(b, 1, 0)
    r5 = SmartRaccoon(b, 1, 1)
    assert str(b) == 'SB\nPC'


def test_move_rb() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 1, 0)
    rb2 = RecyclingBin(b, 2, 0)
    assert rb2.move(LEFT) is True
    assert b.at(2, 0) == []
    assert b.at(1, 0) == [rb2]
    assert b.at(0, 0) == [rb1]


def test_move_rb_v1() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 2, 0)
    rb2 = RecyclingBin(b, 3, 0)
    assert rb1.move(RIGHT) is False
    assert b.at(2, 0) == [rb1]
    assert b.at(3, 0) == [rb2]
    assert rb2.move(RIGHT) is False
    assert b.at(2, 0) == [rb1]
    assert b.at(3, 0) == [rb2]


def test_move_rb_v2() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 0, 1)
    rb3 = RecyclingBin(b, 0, 2)
    assert rb1.move(DOWN) is False
    assert rb2.move(DOWN) is False
    assert rb3.move(DOWN) is False
    assert b.at(0, 0) == [rb1]
    assert b.at(0, 1) == [rb2]
    assert b.at(0, 2) == [rb3]


def test_move_rb_v3() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 0, 0)
    assert rb1.move(RIGHT) is True
    assert rb1.move(RIGHT) is True
    assert rb1.move(RIGHT) is True
    assert b.at(3, 0) == [rb1]
    assert b.at(0, 0) == []


def test_move_rb_v4() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 1, 0)
    assert rb1.move(LEFT) is False
    assert rb1.move(RIGHT) is True
    assert b.at(2, 0) == [rb2]
    assert b.at(1, 0) == [rb1]
    assert b.at(0, 0) == []
    assert rb1.move(RIGHT) is True
    assert b.at(3, 0) == [rb2]
    assert b.at(2, 0) == [rb1]
    assert b.at(1, 0) == []


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


def test_move_rb_v6() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 0, 1)
    grid = b.to_grid()
    assert rb1.move(DOWN) is True
    assert rb2.move(DOWN) is False
    grid_after = b.to_grid()
    assert grid != grid_after
    assert b.at(0, 0) == []
    assert b.at(0, 1) == [rb1]
    assert b.at(0, 2) == [rb2]


def test_move_rb_v7() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 0, 0)
    rb2 = RecyclingBin(b, 0, 1)
    rb3 = RecyclingBin(b, 0, 2)
    grid = b.to_grid()
    assert rb1.move(DOWN) is False
    assert rb2.move(DOWN) is False
    assert rb3.move(DOWN) is False
    grid_after = b.to_grid()
    assert grid == grid_after
    assert b.at(0, 0) == [rb1]
    assert b.at(0, 1) == [rb2]
    assert b.at(0, 2) == [rb3]


def test_move_rb_v8() -> None:
    b = GameBoard(4, 3)
    rb1 = RecyclingBin(b, 1, 0)
    p = Player(b, 0, 0)
    s = SmartRaccoon(b, 1, 1)
    gb = GarbageCan(b, 2, 0, False)
    grid = b.to_grid()
    assert rb1.move(LEFT) is False
    assert rb1.move(RIGHT) is False
    assert rb1.move(UP) is False
    assert rb1.move(DOWN) is False
    grid_after = b.to_grid()
    assert grid == grid_after


def test_move_p() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    gb = GarbageCan(b, 0, 1, True)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(UP) is False
    grid_after = b.to_grid()
    assert grid == grid_after
    assert p.move(DOWN) is False
    assert p.move(RIGHT) is True
    grid_after_2 = b.to_grid()
    assert grid != grid_after_2
    assert b.at(0, 0) == []
    assert b.at(1, 0) == [p]
    assert b.at(0, 1) == [gb]


def test_move_p_v1() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    gb = GarbageCan(b, 0, 1, False)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(UP) is False
    assert p.move(DOWN) is True
    assert p.move(RIGHT) is True
    grid_after_2 = b.to_grid()
    assert grid != grid_after_2
    assert b.at(0, 0) == []
    assert b.at(1, 0) == [p]
    assert b.at(0, 1) == [gb]


def test_move_p_v2() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    o1 = GarbageCan(b, 1, 0, False)
    o2 = GarbageCan(b, 2, 0, False)
    o3 = GarbageCan(b, 3, 0, False)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(UP) is False
    assert p.move(RIGHT) is True
    grid_after = b.to_grid()
    assert grid != grid_after
    assert b.at(0, 0) == [p]
    assert b.at(1, 0) == [o1]


def test_move_p_v3() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    o1 = GarbageCan(b, 1, 0, True)
    o2 = GarbageCan(b, 2, 0, False)
    o3 = GarbageCan(b, 3, 0, False)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(UP) is False
    assert p.move(RIGHT) is False
    grid_after = b.to_grid()
    assert grid == grid_after


def test_move_p_v4() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    rb = RecyclingBin(b, 0, 1)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(UP) is False
    assert p.move(DOWN) is True
    grid_after = b.to_grid()
    assert grid != grid_after
    assert b.at(0, 0) == []
    assert b.at(0, 1) == [p]
    assert b.at(0, 2) == [rb]


def test_move_p_v5() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 1, 0)
    rb1 = RecyclingBin(b, 1, 0)
    r = Raccoon(b, 1, 1)
    s = SmartRaccoon(b, 0, 0)
    gb = GarbageCan(b, 2, 0, True)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(RIGHT) is False
    assert p.move(UP) is False
    assert p.move(DOWN) is False
    grid_after = b.to_grid()
    assert grid == grid_after


def test_move_p_v6() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 1, 0)
    rb1 = RecyclingBin(b, 1, 0)
    r = Raccoon(b, 1, 1)
    s = SmartRaccoon(b, 0, 0)
    gb = GarbageCan(b, 2, 0, False)
    grid = b.to_grid()
    assert p.move(LEFT) is False
    assert p.move(RIGHT) is True
    assert p.move(UP) is False
    assert p.move(DOWN) is False
    assert b.at(2, 0) == [gb]


def test_move_p_v7() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    rb1 = RecyclingBin(b, 1, 0)
    rb2 = RecyclingBin(b, 2, 0)
    assert p.move(RIGHT) is True
    assert p.move(RIGHT) is False
    assert b.at(2, 0) == [rb1]
    assert b.at(3, 0) == [rb2]


def test_move_p_v8() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    rb1 = RecyclingBin(b, 1, 0)
    rb2 = RecyclingBin(b, 2, 0)
    rb3 = RecyclingBin(b, 3, 0)
    grid = b.to_grid()
    assert p.move(RIGHT) is False
    grid_after = b.to_grid()
    assert grid == grid_after


def test_move_p_v9() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    o1 = GarbageCan(b, 1, 0, False)
    rb2 = RecyclingBin(b, 2, 0)
    rb3 = RecyclingBin(b, 3, 0)
    grid = b.to_grid()
    assert p.move(RIGHT) is True
    grid_after = b.to_grid()
    assert grid != grid_after


def test_move_p_v10() -> None:
    b = GameBoard(4, 3)
    p = Player(b, 0, 0)
    o1 = GarbageCan(b, 1, 0, False)
    rb2 = RecyclingBin(b, 2, 0)
    rb3 = RecyclingBin(b, 3, 0)
    grid = b.to_grid()
    assert p.move(DOWN) is True
    grid_after = b.to_grid()
    assert grid != grid_after


def test_check_trapped() -> None:
    b = GameBoard(2, 2)
    s = SmartRaccoon(b, 0, 0)
    r2 = Raccoon(b, 0, 0)
    r5 = SmartRaccoon(b, 1, 1)
    assert s.check_trapped() is False


def test_check_trapped_v1() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 1, 1)
    r2 = Raccoon(b, 2, 1)
    p = Player(b, 1, 0)
    rb = RecyclingBin(b, 0, 1)
    c = GarbageCan(b, 1, 2, True)
    assert s.check_trapped() is False


def test_check_trapped_v2() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 1, 1)
    r2 = Raccoon(b, 2, 1)
    p = Player(b, 1, 0)
    rb = RecyclingBin(b, 0, 1)
    c = GarbageCan(b, 1, 2, False)
    assert s.check_trapped() is False


def test_check_trapped_v3() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 1, 1)
    p = Player(b, 1, 0)
    r2 = Raccoon(b, 2, 1)
    rb = RecyclingBin(b, 0, 1)
    c = GarbageCan(b, 1, 2, False)
    r3 = Raccoon(b, 1, 2)
    assert s.check_trapped() is True


def test_check_trapped_v4() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 0, 0)
    p = Player(b, 1, 0)
    r2 = Raccoon(b, 0, 1)
    c = GarbageCan(b, 1, 2, False)
    assert r.check_trapped() is True


def test_check_trapped_v5() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 0, 0)
    g1 = GarbageCan(b, 1, 0, True)
    r1 = Raccoon(b, 1, 0)
    g2 = GarbageCan(b, 0, 1, True)
    r2 = Raccoon(b, 0, 1)
    assert r.check_trapped() is False


def test_check_trapped_v6() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 0, 0)
    g1 = GarbageCan(b, 1, 0, False)
    r1 = Raccoon(b, 1, 0)
    g2 = GarbageCan(b, 0, 1, False)
    r2 = Raccoon(b, 0, 1)
    assert r.check_trapped() is True


def test_check_trapped_v7() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    g1 = GarbageCan(b, 2, 2, False)
    r1 = Raccoon(b, 2, 2)
    g2 = GarbageCan(b, 3, 1, False)
    r2 = Raccoon(b, 3, 1)
    assert r.check_trapped() is True


def test_check_trapped_v8() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    g1 = GarbageCan(b, 2, 2, True)
    r1 = Raccoon(b, 2, 2)
    g2 = GarbageCan(b, 3, 1, True)
    r2 = Raccoon(b, 3, 1)
    assert r.check_trapped() is False


def test_check_trapped_v9() -> None:
    b = GameBoard(4, 3)
    g1 = GarbageCan(b, 2, 2, False)
    r1 = Raccoon(b, 2, 2)
    assert r1.check_trapped() is False


def test_check_trapped_v10() -> None:
    b = GameBoard(4, 3)
    g1 = GarbageCan(b, 1, 1, False)
    r1 = Raccoon(b, 1, 1)
    r2 = Raccoon(b, 1, 0)
    r3 = Raccoon(b, 0, 1)
    rb = RecyclingBin(b, 2, 1)
    assert r1.check_trapped() is False


def test_rc_move() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    assert s.move(UP) is False
    assert s.move(DOWN) is True
    assert b.at(0, 1) == [s]


def test_rc_move_v1() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    r = Raccoon(b, 1, 0)
    r1 = Raccoon(b, 0, 1)
    assert s.move(UP) is False
    assert s.move(DOWN) is False
    assert s.move(RIGHT) is False
    assert b.at(1, 0) == [r]
    assert r.move(RIGHT) is True
    assert b.at(1, 0) == []
    assert b.at(2, 0) == [r]


def test_rc_move_v2() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 3, 0)
    c = GarbageCan(b, 2, 0, True)
    o = GarbageCan(b, 3, 1, False)
    assert s.move(UP) is False
    assert s.move(RIGHT) is False
    assert s.move(LEFT) is True
    assert b.at(3, 0) == [s]
    assert b.at(2, 0) == [c]
    assert c.locked is False
    assert b.at(3, 1) == [o]
    assert s.move(LEFT) is True
    assert b.at(3, 0) == []
    assert b.at(2, 0) == [c, s]


def test_rc_move_v3() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 3, 0)
    c = GarbageCan(b, 2, 0, True)
    o = GarbageCan(b, 3, 1, False)
    assert s.move(DOWN) is True
    assert b.at(3, 1) == [o, s]
    assert b.at(3, 0) == []
    assert o.locked is False


def test_rc_take_turn() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    c = GarbageCan(b, 2, 2, True)
    c2 = GarbageCan(b, 3, 1, True)
    r.take_turn()
    assert (r.x, r.y) == (3, 2)


def test_rc_take_turn_v1() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    c = GarbageCan(b, 2, 2, True)
    c2 = GarbageCan(b, 3, 1, False)
    r.take_turn()
    assert (r.x, r.y) in [(3, 1), (3, 2)]


def test_rc_take_turn_v2() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    rb = RecyclingBin(b, 2, 2)
    rb1 = RecyclingBin(b, 3, 1)
    r.take_turn()
    r.take_turn()
    r.take_turn()
    assert (r.x, r.y) == (3, 2)


def test_rc_take_turn_v3() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    c = GarbageCan(b, 2, 2, True)
    c2 = GarbageCan(b, 3, 1, False)
    r.move(UP)
    r.take_turn()
    r.take_turn()
    assert (r.x, r.y) == (3, 1)


def test_rc_take_turn_v4() -> None:
    b = GameBoard(4, 3)
    r = Raccoon(b, 3, 2)
    c = GarbageCan(b, 2, 2, False)
    c2 = GarbageCan(b, 3, 1, False)
    r2 = Raccoon(b, 2, 2)
    r3 = Raccoon(b, 3, 1)
    r.move(UP)
    r.take_turn()
    r.take_turn()
    assert (r.x, r.y) == (3, 2)


def test_sc_take_turn() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    # c = GarbageCan(b, 2, 2, False)
    # c2 = GarbageCan(b, 3, 1, False)
    # r2 = Raccoon(b, 2, 2)
    # r3 = Raccoon(b, 3, 1)
    s.move(UP)
    s.take_turn()
    assert (s.x, s.y) in [(1, 0), (0, 1)]


def test_sc_take_turn_v1() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    # c = GarbageCan(b, 2, 2, False)
    c2 = GarbageCan(b, 0, 1, False)
    r2 = Raccoon(b, 1, 0)
    r3 = Raccoon(b, 0, 1)
    s.move(UP)
    s.take_turn()
    assert (s.x, s.y) == (0, 0)


def test_sc_take_turn_v2() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    # c = GarbageCan(b, 2, 2, False)
    c2 = GarbageCan(b, 0, 1, False)
    # r2 = Raccoon(b, 1, 0)
    r3 = Raccoon(b, 0, 1)
    s.move(UP)
    s.take_turn()
    assert (s.x, s.y) == (1, 0)


def test_sc_take_turn_v3() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    c = GarbageCan(b, 2, 0, False)
    c2 = GarbageCan(b, 0, 1, False)
    s.move(UP)
    s.take_turn()
    assert (s.x, s.y) == (0, 1)


def test_sc_take_turn_v4() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    gc = GarbageCan(b, 2, 0, False)
    c = GarbageCan(b, 1, 0, True)
    o = GarbageCan(b, 0, 1, False)
    s.move(UP)
    s.take_turn()
    assert b.at(1, 0) == [c]
    assert gc.locked is False
    assert (s.x, s.y) == (0, 0)


def test_sc_take_turn_v5() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    gc = GarbageCan(b, 2, 0, False)
    o1 = GarbageCan(b, 1, 0, False)
    o = GarbageCan(b, 0, 1, False)
    s.move(UP)
    s.take_turn()
    assert b.at(1, 0) == [o1, s]
    assert s.inside_can is True
    assert (s.x, s.y) == (1, 0)
    assert b.at(0, 0) == []


def test_sc_take_turn_v6() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    p = Player(b, 0, 1)
    o = GarbageCan(b, 0, 2, False)
    o = GarbageCan(b, 3, 0, False)
    grid_before = b.to_grid()
    s.move(UP)
    s.take_turn()
    grid_after = b.to_grid()
    assert (s.x, s.y) == (0, 0)
    assert grid_before == grid_after
    p.move(RIGHT)
    s.take_turn()
    assert (s.x, s.y) == (0, 1)
    s.take_turn()
    assert (s.x, s.y) == (0, 2)


def test_sc_take_turn_v7() -> None:
    b = GameBoard(4, 3)
    s = SmartRaccoon(b, 0, 0)
    o = GarbageCan(b, 2, 0, False)
    o1 = GarbageCan(b, 1, 0, False)
    r = Raccoon(b, 1, 0)
    o2 = GarbageCan(b, 0, 1, False)
    s.move(UP)
    s.take_turn()
    assert b.at(1, 0) == [o1, r]
    assert o.locked is False
    assert r.inside_can is True
    assert (s.x, s.y) == (0, 1)


def test_sc_take_turn_v8() -> None:
    b = GameBoard(5, 4)
    s = SmartRaccoon(b, 2, 2)
    o = GarbageCan(b, 4, 2, False)
    p = Player(b, 2, 1)
    c = GarbageCan(b, 2, 0, True)
    s.move(UP)
    s.take_turn()
    assert (s.x, s.y) == (2, 2)


def test_sc_take_turn_v9() -> None:
    b = GameBoard(2, 2)
    s = SmartRaccoon(b, 0, 0)
    p = Player(b, 1, 0)
    s.move(UP)
    s.take_turn()
    assert (s.x, s.y) == (0, 1)


def test_abs() -> None:
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
    assert b.adjacent_bin_score() == 5


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


def test_abs_v3() -> None:
    b = GameBoard(5, 4)
    rb1 = RecyclingBin(b, 0, 1)
    rb2 = RecyclingBin(b, 2, 1)
    rb3 = RecyclingBin(b, 3, 1)
    rb4 = RecyclingBin(b, 2, 0)
    rb6 = RecyclingBin(b, 1, 3)
    rb7 = RecyclingBin(b, 2, 3)
    rb8 = RecyclingBin(b, 3, 3)
    rb9 = RecyclingBin(b, 4, 3)
    assert b.adjacent_bin_score() == 4


def test_abs_v4() -> None:
    b = GameBoard(5, 4)
    rb1 = RecyclingBin(b, 0, 1)
    rb2 = RecyclingBin(b, 1, 2)
    assert b.adjacent_bin_score() == 1


def test_abs_v5() -> None:
    b = GameBoard(5, 4)
    rb1 = RecyclingBin(b, 0, 1)
    rb2 = RecyclingBin(b, 2, 1)
    rb3 = RecyclingBin(b, 3, 1)
    rb4 = RecyclingBin(b, 2, 0)
    rb6 = RecyclingBin(b, 1, 3)
    rb7 = RecyclingBin(b, 2, 3)
    rb8 = RecyclingBin(b, 3, 3)
    rb9 = RecyclingBin(b, 4, 3)
    assert b.adjacent_bin_score() == 4


def test_abs_v6() -> None:
    b = GameBoard(5, 4)
    rb = RecyclingBin(b, 0, 0)
    rb1 = RecyclingBin(b, 0, 1)
    rb2 = RecyclingBin(b, 1, 0)
    rb3 = RecyclingBin(b, 1, 1)
    rb4 = RecyclingBin(b, 1, 2)
    rb6 = RecyclingBin(b, 1, 3)
    rb9 = RecyclingBin(b, 3, 3)
    assert b.adjacent_bin_score() == 6


def test_abs_v7() -> None:
    b = GameBoard(5, 4)
    rb1 = RecyclingBin(b, 2, 1)
    rb2 = RecyclingBin(b, 3, 1)
    rb3 = RecyclingBin(b, 4, 1)
    rb4 = RecyclingBin(b, 1, 2)
    rb10 = RecyclingBin(b, 2, 2)
    rb11 = RecyclingBin(b, 3, 2)
    rb5 = RecyclingBin(b, 4, 2)
    rb6 = RecyclingBin(b, 2, 3)
    assert b.adjacent_bin_score() == 8


def test_adjacent_bin_score_4() -> None:
    b = GameBoard(10, 10)
    _ = RecyclingBin(b, 2, 0)
    _ = RecyclingBin(b, 3, 0)
    _ = RecyclingBin(b, 7, 0)
    _ = RecyclingBin(b, 0, 1)
    _ = RecyclingBin(b, 1, 1)
    _ = RecyclingBin(b, 2, 1)
    _ = RecyclingBin(b, 3, 1)
    _ = RecyclingBin(b, 4, 1)
    _ = RecyclingBin(b, 7, 1)
    _ = RecyclingBin(b, 0, 2)
    _ = RecyclingBin(b, 1, 2)
    _ = RecyclingBin(b, 2, 2)
    _ = RecyclingBin(b, 3, 2)
    _ = RecyclingBin(b, 8, 2)
    _ = RecyclingBin(b, 9, 2)
    _ = RecyclingBin(b, 0, 4)
    _ = RecyclingBin(b, 1, 4)
    _ = RecyclingBin(b, 2, 4)
    _ = RecyclingBin(b, 3, 4)
    _ = RecyclingBin(b, 4, 4)
    _ = RecyclingBin(b, 5, 4)
    _ = RecyclingBin(b, 6, 4)
    _ = RecyclingBin(b, 7, 4)
    _ = RecyclingBin(b, 8, 4)
    _ = RecyclingBin(b, 9, 4)
    _ = RecyclingBin(b, 0, 6)
    _ = RecyclingBin(b, 1, 6)
    _ = RecyclingBin(b, 2, 6)
    _ = RecyclingBin(b, 3, 6)
    _ = RecyclingBin(b, 0, 7)
    _ = RecyclingBin(b, 3, 7)
    _ = RecyclingBin(b, 9, 7)
    _ = RecyclingBin(b, 0, 8)
    _ = RecyclingBin(b, 1, 8)
    _ = RecyclingBin(b, 2, 8)
    _ = RecyclingBin(b, 3, 8)
    _ = RecyclingBin(b, 8, 8)
    _ = RecyclingBin(b, 9, 8)
    _ = RecyclingBin(b, 7, 9)
    _ = RecyclingBin(b, 8, 9)
    _ = RecyclingBin(b, 9, 9)
    assert b.adjacent_bin_score() == 11


# partner's tests
class PartnersTests:
    pass


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

    assert isinstance(gb.at(1, 0)[0], GarbageCan)
    assert isinstance(gb.at(1, 0)[1], SmartRaccoon)


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


def test_abs_v1_j() -> None:
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


def test_abs_v2_j() -> None:
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

