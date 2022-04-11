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


def test_become_subordinate_to() -> None:
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


###########################################################################
# Tests for methods in Task 1.3
###########################################################################


def test_society_get_citizen() -> None:
    s = sample_society0()
    who = s.get_citizen(5)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [5, 'Citizen 5', 3005, 'Farmer', 100]


def test_get_all_citizens() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_all_citizens()]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c2)
    s.add_citizen(c1, 2)
    assert s.get_head() == c2
    assert s.get_citizen(1) is c1
    assert c1.get_superior() is c2


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


def test_change_citizen_type_v2() -> None:
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
    s._swap_up(c3)
    assert c2.job == 'Three'
    assert c3.job == 'Two'
    assert len(c1.get_direct_subordinates()) == 1
    assert len(c2.get_direct_subordinates()) == 2
    assert c1.get_direct_subordinates()[0] == c3
    assert c4 in c3.get_direct_subordinates()
    assert c4 not in c2.get_direct_subordinates()
    assert c5 in c2.get_direct_subordinates()
    assert c5 not in c3.get_direct_subordinates()
    assert c2.get_superior() == c3
    assert c3.get_superior() == c1


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
    s._swap_up(c2)
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
    s._swap_up(c5)
    assert c3.job == 'Five'
    assert c5.job == 'Three'
    assert c3 not in c2.get_direct_subordinates()
    assert c5 not in c3.get_direct_subordinates()
    assert c3 in c5.get_direct_subordinates()
    assert c6 in c5.get_direct_subordinates()
    assert len(c3.get_direct_subordinates()) == 0
    assert len(c5.get_direct_subordinates()) == 2
    assert c5.get_superior() == c2
    assert c3.get_superior() == c5


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


def test_delete_citizen() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert s.get_citizen(6) is None


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


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test_junaid.py'])
