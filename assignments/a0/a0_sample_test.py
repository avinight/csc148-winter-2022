"""CSC148 Assignment 0: Sample tests

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
from elections import Election, Jurisdiction

# A string representing one election result.
# StringIO will take the string below and make an object that we can pass to
# method read_results just like we would pass an open file to it.
# We use this in our testing below. You can use it in your own testing, but
# you do not have to.
SHORT_FILE_CONTENTS = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '113'])


def simple_election_setup() -> Election:
    """Set up a simple Election with two ridings and three parties"""
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)

    e.update_results('r2', 'ndp', 300)
    e.update_results('r2', 'lib', 200)
    e.update_results('r2', 'pc', 100)

    return e


def simple_jurisdiction_setup() -> Jurisdiction:
    """Set up a simple Jurisdiction with a single Election and one result."""
    j = Jurisdiction('Canada')
    res1 = StringIO(SHORT_FILE_CONTENTS)
    j.read_results(2000, 1, 2, res1)
    return j


def test_simple_election_ridings_recorded() -> None:
    """Test Election.ridings_recorded with a simple Election."""
    e = simple_election_setup()
    assert e.ridings_recorded() == ['r1', 'r2']


def test_simple_election_results_for() -> None:
    """Test Election.results_for with a simple Election."""
    e = simple_election_setup()
    assert e.results_for('r1', 'ndp') == 1234


def test_simple_election_riding_winners() -> None:
    """Test Election.riding_winners with a simple Election."""
    e = simple_election_setup()
    assert e.riding_winners('r1') == ['pc']


def test_simple_election_popular_vote() -> None:
    """Test Election.popular_vote with a simple Election."""
    e = simple_election_setup()
    assert e.popular_vote() == {'ndp': 1534, 'lib': 1545, 'pc': 1556}


def test_simple_election_party_seats() -> None:
    """Test Election.party_seats with a simple Election."""
    e = simple_election_setup()
    assert e.party_seats() == {'ndp': 1, 'lib': 0, 'pc': 1}


def test_one_party_one_riding_read_results() -> None:
    """Test Election.read_results with a file with a single line."""
    file = StringIO(SHORT_FILE_CONTENTS)
    e = Election(date(2012, 10, 30))
    e.read_results(file)
    assert e.popular_vote() == {'Liberal': 113}


def test_simple_jurisdiction_party_wins() -> None:
    """Test Jurisdiction.party_wins with a file with a single line. """
    j = simple_jurisdiction_setup()
    assert j.party_wins('Liberal') == [date(2000, 1, 2)]


def test_simple_jurisdiction_party_history() -> None:
    """Test Jurisdiction.party_history with a file with a single line."""
    j = simple_jurisdiction_setup()
    assert j.party_history('Liberal') == {date(2000, 1, 2): 1.0}


def test_simple_jurisdiction_riding_changes() -> None:
    """Test Jurisdiction.riding_changes with two Elections."""
    j = simple_jurisdiction_setup()
    res2 = open('data/toronto-stpauls.csv')
    j.read_results(2004, 5, 15, res2)
    res2.close()
    assert j.riding_changes() == [({"St. Paul's"}, {"Toronto--St. Paul's"})]


def test_popular_no_vote_parties() -> None:
    """Test that popular vote returns every seat excluding 0 votes."""
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 0)
    e.update_results('r1', 'lib', 1)
    e.update_results('r1', 'pc', 1)
    e.update_results('r2', 'pc', 1)
    e.update_results('r2', 'lib', 1)
    e.update_results('r2', 'green', 1)
    e.update_results('r2', 'ndp', 0)
    assert e.popular_vote() == {'lib': 2, 'pc': 2, 'green': 1}


def test_party_history_file() -> None:
    c = Jurisdiction('Canada')
    with open('data/small_data.csv') as file:
        c.read_results(2015, 2, 3, file)
    assert c.party_history('Green Party') == {date(2015, 2, 3): 76 / 4082}


def test_jurisdiction_read_results_file() -> None:
    c = Jurisdiction('Canada')

    with open('data/brampton-centre.csv') as file:
        c.read_results(2015, 2, 3, file)
    with open('data/medicine-hat.csv') as file:
        c.read_results(2015, 2, 3, file)
    with open('data/university-rosedale.csv') as file:
        c.read_results(2015, 2, 3, file)

        # An example of using that data to calculate some things.
    print(c.party_history('Liberal'))
    print(c.party_history('Conservative'))
    print(c.party_history('Green Party'))
    print(c.party_history('NDP-New Democratic Party'))
    print(c.party_history('Marxist-Leninist'))
    print(c._elections[date(2015, 2, 3)].popular_vote())
    print(c._elections[date(2015, 2, 3)].results_for("University--Rosedale",
                                                     "Marxist-Leninist"))


def test_election_read_results_small() -> None:
    e = Election(date(2015, 2, 3))
    with open('data/small_data.csv') as file:
        e.read_results(file)
    print(sum(e.popular_vote().values()))


def test_election_update_results() -> None:
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 0)
    assert e.results_for('r1', 'ndp') is None
    e.update_results('r1', 'ndp', 1000)
    assert e.results_for('r1', 'ndp') == 1000


def test_election_read_results_zero() -> None:
    e = Election(date(2000, 2, 8))
    with open('data/test.csv') as file:
        e.read_results(file)
    assert e._parties == []
    assert e._results == {}
    assert e._ridings == []


def test_results_for_none() -> None:
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)
    e.update_results('r2', 'pc', 0)
    assert e.results_for('r2', 'pc') is None


def test_results_for_none_complete() -> None:
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 0)
    e.update_results('r2', 'pc', 0)
    assert e.results_for('r1', 'pc') is None


def test_riding_winners_ties() -> None:
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1)
    e.update_results('r1', 'lib', 3)
    e.update_results('r1', 'pc', 3)
    assert e.riding_winners('r1') == ['lib', 'pc']


def test_riding_winners_len1() -> None:
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1)
    e.update_results('r1', 'lib', 3)
    e.update_results('r1', 'pc', 2)
    assert len(e.riding_winners('r1')) == 1


def test_party_seats_no_vote() -> None:
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 0)
    e.update_results('r1', 'lib', 2)
    e.update_results('r1', 'pc', 3)
    e.update_results('r2', 'pc', 7)
    e.update_results('r2', 'lib', 5)
    e.update_results('r2', 'green', 6)
    e.update_results('r2', 'ndp', 0)
    assert e.party_seats() == {'pc': 2, 'lib': 0, 'green': 0}


def test_election_winners_empty() -> None:
    e = Election(date(2000, 2, 8))
    assert e.election_winners() == []


def test_riding_changes_empty() -> None:
    j = Jurisdiction('Canada')
    e1 = Election(date(2000, 2, 8))
    e1.update_results('r1', 'ndp', 1)
    e1.update_results('r1', 'lib', 1)
    e1.update_results('r1', 'pc', 1)
    e1.update_results('r2', 'pc', 1)
    e1.update_results('r2', 'lib', 1)
    e1.update_results('r2', 'green', 1)
    e1.update_results('r2', 'ndp', 1)
    j._elections[date(2000, 2, 8)] = e1
    e2 = Election(date(2004, 5, 16))
    e2.update_results('r1', 'ndp', 1)
    e2.update_results('r2', 'pc', 1)
    j._elections[date(2004, 5, 16)] = e2
    assert j.riding_changes() == [(set(), set())]


def test_party_wins_ties() -> None:
    import datetime
    e1 = Election(date(2000, 2, 8))
    e1.update_results('r1', 'ndp', 1)
    e1.update_results('r1', 'lib', 2)
    e1.update_results('r1', 'pc', 3)
    e1.update_results('r2', 'lib', 10)
    e1.update_results('r2', 'pc', 20)
    e1.update_results('r3', 'ndp', 200)
    e1.update_results('r3', 'pc', 100)
    e2 = Election(date(2003, 5, 16))
    e2.update_results('r1', 'ndp', 80)
    e2.update_results('r1', 'lib', 20)
    e2.update_results('r2', 'ndp', 20)
    e2.update_results('r2', 'lib', 80)
    e2.update_results('r2', 'pc', 8)
    e3 = Election(date(2003, 6, 1))
    e3.update_results('r1', 'ndp', 102)
    e3.update_results('r1', 'lib', 102)
    e3.update_results('r2', 'ndp', 1002)
    e3.update_results('r2', 'lib', 1002)
    j = Jurisdiction('Canada')
    j._elections[date(2000, 2, 8)] = e1
    j._elections[date(2003, 5, 16)] = e2
    j._elections[date(2003, 6, 1)] = e3
    assert j.party_wins('lib') == [datetime.date(2003, 5, 16),
                                   datetime.date(2003, 6, 1)]
    assert j.party_wins('ndp') == [datetime.date(2003, 5, 16),
                                   datetime.date(2003, 6, 1)]


if __name__ == '__main__':
    import pytest
    pytest.main(['a0_sample_test.py'])
