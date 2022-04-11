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


def test_add_subordinate_v2() -> None:
    """Test c1.add_subordinate(c)"""
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_add_subordinate_v3() -> None:
    """Test c1.add_subordinate(c) with DistrictLeader"""
    c = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "District A")
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.add_subordinate(c)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_add_subordinate_v4() -> None:
    """Test c.add_subordinate(c1) with DistrictLeader"""
    c = DistrictLeader(1, 'Citizen 1', 3001, 'Big boss', 10, "District A")
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_remove_subordinate() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_become_subordinate_to() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c


def test_become_subordinate_to_v2() -> None:
    """Test """
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.become_subordinate_to(c1)
    assert c1.get_direct_subordinates()[0] is c
    assert c.get_superior() is c1


def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 101]


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


def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    assert head is c3


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


def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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

# test_add_citizen head is not None, no superior.


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


def test_get_citizens_with_job() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == [5, 8, 9]


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


def test_rename_district() -> None:
    s = sample_society1()
    who = s.get_citizen(10)
    who.rename_district('D10')
    leader = s.get_citizen(2)
    assert leader.get_district_name() == 'D10'


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

# test_change_citizen_type_1() -> None: test

###########################################################################
# Tests for method in Task 3.1
###########################################################################


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


def test_promote_citizen_v2() -> None:
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


def test_promote_citizen_v3() -> None:
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

###########################################################################
# Tests for method in Task 3.2
###########################################################################


def test_get_highest_rated_subordinate() -> None:
    s = sample_society1()
    who = s.get_citizen(2)
    result = who.get_highest_rated_subordinate()
    assert result.cid == 5


def test_get_highest_rated_subordinate_v2() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v3() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', -1)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v4() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 0)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v5() -> None:
    s = Society()
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 0)
    c2 = Citizen(12, 'Citizen 11', 3011, 'Watcher', 0)
    s.add_citizen(c)
    s.add_citizen(c1, 1)
    s.add_citizen(c2, 1)
    assert c.get_highest_rated_subordinate().cid == 11


def test_get_highest_rated_subordinate_v6() -> None:
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


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test_v2.py'])
