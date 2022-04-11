"""CSC148 Assignment 1: Sample tests

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Assignment 2.

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
# Note that some tests under each Task subheading depend on other methods
# implemented within that task, and previous tasks before it

from society_hierarchy import *


def sample_society0() -> Society:
    """Return a Society of sufficient complexity without District Leaders.
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = Citizen(2, 'Citizen 2', 3002, 'Bank robber', 19)
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = Citizen(7, 'Citizen 7', 3007, 'Builder', 58)
    s.add_citizen(c7, 4)
    return s


def sample_society1() -> Society:
    """Return a Society of sufficient complexity with District leaders.
    """
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = DistrictLeader(7, 'Citizen 7', 3007, 'Builder', 58, 'D7')
    s.add_citizen(c7, 4)
    return s


def sample_society2() -> Society:
    """Return a Society of sufficient complexity with District leaders,
    where the head is also a DistrictLeader.
    """
    s = Society()
    c1 = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "I am the boss")
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 100)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = DistrictLeader(7, 'Citizen 7', 3007, 'Builder', 58, 'D7')
    s.add_citizen(c7, 4)
    return s


def citizen_system() -> Citizen:
    """A system of citizens, without using class Society, of height 4.
    There is one head, 10 children. Each child has 5 children of their own.
    Each of these 5 children has 2 children."""
    c = Citizen(0, "Star", 3000, "Dictator", 100)  # the head
    id_ = 0
    manu = "Star"
    yr = 3000
    job = "worker"
    rating = 100
    cits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(cits)):
        id_ += 1
        yr += 1
        rating -= 1
        cits[i] = Citizen(id_, manu, yr, job, rating)
        c.add_subordinate(cits[i])
    for i in range(len(cits)):
        head = cits[i]
        sub_cits = [1, 2, 3, 4, 5]
        for j in range(len(sub_cits)):
            id_ += 1
            yr += 1
            rating -= 1
            sub_cits[j] = Citizen(id_, manu, yr, job, rating)
            head.add_subordinate(sub_cits[j])
    for i in range(len(cits)):
        head = cits[i]
        sub_cits = head.get_direct_subordinates()
        for j in range(len(sub_cits)):
            sub_head = sub_cits[j]
            kids = [1, 2]
            for k in range(len(kids)):
                id_ += 1
                yr += 1
                rating = id_ // 2
                kids[k] = Citizen(id_, manu, yr, job, rating)
                sub_head.add_subordinate(kids[k])
    return c


def society_from_file_demo() -> Society:
    """Return the Society defined in the provided file citizens.csv.
    """
    return create_society_from_file(open("citizens.csv"))


def promote_citizen_example() -> Society:
    """Return the society used in the handout example of promotion.
    """
    c = DistrictLeader(6, "Star", 3036, "CFO", 20, "Area 52")
    c2 = DistrictLeader(5, "S.T.A.R.R.Y Lab", 3024, "Manager", 50, "Finance")
    c3 = Citizen(7, "Hookins", 3071, "Labourer", 60)
    c4 = Citizen(11, "Starky", 3036, "Repairer", 90)
    c5 = Citizen(13, "STARRY", 3098, "Eng", 86)
    s = Society()
    s.add_citizen(c)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 5)
    s.add_citizen(c4, 7)
    s.add_citizen(c5, 7)
    return s


###########################################################################
# Tests for methods in Task 1.1
###########################################################################


def test_add_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_add_subordinate_v1() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(1, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    assert c.get_direct_subordinates()[0] is c4
    assert c.get_direct_subordinates()[3] is c3
    assert len(c.get_direct_subordinates()) == 4
    assert c4.get_superior() is c


def test_add_subordinate_v2() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    assert c.get_direct_subordinates()[0] is c1
    assert c.get_direct_subordinates()[3] is c4
    assert len(c.get_direct_subordinates()) == 4
    assert c4.get_superior() is c


def test_add_subordinate_v3() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    assert c.get_direct_subordinates()[0] is c1
    assert c.get_direct_subordinates()[3] is c3
    assert c.get_direct_subordinates()[1] is c4
    assert len(c.get_direct_subordinates()) == 4
    assert c4.get_superior() is c


def test_add_subordinate_v4() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c1.add_subordinate(c2)
    c1.add_subordinate(c3)
    c1.add_subordinate(c4)
    c1.add_subordinate(c4)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_direct_subordinates()[0] is c4
    assert c1.get_direct_subordinates()[2] is c3
    assert len(c.get_all_subordinates()) == 4
    assert c4.get_superior() is c1


def test_add_subordinate_v5() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_add_subordinate_v6() -> None:
    c = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "District A")
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_add_subordinate_v7() -> None:
    c = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "District A")
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_add_subordinate_sorting() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(5, 'Citizen 5', 3011, 'Just a Dude', 69)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    assert c.get_direct_subordinates()[0] is c2
    assert c1.get_superior() is c


def test_remove_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_remove_subordinate_v1() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    c.remove_subordinate(5)
    assert len(c.get_direct_subordinates()) == 3
    assert c4.get_superior() is None
    assert c4 not in c.get_direct_subordinates()


def test_remove_subordinate_v2() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(1, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    c.remove_subordinate(1)
    assert c.get_direct_subordinates()[0] is c1
    assert c.get_direct_subordinates()[2] is c3
    assert len(c.get_direct_subordinates()) == 3
    assert c4.get_superior() is None
    assert c3.get_superior() is c


def test_remove_subordinate_v3() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    c.remove_subordinate(10)
    assert c.get_direct_subordinates()[0] is c1
    assert c.get_direct_subordinates()[2] is c3
    assert len(c.get_direct_subordinates()) == 3
    assert c4.get_superior() is None
    assert c1.get_superior() is c


def test_remove_subordinate_v4() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c.add_subordinate(c4)
    c.add_subordinate(c4)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates()[0] is c1
    assert c.get_direct_subordinates()[2] is c3
    assert len(c.get_direct_subordinates()) == 4
    assert c4.get_superior() is c
    assert c1.get_superior() is c


def test_become_subordinate_to() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_to_v1() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c4.become_subordinate_to(c)
    c4.become_subordinate_to(c)
    assert len(c.get_direct_subordinates()) == 4
    assert c4.get_superior() is c
    assert c4 == c.get_direct_subordinates()[1]


def test_become_subordinate_to_v2() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    assert c.get_direct_subordinates() == []
    # c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    # c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    # c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c4.become_subordinate_to(c)
    c4.become_subordinate_to(c)
    assert len(c.get_direct_subordinates()) == 1
    assert c4.get_superior() is c
    assert c4 == c.get_direct_subordinates()[0]
    c.remove_subordinate(5)
    assert c.get_direct_subordinates() == []


def test_become_subordinate_to_v3() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c4.become_subordinate_to(None)
    assert len(c.get_direct_subordinates()) == 3
    assert c4.get_superior() is None
    assert c2 == c.get_direct_subordinates()[1]


def test_become_subordinate_to_v4() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c3)
    c4.become_subordinate_to(None)
    assert len(c.get_direct_subordinates()) == 3
    assert c4.get_superior() is None
    assert c2 == c.get_direct_subordinates()[1]


def test_become_subordinate_to_v5() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c4.add_subordinate(c2)
    c4.add_subordinate(c3)
    assert len(c.get_direct_subordinates()) == 1
    assert len(c4.get_direct_subordinates()) == 2
    assert c4.get_superior() is None
    c4.become_subordinate_to(c)
    assert c.get_direct_subordinates()[1] == c4
    assert len(c.get_direct_subordinates()) == 2
    c4.become_subordinate_to(None)
    assert c.get_direct_subordinates()[0] == c1 and \
           len(c.get_direct_subordinates()) == 1
    assert c4.get_direct_subordinates() == [c2, c3]


def test_become_subordinate_to_v6() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_get_citizen_v1() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c4.add_subordinate(c2)
    c4.add_subordinate(c3)
    c4.become_subordinate_to(c)
    assert c.get_citizen(8) == c3 == c4.get_direct_subordinates()[1]


def test_get_citizen_v2() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c4.add_subordinate(c2)
    c4.add_subordinate(c3)
    c4.become_subordinate_to(c)
    assert c.get_citizen(10) is None


def test_get_citizen_v3() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c4.add_subordinate(c2)
    c4.add_subordinate(c3)
    c4.become_subordinate_to(c1)
    assert c.get_citizen(8) == c3 == c4.get_direct_subordinates()[1]


###########################################################################
# Tests for methods in Task 1.2
###########################################################################

def test_get_all_subordinates() -> None:
    c1 = Citizen(10, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    result = c3.get_all_subordinates()
    assert result == [c2, c1]


def test_get_all_subordinates_v1() -> None:
    c = Citizen(2, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(4, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(6, 'oscorp', 3011, 'babysitter', 20)
    c3 = Citizen(8, 'oscorp', 3011, 'smh', 20)
    c4 = Citizen(5, 'oscorp', 3011, 'a', 20)
    c.add_subordinate(c1)
    c4.add_subordinate(c2)
    c4.add_subordinate(c3)
    c4.become_subordinate_to(c)
    assert c.get_all_subordinates() == [c1, c4, c2, c3]


def test_get_all_subordinates_v2() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    assert c6.get_all_subordinates() == [c2, c3, c5, c7, c8, c9, c10, c11]


def test_get_all_subordinates_v3() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    # c7.become_subordinate_to(c5)
    # c9.become_subordinate_to(c5)
    # c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    # c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    assert c6.get_all_subordinates() == [c2, c3, c10, c11]


def test_get_all_subordinates_v4() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    assert c6.get_all_subordinates() == []


def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    assert head is c3


def test_get_society_head_v1() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    assert c12.get_society_head() is c12


def test_get_society_head_v2() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    assert c12 not in c6.get_all_subordinates()
    assert c10.get_society_head() is c6
    assert c6.get_society_head() is c6


def test_get_closest_common_superior() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c3.get_closest_common_superior(1) == c3


def test_get_closest_common_superior_v1() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    assert c11.get_closest_common_superior(2) is c2
    assert c10.get_closest_common_superior(3) is c6
    assert c5.get_closest_common_superior(3) is c6


def test_get_closest_common_superior_v5() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(5) == c3


def test_get_closest_common_superior_v2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(2) == c2


def test_get_closest_common_superior_v3() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    c2.become_subordinate_to(c4)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(3) == c2


def test_get_closest_common_superior_v4() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    c2.become_subordinate_to(c4)
    c5.become_subordinate_to(c4)
    assert c1.get_closest_common_superior(5) == c4

###########################################################################
# Tests for methods in Task 1.3
###########################################################################


def test_society_get_citizen() -> None:
    s = sample_society0()
    who = s.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


def test_society_get_citizen_v1() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    assert s.get_citizen(10) is None
    s.set_head(c6)
    assert s.get_citizen(10) is c10
    assert s.get_citizen(12) is None


def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_get_all_citizens_v1() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    assert s.get_all_citizens() == []
    s.set_head(c6)
    assert s.get_all_citizens() == [c2, c3, c5, c6, c7, c8, c9, c10, c11]


def test_get_all_citizens_v2() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    assert s.get_all_citizens() == []
    s.set_head(c6)
    assert s.get_all_citizens() == [c2, c3, c5, c6, c7, c8, c9, c10, c11]


def test_get_all_citizens_doctest() -> None:
    """Test the doctest of get_all_citizens."""
    o = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Manager", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 65)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3024, "Manager", 30)
    c5 = Citizen(5, "Hookins National Lab", 3024, "Labourer", 50)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 30)
    o.add_citizen(c4, None)
    o.add_citizen(c2, 4)
    o.add_citizen(c6, 2)
    o.add_citizen(c1, 4)
    o.add_citizen(c3, 1)
    o.add_citizen(c5, 1)
    assert o.get_all_citizens() == [c1, c2, c3, c4, c5, c6]


def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    s.add_citizen(c1, 2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2


def test_soc_add_citizen_v1() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c50 = Citizen(50, 'oscorp', 3011, 'a', 20)
    c60 = Citizen(60, 'oscorp', 3011, 'a', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    assert s.get_head() is c6
    s.add_citizen(c4, 5)
    assert c5.get_direct_subordinates() == [c4, c7, c9]


def test_soc_add_citizen_v2() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'Big boss', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'Watcher', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'a', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'a', 20)
    c50 = Citizen(50, 'oscorp', 3011, 'a', 20)
    c60 = Citizen(60, 'oscorp', 3011, 'a', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    assert s.get_head() is c6
    s.add_citizen(c12)
    assert s.get_head() is c12
    assert c12.get_direct_subordinates() == [c6]


def test_add_citizen_v2() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.add_subordinate(c3)
    s.add_citizen(c1)
    s.add_citizen(c2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2
    assert c2.get_direct_subordinates() == [c1]


def test_add_citizen_v3() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.add_subordinate(c3)
    s.add_citizen(c1)
    s.add_citizen(c2, 1)
    assert s.get_head() == c1
    assert s.get_citizen(1) is c1
    assert c2.get_superior() is c1
    assert c2.get_direct_subordinates() == [c3]
    assert c1.get_direct_subordinates() == [c2]


def test_add_citizen_v4() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c1.add_subordinate(c3)
    s.add_citizen(c2)
    s.add_citizen(c1)
    assert s.get_head() == c1
    assert s.get_citizen(1) is c1
    assert c2.get_superior() is c1
    assert c2.get_direct_subordinates() == []
    assert c1.get_direct_subordinates() == [c2]


def test_add_citizen_superior_with_subs() -> None:
    s = sample_society0()
    c1 = Citizen(69, 'Test', 1994, 'Killer', 100)
    c2 = Citizen(70, 'Test 2', 1994, 'Killers Sub', 100)
    c1.add_subordinate(c2)
    c1.get_direct_subordinates()
    s.add_citizen(c1)
    assert s.get_head() == c1
    assert len(s.get_head().get_direct_subordinates()) == 1
    assert s.get_head().get_direct_subordinates()[0] != c2


def test_get_citizens_with_job() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == [5, 8, 9]


def test_get_citizens_with_job_v1() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'moron', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'moron', 20)
    c50 = Citizen(50, 'oscorp', 3011, 'moron', 20)
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    assert s.get_citizens_with_job('a') == []
    s.add_citizen(c6)
    s.add_citizen(c12, 6)
    assert s.get_citizens_with_job('moron') == [c2, c6, c8, c12, c50, c60]


###########################################################################
# Tests for methods in Task 2.1
###########################################################################

def test_district_leader() -> None:
    d = DistrictLeader(2, "Some Lab", 3024, "Lawyer", 30, "District A")
    assert [d.cid, d.manufacturer, d.model_year, d.job, d.rating] == \
           [2, "Some Lab", 3024, "Lawyer", 30]
    assert d.get_district_name() == 'District A'


def test_get_district_citizens() -> None:
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c1)
    assert c1.get_district_citizens() == [c1, c2, c3]


###########################################################################
# Tests for methods in Task 2.2
###########################################################################


def test_get_district_name() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    result = who.get_district_name()
    assert result == 'D2'


def test_get_district_name_v1() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'moron', 20)
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c6.get_district_name() == 'eng'
    assert c5.get_district_name() == 'eng'
    assert c11.get_district_name() == 'eng'
    assert c50.get_district_name() == 'la mer'
    assert c60.get_district_name() == 'eng'


def test_get_district_name_v2() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'moron', 10)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c6.add_subordinate(c8)
    s = Society()
    s.add_citizen(c6)
    assert c6.get_district_name() == ''
    assert c8.get_district_name() == ''
    c6.remove_subordinate(8)
    c8 = DistrictLeader(8, 'oscorp', 3011, 'moron', 20, 'eng')
    c6.add_subordinate(c8)
    assert c8.get_district_name() == 'eng'


def test_rename_district() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    who.rename_district('D10')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D10'


def test_rename_district_v1() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'watcher', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'lancer', 99)
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c6.get_district_name() == 'eng'
    assert c50.get_district_name() == 'la mer'
    c50.rename_district('la ceil')
    assert c50.get_district_name() == 'la ceil'
    assert c60.get_district_name() == 'eng'
    c60.rename_district('echoplex')
    assert c60.get_district_name() == 'echoplex'
    assert c6.get_district_name() == 'echoplex'


###########################################################################
# Tests for method in Task 2.3
###########################################################################

def test_change_citizen_type() -> None:
    s = sample_society1()
    s.change_citizen_type(6, 'D6')
    who = s.get_citizen(6)
    assert isinstance(who, DistrictLeader)
    assert who.get_district_name() == 'D6'
    assert [c.cid for c in who.get_all_subordinates()] == [8, 9, 10]
    assert who.get_superior().cid == 2


def test_change_citizen_type_v1() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'moron', 20)
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c12.get_district_name() == 'eng' == c60.get_district_name()
    s.change_citizen_type(12, 'la ceil')
    c12 = s.get_citizen(12)
    assert c12.get_district_name() == 'la ceil'
    assert c50.get_district_name() == 'la mer'
    assert c5.get_district_name() == 'eng' == c6.get_district_name()
    s.change_citizen_type(6)
    c6 = c3.get_superior()
    assert c9.get_district_name() == '' == c6.get_district_name()


def test_change_citizen_type_v2() -> None:
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    assert c4.get_district_name() == ''
    s = Society()
    s.add_citizen(c4)
    c4 = s.change_citizen_type(4, 'eng')
    assert c4.get_district_name() == 'eng'


def test_change_citizen_type_v3() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'smh', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    c61 = s.change_citizen_type(6)
    assert s.get_head() == c61 != c6
    assert c61.get_superior() is None
    assert c61.get_direct_subordinates() == [c2, c3, c5, c8]


def test_change_citizen_type_v4() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = DistrictLeader(7, 'Citizen 7', 3007, 'Builder', 58, 'D7')
    s.add_citizen(c7, 4)

    s.change_citizen_type(6, 'D6')
    assert c6.get_superior() is None
    assert c6.get_direct_subordinates() == []

    c6new = s.get_citizen(6)
    assert isinstance(c6new, DistrictLeader)
    assert c6new.get_district_name() == 'D6'
    assert [c.cid for c in c6new.get_all_subordinates()] == [8, 9, 10]
    assert c6new.get_superior().cid == 2
    assert id(c6new) != id(c6)


def test_change_society_head() -> None:
    s = Society()
    c1 = Citizen(1, 'test1', 2022, 'Leader', 69)
    s.add_citizen(c1)
    s.change_citizen_type(1)
    assert s.get_head() is not None
    assert type(s.get_head()) is DistrictLeader


def test_change_type_with_no_superior() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s.change_citizen_type(c1.cid, 'District One')

    c1new = s.get_citizen(1)
    assert c1new.get_superior() is None
    assert c1new.get_direct_subordinates()[0] == c2
    assert type(c1new) is DistrictLeader


def test_change_citizen_dl_with_no_subs() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s.change_citizen_type(c4.cid, 'District One')

    c4new = s.get_citizen(4)
    assert c4new.get_superior() == c2
    assert not c4new.get_direct_subordinates()
    assert type(c4new) is DistrictLeader
    assert c4new.get_district_name() == 'District One'
    assert c4.job == c4new.job
    assert c4.get_superior() is None


def test_change_citizen_dl_with_subs_and_superior() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s.change_citizen_type(c2.cid, 'District One')

    c2new = s.get_citizen(2)
    assert c2new.get_superior() == c1
    assert len(c2new.get_direct_subordinates()) == 2
    assert c2new.get_direct_subordinates() != c2.get_direct_subordinates()
    assert type(c2new) is DistrictLeader
    assert c2new.get_district_name() == 'District One'


def test_swap_up_v0() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'watcher', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'lancer', 99)
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c12.get_superior() == c5
    assert c12.get_all_subordinates() == [c50, c60]
    c12 = s._swap_up(c12)
    assert c12.job == 'watcher'
    assert c12.get_superior() == c6
    assert [c.cid for c in c12.get_all_subordinates()] == [5, 7, 9, 50, 60]
    # assert c12.get_all_subordinates() == [c5, c7, c9, c50, c60]
    assert s._swap_up(c12) == s.get_citizen(12)
    # c12 = s._swap_up(c12)
    assert s.get_head() == s.get_citizen(12)
    c6 = s.get_citizen(6)
    assert [c.cid for c in c6.get_all_subordinates()] == [5, 7, 9, 50, 60]
    # assert c6.get_all_subordinates() == [c5, c7, c9, c50, c60]


def test_swap_up_v1() -> None:
    s = Society()
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 2)
    c3 = s._swap_up(c3)
    assert c3.job == "Lawyer"
    assert isinstance(c3, Citizen)
    assert c3.cid == 3
    assert c3.rating == 55
    assert [c.cid for c in c3.get_all_subordinates()] == [2]


def test_swap_up_v2() -> None:
    s = Society()
    c1 = DistrictLeader(1, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 2)
    c3 = s._swap_up(c3)
    assert c3.job == "Lawyer"
    assert isinstance(c3, Citizen)
    assert c3.cid == 3
    assert c3.rating == 55
    assert [c.cid for c in c3.get_all_subordinates()] == [2, 4]


def test_swap_up_v3() -> None:
    s = Society()
    c1 = DistrictLeader(6, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    c3 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    c4 = Citizen(11, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 6)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 2)
    c2 = s._swap_up(c2)

    assert [c.cid for c in c2.get_all_subordinates()] == [6, 10, 11]


def test_swap_up_sub_and_sup() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    c3 = s._swap_up(c3)
    assert s.get_citizen(2).job == 'Three'
    assert c3.job == 'Two'
    assert len(s.get_citizen(1).get_direct_subordinates()) == 1
    assert len(s.get_citizen(2).get_direct_subordinates()) == 2
    assert s.get_citizen(1).get_direct_subordinates()[0] == c3
    assert s.get_citizen(4) in c3.get_direct_subordinates()
    assert s.get_citizen(4) not in s.get_citizen(2).get_direct_subordinates()
    assert s.get_citizen(5) in s.get_citizen(2).get_direct_subordinates()
    assert s.get_citizen(5)not in c3.get_direct_subordinates()
    assert s.get_citizen(2).get_superior() == c3
    assert c3.get_superior() == s.get_citizen(1)


def test_swap_up_sub_and_sup_dl() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = DistrictLeader(2, 'test2', 2022, 'Two', 92, 'District 2')
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s._swap_up(c3)

    c2 = s.get_citizen(2)
    c3 = s.get_citizen(3)
    assert c2.job == 'Three'
    assert c3.job == 'Two'
    assert isinstance(c2, Citizen)
    assert type(c3) is DistrictLeader
    assert len(c1.get_direct_subordinates()) == 1
    assert len(c2.get_direct_subordinates()) == 2
    assert c1.get_direct_subordinates()[0] == c3
    assert c4 in c3.get_direct_subordinates()
    assert c4 not in c2.get_direct_subordinates()
    assert c5 in c2.get_direct_subordinates()
    assert c5 not in c3.get_direct_subordinates()
    assert c2.get_superior() == c3
    assert c3.get_superior() == c1


def test_swap_up_with_head() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    c2 = s._swap_up(c2)
    assert c2.job == 'One'
    assert s.get_citizen(1).job == 'Two'
    assert len(s.get_citizen(1).get_direct_subordinates()) == 2
    assert s.get_citizen(3) in s.get_citizen(1).get_direct_subordinates()
    assert s.get_citizen(4) in s.get_citizen(1).get_direct_subordinates()
    assert c2 not in s.get_citizen(1).get_direct_subordinates()
    assert s.get_citizen(1) in c2.get_direct_subordinates()
    assert len(c2.get_direct_subordinates()) == 1
    assert s.get_citizen(1).get_superior() == c2
    assert c2.get_superior() is None


def test_swap_up_with_head_dl() -> None:
    c1 = DistrictLeader(1, 'test1', 2021, 'One', 91, 'District 2')
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    s._swap_up(c2)
    c2 = s.get_citizen(2)
    c1 = s.get_citizen(1)
    assert isinstance(c2, DistrictLeader)
    assert type(c1) is Citizen
    assert c2.job == 'One'
    assert c1.job == 'Two'
    assert len(c1.get_direct_subordinates()) == 2
    assert c3 in c1.get_direct_subordinates()
    assert c4 in c1.get_direct_subordinates()
    assert c2 not in c1.get_direct_subordinates()
    assert c1 in c2.get_direct_subordinates()
    assert len(c2.get_direct_subordinates()) == 1
    assert c1.get_superior() == c2
    assert c2.get_superior() is None


def test_swap_up_with_no_sub() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    c5 = s._swap_up(c5)
    assert s.get_citizen(3).job == 'Five'
    assert s.get_citizen(5).job == 'Three'
    assert s.get_citizen(3) not in s.get_citizen(2).get_direct_subordinates()
    assert s.get_citizen(5) not in s.get_citizen(3).get_direct_subordinates()
    assert s.get_citizen(3) in s.get_citizen(5).get_direct_subordinates()
    assert s.get_citizen(6) in s.get_citizen(5).get_direct_subordinates()
    assert len(s.get_citizen(3).get_direct_subordinates()) == 0
    assert len(s.get_citizen(5).get_direct_subordinates()) == 2
    assert s.get_citizen(5).get_superior() == c2
    assert s.get_citizen(3).get_superior() == c5
###########################################################################
# Tests for method in Task 3.1
###########################################################################


def test_promote_citizen() -> None:
    s = promote_citizen_example()
    s.promote_citizen(11)
    promoted = s.get_citizen(11)
    demoted = s.get_citizen(5)
    assert isinstance(promoted, DistrictLeader)
    assert promoted.get_district_name() == 'Finance'
    assert [c.cid for c in promoted.get_all_subordinates()] == [5, 7, 13]
    assert promoted.get_superior().cid == 6
    assert not isinstance(demoted, DistrictLeader)
    assert [c.cid for c in demoted.get_all_subordinates()] == [7, 13]
    assert demoted.get_superior() == promoted


def test_promote_citizen_v1() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 25)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'watcher', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 20)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = Citizen(12, 'oscorp', 3011, 'lancer', 99)
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    s.promote_citizen(12)
    assert s.get_head() == s.get_citizen(12)
    assert isinstance(s.get_citizen(12), DistrictLeader)
    c6 = s.get_citizen(6)
    assert [c.cid for c in c6.get_all_subordinates()] == [5, 7, 9, 50, 60]
    # assert c6.get_all_subordinates() == [c5, c7, c9, c50, c60]
    c12 = s.get_citizen(12)
    assert c12.job == 'moron'


def test_promote_citizen_v2() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 20)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'watcher', 20)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 20)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 20)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 100)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = DistrictLeader(12, 'oscorp', 3011, 'lancer', 99, 'finance')
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    s.promote_citizen(12)
    assert s.get_head() == c6
    assert c12.get_all_subordinates() == [c50, c60]
    assert c60.get_district_name() == 'finance'
    assert c50.get_district_name() == 'la mer'
    s.promote_citizen(10)
    c10 = s.get_citizen(10)
    assert s.get_head() == c10
    assert c10.get_superior() is None
    assert c11.get_all_subordinates() == []
    assert c11.get_superior() == s.get_citizen(6)
    assert s.get_citizen(2).get_superior() == s.get_citizen(6)
    assert c11.get_district_name() == 'eng'
    c2 = s.get_citizen(2)
    assert c2.get_superior() == s.get_citizen(6)


def test_promote_citizen_v3() -> None:
    """Test promote_citizen on head"""
    s = Society()
    c1 = DistrictLeader(6, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 70)
    # c3 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    # c4 = Citizen(11, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 6)
    s.promote_citizen(2)
    promoted = s.get_citizen(2)
    demoted = s.get_citizen(6)
    assert isinstance(promoted, DistrictLeader)
    assert promoted.get_superior() is None
    assert not isinstance(demoted, DistrictLeader)
    assert [c.cid for c in promoted.get_all_subordinates()] == [demoted.cid]
    assert [c.cid for c in demoted.get_all_subordinates()] == []
    assert demoted.get_superior() == promoted


def test_promote_citizen_v4() -> None:
    """Test promote_citizen on head"""
    s = Society()
    c1 = DistrictLeader(6, "Some Lab", 3024, "Commander", 65, "District A")
    c2 = Citizen(2, "Hookins National Lab", 3024, "Lawyer", 30)
    # c3 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Labourer", 55)
    # c4 = Citizen(11, "Starky Industries", 3022, "Manager", 55)
    s.add_citizen(c1)
    s.add_citizen(c2, 6)
    s.promote_citizen(2)
    # 2 didn't promote
    promoted = s.get_citizen(2)
    demoted = s.get_citizen(6)
    assert isinstance(promoted, Citizen)
    assert promoted.get_superior() is demoted
    assert isinstance(demoted, Citizen)
    assert [c.cid for c in promoted.get_all_subordinates()] == []
    assert [c.cid for c in demoted.get_all_subordinates()] == [promoted.cid]
    assert demoted.get_superior() is None


def test_promote_citizen_sub_and_sup() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)

    s.promote_citizen(3)
    assert s.get_head() == s.get_citizen(3)
    assert s.get_citizen(5).get_superior() == s.get_citizen(2)
    assert s.get_citizen(2).get_superior() == s.get_citizen(1)
    assert s.get_citizen(1).get_superior() == s.get_citizen(3)
    assert len(s.get_citizen(2).get_direct_subordinates()) == 2


def test_promote_citizen_equal_rating() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 93)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)

    s.promote_citizen(3)
    assert s.get_citizen(3).get_superior() == s.get_citizen(2)


def test_promote_citizen_less_rating() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 94)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)

    s.promote_citizen(3)
    assert s.get_citizen(3).get_superior() == s.get_citizen(2)


def test_promote_citizen_dl() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)

    s.change_citizen_type(2, 'Take This District')
    s.promote_citizen(3)
    assert s.get_citizen(3).get_superior() == s.get_citizen(1)
    assert isinstance(s.get_citizen(3), DistrictLeader)
    assert s.get_head() == s.get_citizen(1)


def test_promote_citizen_top_dl() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)

    s.change_citizen_type(1, 'King of the World')
    s.promote_citizen(6)
    assert s.get_citizen(1).get_superior() == s.get_citizen(6)
    assert isinstance(s.get_citizen(6), DistrictLeader)
    assert s.get_head() == s.get_citizen(6)
    assert s.get_citizen(3).get_superior() == s.get_citizen(2)
    assert s.get_citizen(2).get_direct_subordinates()[1] == s.get_citizen(5)
###########################################################################
# Tests for method in Task 3.2
###########################################################################


def test_get_highest_rated_subordinate() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    result = who.get_highest_rated_subordinate()
    assert result.cid == 5


def test_get_highest_rated_subordinate_v1() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 30, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 10)
    # c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 10)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c2, 6)
    assert c6.get_highest_rated_subordinate() == c2


# this test varies by implementation and the answer for the first assert
# statement is either c5 or c8
def test_get_highest_rated_subordinate_v2() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 20)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'watcher', 80)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 10)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 80)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 100)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = DistrictLeader(12, 'oscorp', 3011, 'lancer', 9, 'finance')
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c6.get_highest_rated_subordinate() == c5
    assert c5.get_highest_rated_subordinate() == c9


def test_get_highest_rated_subordinate_v3() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v4() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', -1)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v5() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 0)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v6() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 0)
    c2 = Citizen(12, 'Citizen 11', 3011, 'Watcher', 0)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    s.add_citizen(c2, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v7() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 2)
    c2 = Citizen(12, 'Citizen 11', 3011, 'Watcher', 4)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    s.add_citizen(c2, 1)
    assert c.get_highest_rated_subordinate().cid == 12


def test_delete_citizen() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert s.get_citizen(6) is None


def test_delete_citizen_v1() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    s = Society()
    s.add_citizen(c6)
    assert s.get_head() == c6
    s.delete_citizen(6)
    assert s.get_head() is None


def test_delete_citizen_v2() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 20)
    c6.add_subordinate(c2)
    s = Society()
    s.add_citizen(c6)
    assert s.get_head() == c6
    s.delete_citizen(6)
    assert s.get_head() == c2
    assert s.get_all_citizens() == [c2]


def test_delete_citizen_v3() -> None:
    c6 = DistrictLeader(6, 'Citizen 1', 3001, 'moron', 10, 'eng')
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 20)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = Citizen(5, 'oscorp', 3011, 'watcher', 80)
    c7 = Citizen(7, 'oscorp', 3011, 'a', 10)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 80)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 100)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = DistrictLeader(12, 'oscorp', 3011, 'lancer', 9, 'finance')
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c12.get_all_subordinates() == [c50, c60]
    s.delete_citizen(50)
    assert c12.get_all_subordinates() == [c60]


def test_delete_citizen_v4() -> None:
    c6 = Citizen(6, 'Citizen 1', 3001, 'moron', 10)
    c2 = Citizen(2, 'Citizen 11', 3011, 'moron', 20)
    c3 = Citizen(3, 'oscorp', 3011, 'babysitter', 20)
    c5 = DistrictLeader(5, 'oscorp', 3011, 'watcher', 80, 'echoplex')
    c7 = Citizen(7, 'oscorp', 3011, 'a', 10)
    c8 = Citizen(8, 'oscorp', 3011, 'moron', 80)
    c9 = Citizen(9, 'oscorp', 3011, 'a', 20)
    c10 = Citizen(10, 'oscorp', 3011, 'a', 100)
    c11 = Citizen(11, 'oscorp', 3011, 'a', 20)
    c4 = Citizen(4, 'oscorp', 3011, 'a', 20)
    c12 = DistrictLeader(12, 'oscorp', 3011, 'lancer', 9, 'finance')
    c50 = DistrictLeader(50, 'oscorp', 3011, 'moron', 20, 'la mer')
    c60 = Citizen(60, 'oscorp', 3011, 'moron', 20)
    c12.add_subordinate(c50)
    c12.add_subordinate(c60)
    c10.become_subordinate_to(c2)
    c11.become_subordinate_to(c2)
    c7.become_subordinate_to(c5)
    c9.become_subordinate_to(c5)
    c6.add_subordinate(c8)
    c6.add_subordinate(c2)
    c6.add_subordinate(c5)
    c6.add_subordinate(c3)
    s = Society()
    s.add_citizen(c6)
    s.add_citizen(c12, 5)
    assert c9.get_district_name() == 'echoplex'
    s.delete_citizen(5)
    assert c9.get_district_name() == ''


def test_delete_king() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    c7 = Citizen(7, 'test 7', 2025, 'Seven', 1)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    c7.become_subordinate_to(c1)

    s.delete_citizen(1)
    assert s.get_head() == c2
    assert s.get_citizen(2).get_direct_subordinates()[2] == c7
    assert c1.get_superior() is None and c1.get_direct_subordinates() == []


def test_delete_citizen_with_sub_and_sup() -> None:
    c1 = Citizen(1, 'test1', 2021, 'One', 91)
    c2 = Citizen(2, 'test2', 2022, 'Two', 92)
    c3 = Citizen(3, 'test3', 2023, 'Three', 93)
    c4 = Citizen(4, 'test4', 2024, 'Four', 94)
    c5 = Citizen(5, 'test5', 2025, 'Five', 95)
    c6 = Citizen(6, 'test6', 2026, 'Six', 96)
    c7 = Citizen(7, 'test 7', 2025, 'Seven', 1)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    c5.become_subordinate_to(c3)
    c6.become_subordinate_to(c3)
    c7.become_subordinate_to(c1)

    s.delete_citizen(2)
    assert s.get_head() == c1
    assert s.get_citizen(1).get_direct_subordinates()[1] == c4
    assert c2.get_superior() is None and c2.get_direct_subordinates() == []


class AdditionalTests:
    pass

def test_get_all_subordinates_out_of_order() -> None:
    """Get all subordinates of a tree that is not ordered -- UNORDERED here on.
    """
    c1 = Citizen(10, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c50 = Citizen(50, "S.T.A.R.R.Y Lab", 3050, "Commander", 60)
    c5 = Citizen(5, "blob", 3023, "Engin5", 50)
    c6 = Citizen(6, "blob", 3024, "Engin6", 51)

    c6.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    c3.become_subordinate_to(c50)
    c50.become_subordinate_to(c5)
    c5.become_subordinate_to(c1)
    result = c1.get_all_subordinates()
    assert result == [c2, c3, c5, c6, c50]


def test_get_all_subordinates_not_head() -> None:
    """Get all subordinates of a general citizen (*not* root of tree)."""
    c1 = Citizen(10, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "blob lab", 3011, "Worker", 61)
    c4.become_subordinate_to(c1)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    result = c1.get_all_subordinates()
    assert result == [c4]
###########################################################################


def test_get_all_subordinates_long() -> None:
    """Get all subordinates of a long tree."""
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c50 = Citizen(50, "S.T.A.R.R.Y Lab", 3050, "Commander", 60)
    c6 = Citizen(6, "blob", 3024, "Engin6", 51)
    c700 = Citizen(700, "blob", 3025, "Engin700", 52)
    c8 = Citizen(8, "blob", 3026, "Engin8", 53)
    c92 = Citizen(92, "blob", 3027, "Engin92", 54)
    c1 = Citizen(1, "blob", 3028, "Engin1", 55)
    c701 = Citizen(701, "blob", 3025, "Engin701", 56)
    c81 = Citizen(81, "blob", 3026, "Engin81", 57)
    c921 = Citizen(921, "blob", 3027, "Engin921", 58)
    c11 = Citizen(11, "blob", 3028, "Engin11", 59)
    c800 = Citizen(800, "blob", 3025, "Engin800", 60)
    c7 = Citizen(7, "blob", 3026, "Engin7", 61)
    c102 = Citizen(102, "blob", 3027, "Engin102", 62)
    c3 = Citizen(3, "blob", 3028, "Engin3", 63)
    c3.become_subordinate_to(c102)
    c102.become_subordinate_to(c7)
    c7.become_subordinate_to(c800)
    c800.become_subordinate_to(c11)
    c11.become_subordinate_to(c921)
    c921.become_subordinate_to(c81)
    c81.become_subordinate_to(c701)
    c701.become_subordinate_to(c1)
    c1.become_subordinate_to(c92)
    c92.become_subordinate_to(c8)
    c8.become_subordinate_to(c700)
    c700.become_subordinate_to(c6)
    c6.become_subordinate_to(c50)
    c50.become_subordinate_to(c4)
    c4.become_subordinate_to(c2)

    lst = c2.get_all_subordinates()
    assert lst == [c1, c3, c4, c6, c7, c8, c11, c50, c81, c92, c102,
                   c700, c701, c800, c921]


def test_get_all_subordinates_2branch() -> None:
    """Get all subordinates of a tree with two children (no descendants)."""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3006, "Commander", 70)
    c1.become_subordinate_to(c2)
    c6.become_subordinate_to(c2)  # splits into two branches
    lst = c2.get_all_subordinates()
    assert lst == [c1, c6]


def test_get_all_subordinates_2branch_descendant_kids() -> None:
    """Get all subordinates of a tree with two children (and descendants)."""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c50 = Citizen(50, "S.T.A.R.R.Y Lab", 3050, "Commander", 60)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3006, "Commander", 70)
    c92 = Citizen(92, "blob", 3027, "Engin92", 54)
    c701 = Citizen(701, "blob", 3025, "Engin701", 56)
    c2.become_subordinate_to(c3)
    c1.become_subordinate_to(c2)
    c50.become_subordinate_to(c2)
    c92.become_subordinate_to(c3)
    c701.become_subordinate_to(c92)
    c6.become_subordinate_to(c92)
    lst = c3.get_all_subordinates()
    assert lst == [c1, c2, c6, c50, c92, c701]


def test_get_all_subordinates_10branch() -> None:
    """Get all subs of a tree with many children (no descendants)"""
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c50 = Citizen(50, "S.T.A.R.R.Y Lab", 3050, "Commander", 60)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3006, "Commander", 70)
    c92 = Citizen(92, "blob", 3027, "Engin92", 54)
    c701 = Citizen(701, "blob", 3025, "Engin701", 56)
    c81 = Citizen(81, "blob", 3026, "Engin81", 57)
    c621 = Citizen(621, "blob", 3027, "Engin921", 58)
    c14 = Citizen(14, "blob", 3034, "Engin14", 59)
    c15 = Citizen(15, "blob", 3034, "Engin15", 60)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c1)  # splits into two branches
    c50.become_subordinate_to(c1)
    c6.become_subordinate_to(c1)
    c92.become_subordinate_to(c1)
    c701.become_subordinate_to(c1)
    c81.become_subordinate_to(c1)
    c621.become_subordinate_to(c1)
    c14.become_subordinate_to(c1)
    c15.become_subordinate_to(c1)
    lst = c1.get_all_subordinates()
    assert lst == [c2, c3, c6, c14, c15, c50, c81, c92, c621, c701]


def test_get_all_subordinates_10branch_descendants() -> None:
    """Get all subs of a tree with many children (and many descendants)"""
    c = citizen_system()
    lst = c.get_all_subordinates()
    for index in range(len(lst)):
        assert lst[index].cid == index + 1
    # this works, lol


###########################################################################
# Tests for method get_closest_common_superior
###########################################################################
def test_get_closest_common_superior2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c6 = Citizen(6, "blob", 3024, "Engin6", 51)
    c7 = Citizen(7, "blob", 3025, "Engin7", 52)
    c8 = Citizen(8, "blob", 3026, "Engin8", 53)
    c9 = Citizen(9, "blob", 3027, "Engin9", 54)
    c10 = Citizen(10, "blob", 3028, "Engin10", 55)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c1)
    c4.become_subordinate_to(c1)
    c5.become_subordinate_to(c1)
    c6.become_subordinate_to(c2)
    c9.become_subordinate_to(c6)
    c10.become_subordinate_to(c6)
    c7.become_subordinate_to(c2)
    c8.become_subordinate_to(c7)

    # testing with a common parent
    assert c9.get_closest_common_superior(10) == c6
    assert c10.get_closest_common_superior(9) == c6
    assert c6.get_closest_common_superior(7) == c2
    assert c7.get_closest_common_superior(6) == c2
    assert c2.get_closest_common_superior(3) == c1
    assert c3.get_closest_common_superior(2) == c1
    assert c3.get_closest_common_superior(4) == c1
    assert c4.get_closest_common_superior(3) == c1
    assert c4.get_closest_common_superior(5) == c1
    assert c5.get_closest_common_superior(4) == c1

    # one of them is the superior
    assert c9.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(9) == c2
    assert c10.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(10) == c2
    assert c7.get_closest_common_superior(8) == c7
    assert c8.get_closest_common_superior(7) == c7
    assert c8.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(8) == c2
    assert c6.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(6) == c2
    assert c7.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(7) == c2
    assert c2.get_closest_common_superior(1) == c1
    assert c3.get_closest_common_superior(1) == c1
    assert c4.get_closest_common_superior(1) == c1
    assert c5.get_closest_common_superior(1) == c1
    assert c1.get_closest_common_superior(2) == c1
    assert c1.get_closest_common_superior(3) == c1
    assert c1.get_closest_common_superior(4) == c1
    assert c1.get_closest_common_superior(5) == c1

    # they are the same citizen
    assert c1.get_closest_common_superior(1) == c1
    assert c2.get_closest_common_superior(2) == c2
    assert c3.get_closest_common_superior(3) == c3
    assert c4.get_closest_common_superior(4) == c4
    assert c5.get_closest_common_superior(5) == c5
    assert c6.get_closest_common_superior(6) == c6
    assert c7.get_closest_common_superior(7) == c7
    assert c8.get_closest_common_superior(8) == c8
    assert c9.get_closest_common_superior(9) == c9
    assert c10.get_closest_common_superior(10) == c10

    # the closest common is just the society head
    assert c9.get_closest_common_superior(5) == c1  # c10 and 5 is the same
    assert c5.get_closest_common_superior(9) == c1
    assert c8.get_closest_common_superior(5) == c1
    assert c6.get_closest_common_superior(5) == c1
    assert c7.get_closest_common_superior(5) == c1
    assert c10.get_closest_common_superior(3) == c1

    # should I try this with citizen_society()?


###########################################################################
# Tests for methods in Task 1.3
###########################################################################
def test_add_citizen_indirect_subs() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)

    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)  # the original head
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c2.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 100)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    c5.become_subordinate_to(c2)
    c6.become_subordinate_to(c2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    c8.become_subordinate_to(c6)
    c9.become_subordinate_to(c6)
    c10.become_subordinate_to(c6)
    c7 = Citizen(7, 'Citizen 7', 3007, 'Builder', 58)
    c7.become_subordinate_to(c4)

    s.add_citizen(c1)
    s.add_citizen(c3, 1)
    assert s.get_head() == c1
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is None
    assert c3.get_superior() == c1
    assert c1.get_direct_subordinates() == [c3]
    sub = c1.get_direct_subordinates()[0]
    assert sub == c3
    assert sub.get_direct_subordinates() == [c2, c4]
    assert sub.get_all_subordinates() == [c2, c4, c5, c6, c7, c8, c9, c10]


def test_add_citizen_indirect_subs_with_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)

    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)  # the original head
    s.add_citizen(c3)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    s.add_citizen(c2, 3)
    s.add_citizen(c4, 3)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 100)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    c8 = Citizen(8, 'Citizen 8', 3008, 'Farmer', 22)
    c9 = Citizen(9, 'Citizen 9', 3009, 'Farmer', 22)
    c10 = Citizen(10, 'Citizen 10', 3010, 'Driver', 22)
    s.add_citizen(c8, 6)
    s.add_citizen(c9, 6)
    s.add_citizen(c10, 6)
    c7 = Citizen(7, 'Citizen 7', 3007, 'Builder', 58)
    s.add_citizen(c7, 4)

    s.add_citizen(c1)
    assert s.get_head() == c1
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is None
    assert c3.get_superior() == c1
    assert c1.get_direct_subordinates() == [c3]
    sub = c1.get_direct_subordinates()[0]
    assert sub == c3
    assert sub.get_direct_subordinates() == [c2, c4]
    assert sub.get_all_subordinates() == [c2, c4, c5, c6, c7, c8, c9, c10]


###########################################################################
# Tests for methods in Task 2.2
###########################################################################
def test_rename_district_empty() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c1.rename_district('john')
    assert c1.get_district_name() == ''


def test_rename_district_empty2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Stary Industries", 3025, "Worker", 51)
    c2.become_subordinate_to(c1)
    c2.rename_district('john')
    assert c2.get_district_name() == ''


def test_rename_district_bottom_child() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 10, 'cool district')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 5)
    c5 = Citizen(5, 'Susan', 2000, 'jump', 5)
    c6 = Citizen(6, 'Betty', 2001, 'run', 5)
    c7 = Citizen(7, 'Mary', 2000, 'jump', 15)
    c8 = Citizen(8, 'Hank', 2000, 'jump', 15)
    s = Society(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 3)
    s.add_citizen(c5, 4)
    s.add_citizen(c6, 5)
    s.add_citizen(c7, 6)
    s.add_citizen(c8, 6)
    c8.rename_district('New Name')
    assert c1.get_district_name() == 'New Name'
    # then add a lower district leader to test if that intercepts the call
    s.change_citizen_type(3, 'Blocks')
    c3 = s.get_citizen(3)
    assert c3.get_district_name() == 'Blocks'
    c7.rename_district('Yikes')
    assert c1.get_district_name() == 'New Name'
    assert c3.get_district_name() == 'Yikes'
    # now add a new leader between 2 leaders to test
    s.change_citizen_type(2, '2 District')
    c2 = s.get_citizen(2)
    c3.rename_district('No!')
    assert c1.get_district_name() == 'New Name'
    assert c2.get_district_name() == '2 District'
    assert c3.get_district_name() == 'No!'
    # one last attempt to change from bottom
    c8.rename_district('Last Change')
    assert c1.get_district_name() == 'New Name'
    assert c2.get_district_name() == '2 District'
    assert c3.get_district_name() == 'Last Change'


###########################################################################
# Tests for method in Task 2.3
###########################################################################
def test_change_citizen_type_leader_to_cit() -> None:
    s = sample_society2()
    s.change_citizen_type(1)
    who = s.get_citizen(1)
    assert isinstance(who, Citizen)
    assert who.get_district_name() == ''
    assert [c.cid for c in who.get_all_subordinates()] == [2, 3, 4, 5, 6, 7,
                                                           8, 9, 10]
    assert who.get_superior() is None


def test_change_citizen_type_leader_to_dist() -> None:
    s = sample_society1()
    s.change_citizen_type(1, "I am the boss again")
    who = s.get_citizen(1)
    assert isinstance(who, DistrictLeader)
    assert who.get_district_name() == 'I am the boss again'
    assert [c.cid for c in who.get_all_subordinates()] == [2, 3, 4, 5, 6, 7,
                                                           8, 9, 10]
    assert who.get_superior() is None


###########################################################################
# Tests for method in Task 3.1
###########################################################################
def test_get_highest_rated_subordinate2() -> None:
    s = sample_society0()

    assert s.get_head().get_highest_rated_subordinate() == s.get_citizen(3)
    subs = s.get_head().get_direct_subordinates()
    c2 = subs[0]
    # c3 = subs[1]  # has no subs, so can't run get_highest_rated_sub on it
    c4 = subs[2]  # has 1 sub
    assert c2.get_highest_rated_subordinate() == s.get_citizen(5)
    assert c4.get_highest_rated_subordinate() == s.get_citizen(7)

    c6 = c2.get_direct_subordinates()[1]
    assert c6.get_highest_rated_subordinate() == s.get_citizen(8)


def test_promote_citizen_head_leader() -> None:
    s = promote_citizen_example()
    s.promote_citizen(6)
    assert s.get_head() == s.get_citizen(6)
    assert isinstance(s.get_head(), DistrictLeader)


def test_promote_citizen_head_not_leader() -> None:
    c1 = Citizen(1, 'Bob', 2001, 'run', 20)
    s = Society(c1)
    s.promote_citizen(1)
    assert s.get_head() == s.get_citizen(1)
    assert not isinstance(s.get_head(), DistrictLeader)


def test_promote_citizen_supe_rating_higher() -> None:
    c1 = Citizen(1, 'Bob', 2001, 'run', 20)
    c2 = Citizen(2, 'Jack', 2000, 'jump', 10)
    c3 = Citizen(3, 'Wade', 2001, 'run', 20)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 10)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c2)
    s.promote_citizen(2)
    assert s.get_head() == s.get_citizen(1)
    assert not isinstance(c2, DistrictLeader)
    assert c2.get_superior() == c1
    assert c2.get_direct_subordinates() == [c3, c4]
    assert c3.get_superior() == c2
    assert c4.get_superior() == c2
    assert c1.get_direct_subordinates() == [c2]


def test_promote_citizen_supe_rating_equal_district_leader() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 20, 'cool')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 20)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    s.promote_citizen(4)  # nothing should've changed
    top = s.get_citizen(1)
    bottom = s.get_citizen(4)
    assert s.get_head() == s.get_citizen(1)
    assert isinstance(top, DistrictLeader)
    assert s.get_citizen(2).get_superior() == bottom
    assert bottom.get_superior() == top
    assert top.get_superior() is None
    assert top.get_direct_subordinates() == [bottom]
    assert bottom.get_direct_subordinates() == [s.get_citizen(2)]


def test_promote_citizen_supe_leader_but_higher_rating() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 20, 'cool district')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 15)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    s.promote_citizen(4)
    assert s.get_head() == s.get_citizen(1)
    assert not isinstance(s.get_citizen(4), DistrictLeader)
    assert isinstance(s.get_citizen(1), DistrictLeader)
    assert s.get_citizen(4).get_superior() == s.get_citizen(1)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_citizen(2).get_superior() == s.get_citizen(4)
    assert s.get_citizen(1).get_direct_subordinates() == [s.get_citizen(4)]


def test_promote_citizen_supe_rating_equal() -> None:
    c1 = Citizen(1, 'Bob', 2001, 'run', 20)
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 20)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    s.promote_citizen(4)
    assert s.get_head() == s.get_citizen(1)
    assert not isinstance(s.get_citizen(4), DistrictLeader)
    assert s.get_citizen(1).get_superior() is None
    assert s.get_citizen(4).get_superior() == s.get_citizen(1)
    assert s.get_citizen(2).get_superior() == s.get_citizen(4)
    assert s.get_citizen(1).get_direct_subordinates() == [s.get_citizen(4)]
    assert s.get_citizen(4).get_direct_subordinates() == [s.get_citizen(2)]


def test_promote_citizen_supe_leader_lower_rating() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 10, 'cool district')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 15)
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    s.promote_citizen(4)
    promoted = s.get_citizen(4)
    demoted = s.get_citizen(1)
    assert s.get_head() == s.get_citizen(4)
    assert isinstance(promoted, DistrictLeader)
    assert not isinstance(demoted, DistrictLeader)
    assert demoted.get_superior() == promoted
    assert promoted.get_superior() is None
    assert s.get_citizen(2).get_superior() == demoted
    assert demoted.get_direct_subordinates() == [s.get_citizen(2)]
    assert s.get_citizen(3).get_direct_subordinates() == []


def test_promote_citizen_is_already_leader() -> None:
    c1 = Citizen(1, 'Bob', 2001, 'run', 20)
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = DistrictLeader(4, 'Mark', 2000, 'jump', 20, 'cool district')
    s = Society(c1)
    c2.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    s.promote_citizen(4)
    assert s.get_head() == s.get_citizen(1)
    assert isinstance(c4, DistrictLeader)
    assert c1.get_superior() is None
    assert c4.get_superior() == c3
    assert c2.get_superior() == c1
    assert c3.get_direct_subordinates() == [c4]


def test_swap_up_to_head() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 10, 'cool district')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    s = Society(c1)
    s.add_citizen(c2, 1)
    s._swap_up(c2)
    new_head = s.get_citizen(2)
    assert s.get_head() == new_head
    assert new_head.get_superior() is None
    assert new_head.get_all_subordinates() == [s.get_citizen(1)]
    assert isinstance(new_head, DistrictLeader)
    assert not isinstance(s.get_citizen(1), DistrictLeader)
    assert len(s.get_all_citizens()) == 2
    assert new_head.job == 'run'
    assert s.get_citizen(1).job == 'jump'


def test_swap_many_children() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 10, 'cool district')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 5)
    c5 = Citizen(5, 'Susan', 2000, 'jump', 5)
    c6 = Citizen(6, 'Betty', 2001, 'run', 5)
    c7 = Citizen(7, 'Mary', 2000, 'jump', 15)
    c8 = Citizen(8, 'Hank', 2000, 'jump', 15)
    s = Society(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 2)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    s.add_citizen(c7, 3)
    s.add_citizen(c8, 7)
    s._swap_up(c3)
    c2 = s.get_citizen(2)
    c3 = s.get_citizen(3)
    assert c3.get_superior() == c1
    assert c1.get_direct_subordinates() == [c3]
    assert c2.get_superior() == c3
    assert c3.get_direct_subordinates() == [c2, c4, c5, c6]
    assert c2.get_all_subordinates() == [c7, c8]
    assert not isinstance(c3, DistrictLeader)
    assert len(s.get_all_citizens()) == 8
    assert c3.job == 'jump'
    assert c2.job == 'run'


###########################################################################
# Tests for method in Task 3.2
###########################################################################

def test_delete_head_equal_rated_children() -> None:
    c1 = DistrictLeader(1, 'Bob', 2001, 'run', 10, 'cool district')
    c2 = Citizen(2, 'Jack', 2000, 'jump', 5)
    c3 = Citizen(3, 'Wade', 2001, 'run', 5)
    c4 = Citizen(4, 'Mark', 2000, 'jump', 5)
    c5 = Citizen(5, 'Susan', 2000, 'jump', 5)
    c6 = Citizen(6, 'Betty', 2001, 'run', 5)
    c7 = Citizen(7, 'Mary', 2000, 'jump', 15)
    c8 = Citizen(8, 'Hank', 2000, 'jump', 15)
    s = Society(c1)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 1)
    s.add_citizen(c5, 2)
    s.add_citizen(c6, 2)
    s.add_citizen(c7, 3)
    s.add_citizen(c8, 7)
    assert c1.get_highest_rated_subordinate() == c2
    s.delete_citizen(1)
    assert s.get_head() == c2
    assert c2.get_superior() is None
    assert c3.get_superior() == c2
    assert c4.get_superior() == c2
    assert c7.get_superior() == c3
    assert c2.get_direct_subordinates() == [c3, c4, c5, c6]
    assert s.get_citizen(1) is None
    assert s.get_all_citizens() == [c2, c3, c4, c5, c6, c7, c8]


def test_delete_citizen_new() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert [c.get_superior().cid for c in who.get_direct_subordinates()] == \
           [2, 2, 2, 2]
    assert s.get_citizen(6) is None


def test_delete_citizens_and_heads_in_order() -> None:
    s = sample_society0()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert [c.get_superior().cid for c in who.get_direct_subordinates()] == \
           [2, 2, 2, 2]
    assert s.get_citizen(6) is None

    s.delete_citizen(4)
    who = s.get_citizen(7)
    who2 = s.get_citizen(1)
    assert who.get_direct_subordinates() == []
    assert [c.cid for c in who2.get_direct_subordinates()] == [2, 3, 7]
    assert [c.get_superior().cid for c in who2.get_direct_subordinates()] == \
           [1, 1, 1]
    assert s.get_citizen(4) is None

    s.delete_citizen(2)
    who = s.get_citizen(1)
    whos = [s.get_citizen(5), s.get_citizen(8), s.get_citizen(9),
            s.get_citizen(10)]
    assert [c.cid for c in who.get_direct_subordinates()] == [3, 5, 7, 8, 9, 10]
    assert [c.get_direct_subordinates() for c in whos] == [[], [], [], []]
    assert [c.get_superior().cid for c in whos] == [1, 1, 1, 1]
    assert s.get_citizen(2) is None

    s.delete_citizen(1)
    who = s.get_citizen(5)
    assert s.get_head() == who
    assert [c.cid for c in who.get_direct_subordinates()] == [3, 7, 8, 9, 10]
    whos = [s.get_citizen(3), s.get_citizen(7), s.get_citizen(8),
            s.get_citizen(9), s.get_citizen(10)]
    assert [c.get_superior().cid for c in whos] == [5, 5, 5, 5, 5]
    assert s.get_citizen(1) is None

    best = s.get_citizen(5).get_highest_rated_subordinate()
    s.delete_citizen(5)
    who = s.get_citizen(3)
    assert who == best
    assert s.get_head() == who
    assert [c.cid for c in who.get_direct_subordinates()] == [7, 8, 9, 10]
    whos = [s.get_citizen(7), s.get_citizen(8), s.get_citizen(9),
            s.get_citizen(10)]
    assert [c.get_superior().cid for c in whos] == [3, 3, 3, 3]
    assert s.get_citizen(5) is None

    best = s.get_citizen(3).get_highest_rated_subordinate()
    s.delete_citizen(3)
    who = s.get_citizen(7)
    assert who == best
    assert s.get_head() == who
    assert [c.cid for c in who.get_direct_subordinates()] == [8, 9, 10]
    whos = [s.get_citizen(8), s.get_citizen(9), s.get_citizen(10)]
    assert [c.get_superior().cid for c in whos] == [7, 7, 7]
    assert s.get_citizen(3) is None

    best = s.get_citizen(7).get_highest_rated_subordinate()
    s.delete_citizen(7)
    who = s.get_citizen(8)
    assert who == best
    assert s.get_head() == who
    assert [c.cid for c in who.get_direct_subordinates()] == [9, 10]
    whos = [s.get_citizen(9), s.get_citizen(10)]
    assert [c.get_superior().cid for c in whos] == [8, 8]
    assert s.get_citizen(7) is None

    best = s.get_citizen(8).get_highest_rated_subordinate()
    s.delete_citizen(8)
    who = s.get_citizen(9)
    assert who == best
    assert s.get_head() == who
    assert [c.cid for c in who.get_direct_subordinates()] == [10]
    whos = [s.get_citizen(10)]
    assert [c.get_superior().cid for c in whos] == [9]
    assert s.get_citizen(8) is None

    best = s.get_citizen(9).get_highest_rated_subordinate()
    s.delete_citizen(9)
    who = s.get_citizen(10)
    assert who == best
    assert s.get_head() == who
    assert [c for c in who.get_direct_subordinates()] == []
    assert s.get_citizen(9) is None

    # best = s.get_citizen(10).get_highest_rated_subordinate()  # None
    s.delete_citizen(10)  # society should now be empty
    # assert best is None
    assert s.get_head() is None
    assert s.get_citizen(10) is None


def test_delete_head_no_children() -> None:
    s = Society()
    c1 = Citizen(1, 'Bob', 2001, 'Jumper', 11)
    s.add_citizen(c1)
    s.delete_citizen(1)
    assert s.get_head() is None


def test_delete_head_with_children() -> None:
    s = sample_society2()
    old_head = s.get_head()
    assert old_head.cid == 1
    s.delete_citizen(1)
    new_head = s.get_head()
    assert new_head.cid == 3
    subs = new_head.get_all_subordinates()
    assert len(subs) == 8
    assert new_head.get_superior() is None


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test_complete.py'])
