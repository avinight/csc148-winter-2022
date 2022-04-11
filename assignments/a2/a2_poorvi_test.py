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


###########################################################################
# Tests for methods in Task 1.1 Poorvi
###########################################################################


def test_add_subordinate_not_empty() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c._subordinates = [c1]
    c.add_subordinate(c5)
    assert c.get_direct_subordinates()[0] is c5
    assert c.get_direct_subordinates()[1] is c1
    assert c5.get_superior() is c


def test_add_subordinate_not_empty_1() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c._subordinates = [c5]
    c.add_subordinate(c1)
    assert c.get_direct_subordinates()[0] is c5
    assert c.get_direct_subordinates()[1] is c1
    assert c1.get_superior() is c


def test_add_subordinate_not_empty_2() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c3 = Citizen(3, 'Citizen 3', 3005, 'Farmer', 101)
    c4 = Citizen(4, 'Citizen 4', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 4', 3005, 'Farmer', 101)
    c7 = Citizen(7, 'Citizen 4', 3005, 'Farmer', 101)
    c._subordinates = [c1, c2, c4, c5]
    c.add_subordinate(c3)
    c2.add_subordinate(c7)
    assert c.get_direct_subordinates()[2] is c3
    assert [x.cid for x in c.get_direct_subordinates()] == [11, 2, 3, 4, 5]
    assert [x.cid for x in c2.get_direct_subordinates()] == [7]
    c2.add_subordinate(c6)
    assert [x.cid for x in c2.get_direct_subordinates()] == [6, 7]
    assert c3.get_superior() is c
    assert c6.get_superior() is c2
    assert c7.get_superior() is c2


def test_remove_subordinate_one() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c.add_subordinate(c1)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates() == []
    assert c1.get_superior() is None


def test_remove_subordinate_1() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c5)
    c.remove_subordinate(11)
    assert c.get_direct_subordinates()[0] == c2
    assert c.get_direct_subordinates()[1] == c5
    assert c1.get_superior() is None


def test_remove_subordinate_2() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c5)
    c.remove_subordinate(5)
    assert c.get_direct_subordinates()[0] == c2
    assert c.get_direct_subordinates()[1] == c1
    assert c5.get_superior() is None


def test_remove_subordinate_two() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c3 = Citizen(3, 'Citizen 2', 3005, 'Farmer', 101)
    c4 = Citizen(4, 'Citizen 2', 3005, 'Farmer', 101)
    c.add_subordinate(c1)
    c.add_subordinate(c2)
    c.add_subordinate(c5)
    c2.add_subordinate(c3)
    c2.add_subordinate(c4)
    c.remove_subordinate(2)
    assert c.get_direct_subordinates()[0] == c5
    assert c.get_direct_subordinates()[1] == c1
    assert c2.get_superior() is None


def test_become_subordinate_to() -> None:
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c1.become_subordinate_to(None)
    assert c1.get_superior() is None


def test_become_subordinate_to_1() -> None:
    c = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    c1 = Citizen(11, 'Citizen 11', 3011, 'Watcher', 25)
    c2 = Citizen(2, 'Citizen 2', 3005, 'Farmer', 101)
    c1.become_subordinate_to(c)
    assert c.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c
    c1.become_subordinate_to(c2)
    assert c2.get_direct_subordinates()[0] is c1
    assert c1.get_superior() is c2
    assert c.get_direct_subordinates() == []


def test_get_citizen() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(7)
    assert who is None


def test_get_citizen_one() -> None:
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    who = c5.get_citizen(5)
    assert who is c5


def test_get_citizen_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    assert c3.get_citizen(3) is c3
    assert c3.get_citizen(1) is c1
    assert c3.get_citizen(4) is None
    assert c2.get_citizen(1) is c1
    assert c2.get_citizen(3) is None


def test_get_citizen_2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    assert c2.get_direct_subordinates()[0] is c1
    assert c2.get_direct_subordinates()[1] is c3
    assert c2.get_citizen(3) is c3


def test_get_citizen_3() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    assert c2.get_direct_subordinates()[0] is c1
    assert c2.get_direct_subordinates()[1] is c3
    assert c2.get_citizen(55) is None


###########################################################################
# Tests for methods in Task 1.2 Poorvi
###########################################################################


def test_get_all_subordinates() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    c4.become_subordinate_to(c3)
    assert c2.get_all_subordinates()[0] is c1
    assert c2.get_all_subordinates()[1] is c3
    assert c2.get_all_subordinates()[2] is c4
    assert [x.cid for x in c3.get_all_subordinates()] == [4]
    assert c4.get_all_subordinates() == []
    assert c1.get_all_subordinates() == []


def test_get_all_subordinates_doctest() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    assert c3.get_all_subordinates()[0].cid == 1
    assert c3.get_all_subordinates()[1].cid == 2


def test_get_all_subordinates_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert c1.get_all_subordinates() == []


def test_get_society_head() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    head = c1.get_society_head()
    assert head is c1


def test_get_society_head_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c2.become_subordinate_to(c3)
    head = c1.get_society_head()
    head1 = c2.get_society_head()
    assert head is c3
    assert head1 is c3


def test_get_closest_common_superior_test() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c2.become_subordinate_to(c1)
    c4.become_subordinate_to(c1)
    c3.become_subordinate_to(c2)
    c5.become_subordinate_to(c2)
    assert c3.get_closest_common_superior(5) == c2
    assert c5.get_closest_common_superior(3) == c2
    assert c3.get_closest_common_superior(4) == c1
    assert c4.get_closest_common_superior(3) == c1
    assert c3.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(3) == c2

    assert c1.get_closest_common_superior(1) == c1
    assert c2.get_closest_common_superior(2) == c2
    assert c3.get_closest_common_superior(3) == c3
    assert c4.get_closest_common_superior(4) == c4
    assert c5.get_closest_common_superior(5) == c5


def test_get_closest_common_superior_piazza() -> None:
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c10 = Citizen(10, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "Starky Industries", 3022, "Manager", 55)
    c8 = Citizen(8, "Hookins National Lab", 3023, "Engineer", 50)
    c9 = Citizen(9, "Hookins National Lab", 3023, "Engineer", 50)
    c5 = Citizen(5, "Hookins National Lab", 3023, "Engineer", 50)
    c6 = Citizen(6, "Hookins National Lab", 3023, "Engineer", 50)
    c7 = Citizen(7, "Hookins National Lab", 3023, "Engineer", 50)
    c11 = Citizen(11, "Hookins National Lab", 3023, "Engineer", 50)
    c12 = Citizen(12, "Hookins National Lab", 3023, "Engineer", 50)
    c2.become_subordinate_to(c3)
    c10.become_subordinate_to(c3)
    c4.become_subordinate_to(c3)
    c8.become_subordinate_to(c2)
    c9.become_subordinate_to(c2)
    c5.become_subordinate_to(c4)
    c6.become_subordinate_to(c4)
    c7.become_subordinate_to(c4)
    c11.become_subordinate_to(c6)
    c12.become_subordinate_to(c6)
    assert c12.get_closest_common_superior(4) is c4
    assert c4.get_closest_common_superior(12) is c4


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
    assert c3.get_closest_common_superior(3) == c3
    assert c2.get_closest_common_superior(4) == c3
    assert c4.get_closest_common_superior(2) == c3
    assert c5.get_closest_common_superior(3) == c3


def test_get_closest_common_superior_1() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    assert c1.get_closest_common_superior(1) == c1


def test_get_closest_common_superior_2() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c1.become_subordinate_to(c2)
    assert c1.get_closest_common_superior(2) == c2
    assert c2.get_closest_common_superior(1) == c2


def test_get_closest_common_superior_3() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c2)
    assert c1.get_closest_common_superior(3) == c2
    assert c3.get_closest_common_superior(1) == c2


def test_get_closest_common_superior_4() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c1.become_subordinate_to(c2)
    c3.become_subordinate_to(c1)
    assert c3.get_closest_common_superior(1) == c1


###########################################################################
# Tests for methods in Task 1.3 Poorvi
###########################################################################


def test_add_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c1)
    assert s.get_head() == c1
    s.add_citizen(c2, 1)
    assert s.get_head() == c1
    assert len(c1.get_all_subordinates()) == 1
    assert c2 in c1.get_all_subordinates()


def test_add_citizen_11() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c1)
    s.add_citizen(c3, 1)
    assert s.get_head() == c1
    s.add_citizen(c2)
    assert s.get_head() == c2
    assert len(c2.get_all_subordinates()) == 2
    assert c1 in c2.get_all_subordinates()
    assert c3 in c2.get_all_subordinates()
    assert c3 in c1.get_all_subordinates()


def test_add_citizen_1() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    s.add_citizen(c1)
    s.add_citizen(c2)
    assert s.get_head() == c2
    assert c1 in c2.get_all_subordinates()
    assert len(c2.get_all_subordinates()) == 1


def test_add_citizen_2() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    s.add_citizen(c1)
    s.add_citizen(c2)
    s.add_citizen(c3, 2)
    s.add_citizen(c4, 3)
    assert s.get_head() == c2
    assert c1 in c2.get_direct_subordinates() and \
           c3 in c2.get_direct_subordinates()
    assert len(c2.get_direct_subordinates()) == 2
    assert c4.get_superior() is c3
    assert c4 in c3.get_all_subordinates()
    assert len(c3.get_all_subordinates()) == 1


def test_add_citizen_4() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    c2 = Citizen(2, "Some Lab", 3024, "Lawyer", 30)
    c3 = Citizen(3, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    c5 = Citizen(5, "S.T.A.R.R.Y Lab", 3010, "Commander", 60)
    s.add_citizen(c3)
    s.add_citizen(c2, 3)
    s.add_citizen(c4, 3)
    s.add_citizen(c1, 2)
    s.add_citizen(c5)
    assert s.get_head() is c5
    assert len(c5.get_direct_subordinates()) == 1
    assert c3 in c5.get_direct_subordinates()
    assert len(c5.get_all_subordinates()) == 4


def test_society_get_citizen() -> None:
    s = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Labourer", 50)
    s.add_citizen(c1)
    assert s.get_citizen(1) is c1
    assert s.get_citizen(2) is None


def test_society_get_citizen_empty() -> None:
    s = Society()
    assert s.get_citizen(2) is None


def test_society_get_citizen_1() -> None:
    s = sample_society0()
    who = s.get_citizen(8)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [8, 'Citizen 8', 3008, 'Farmer', 22]


def test_get_all_citizens() -> None:
    o = Society()
    c1 = Citizen(1, "Starky Industries", 3024, "Manager", 50)
    # c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 65)
    # c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    # c4 = Citizen(4, "S.T.A.R.R.Y Lab", 3024, "Manager", 30)
    # c5 = Citizen(5, "Hookins National Lab", 3024, "Labourer", 50)
    # c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 30)
    o.add_citizen(c1, None)
    # o.add_citizen(c2, 4)
    # o.add_citizen(c6, 2)
    # o.add_citizen(c1, 4)
    # o.add_citizen(c3, 1)
    # o.add_citizen(c5, 1)
    assert o.get_all_citizens() == [c1]


def test_get_citizens_with_job() -> None:
    s = Society()
    result = [c.cid for c in s.get_citizens_with_job('Farmer')]
    assert result == []


def test_get_citizens_with_job_1() -> None:
    s = sample_society0()
    result = [c.cid for c in s.get_citizens_with_job('xyz')]
    assert result == []


def test_get_district_name() -> None:
    s = sample_society1()
    who = s.get_citizen(4)
    result = who.get_district_name()
    assert result == ''


def test_delete_citizen() -> None:
    s = sample_society1()
    s.delete_citizen(6)
    who = s.get_citizen(2)
    assert [c.cid for c in who.get_direct_subordinates()] == [5, 8, 9, 10]
    assert s.get_citizen(6) is None
    s.delete_citizen(1)
    who1 = s.get_citizen(3)
    assert s.get_head() == who1
    assert [c.cid for c in who1.get_direct_subordinates()] == [2, 4]


def test_change_citizen_type() -> None:
    s = sample_society1()
    s.change_citizen_type(2)
    who = s.get_citizen(2)
    assert not isinstance(who, DistrictLeader)
    assert isinstance(who, Citizen)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating] == \
           [2, 'Citizen 2', 3002, 'Bank robber', 19]
    assert [c.cid for c in who.get_all_subordinates()] == [5, 6, 8, 9, 10]
    assert who.get_superior().cid == 1


def test_change_citizen_type_1() -> None:
    s = sample_society1()
    s.change_citizen_type(1, 'D1')
    who = s.get_citizen(1)
    assert isinstance(who, DistrictLeader)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating,
            who.get_district_name()] == [1, 'Citizen 1', 3001, 'Big boss', 10,
                                         'D1']
    assert s.get_head().cid == 1
    assert [c.cid for c in who.get_all_subordinates()] == [2, 3, 4, 5, 6, 7, 8,
                                                           9, 10]
    assert who.get_superior() is None


def test_change_citizen_type_2() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Big boss', 10)
    s.add_citizen(c1)
    s.change_citizen_type(1, 'D1')
    who = s.get_citizen(1)
    assert isinstance(who, DistrictLeader)
    assert [who.cid, who.manufacturer, who.model_year, who.job, who.rating,
            who.get_district_name()] == [1, 'Citizen 1', 3001, 'Big boss', 10,
                                         'D1']
    assert who.get_superior() is None
    assert who.get_all_subordinates() == []


def test_delete_citizen_1() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    s.delete_citizen(1)
    assert s.get_head() is None


def test_delete_citizen_2() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.delete_citizen(1)
    assert s.get_head() is c3
    assert c2 in s.get_head().get_all_subordinates()


def test_delete_citizen_3() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    s.add_citizen(c2, 1)
    s.delete_citizen(1)
    assert s.get_head() is c2
    assert s.get_head().get_all_subordinates() == []


def test_delete_citizen_4() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 2)
    s.add_citizen(c5, 3)
    s.add_citizen(c6, 3)
    s.delete_citizen(1)
    assert s.get_head() is c3
    assert [x.cid for x in s.get_head().get_direct_subordinates()] == [2, 5, 6]


def test_delete_citizen_21() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.delete_citizen(2)
    assert s.get_head() is c1
    assert [x.cid for x in s.get_head().get_all_subordinates()] == [3]


def test_delete_citizen_31() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    s.add_citizen(c2, 1)
    s.delete_citizen(2)
    assert s.get_head() is c1
    assert s.get_head().get_all_subordinates() == []


def test_delete_citizen_41() -> None:
    s = Society()
    c1 = Citizen(1, 'Citizen 1', 3001, 'Watcher', 10)
    s.add_citizen(c1)
    c2 = DistrictLeader(2, 'Citizen 2', 3002, 'Bank robber', 19, 'D2')
    c3 = Citizen(3, 'Citizen 3', 3003, 'Cook', 82)
    c4 = Citizen(4, 'Citizen 4', 3004, 'Cook', 5)
    c5 = Citizen(5, 'Citizen 5', 3005, 'Farmer', 101)
    c6 = Citizen(6, 'Citizen 6', 3006, 'Coach', 56)
    s.add_citizen(c2, 1)
    s.add_citizen(c3, 1)
    s.add_citizen(c4, 2)
    s.add_citizen(c5, 3)
    s.add_citizen(c6, 3)
    s.delete_citizen(3)
    assert [x.cid for x in s.get_head().get_direct_subordinates()] == [2, 5, 6]
    s.delete_citizen(4)
    assert [x.cid for x in s.get_head().get_direct_subordinates()] == [2, 5, 6]
    assert c2.get_all_subordinates() == []


def test_piazza() -> None:
    c1 = Citizen(1, "Starky Industries", 3024, "Manager", 50)
    c2 = Citizen(2, "Hookins National Lab", 3024, "Manager", 65)
    c3 = Citizen(3, "Starky Industries", 3024, "Labourer", 50)
    c4 = DistrictLeader(4, "S.T.A.R.R.Y Lab", 3024, "Manager", 60, 'd')
    c5 = Citizen(5, "Hookins National Lab", 3024, "Labourer", 80)
    c6 = Citizen(6, "S.T.A.R.R.Y Lab", 3024, "Lawyer", 70)
    o = Society(c4)
    o.add_citizen(c2, 4)
    o.add_citizen(c6, 2)
    o.add_citizen(c1, 4)
    o.add_citizen(c3, 1)
    o.add_citizen(c5, 1)
    o.promote_citizen(6)
    assert isinstance(o.get_citizen(6), DistrictLeader)
    assert not isinstance(o.get_citizen(4), DistrictLeader)


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_poorvi_test.py'])
