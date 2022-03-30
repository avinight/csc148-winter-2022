"""CSC148 Assignment 0: Starter code

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for Assignment 0.

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) University of Toronto
"""
from datetime import date
from typing import Dict, Tuple, List, Set, Optional, TextIO

# Constants that can be used throughout this module.
# Column numbers where various values can be found in the csv files containing
# election results.
RIDING = 1
PARTY = 13
VOTES = 17


class Election:
    """Data for a single election in a parliamentary democracy.

    === Private Attributes ===
    _d: the date of this election.
    _ridings: all ridings for which any votes have been recorded in this
        election.
    _parties: all parties for which any votes have been recorded in this
        election.
    _results: the vote counts for this election.  Each key is the name of a
        riding, and its value is a dictionary of results for that one riding.
        Each of its keys, in turn, is the name of a party, and the associated
        value is the number of votes earned by that party in that riding.
            A party only appears in the dictionary for a riding if that party
        has had at least one vote recorded in that riding.

    === Representation Invariants ==
    - For all strings s, s in self._ridings iff s in self._results
    - For all strings s, s in self._parties iff s in self._results[r] for some r
    - All recorded vote counts are greater than 0. That is,
      for every key (riding, results) in self._results,
          for every (party, votes) in results,
              votes > 0

    === Sample Usage ===
    >>> e = Election(date(2000, 2, 8))
    >>> e.update_results('r1', 'ndp', 1234)
    >>> e.update_results('r1', 'lib', 1345)
    >>> e.update_results('r1', 'pc', 1456)
    >>> e.riding_winners('r1')
    ['pc']
    >>> e.update_results('r2', 'pc', 1)
    >>> e.popular_vote() == {'ndp': 1234, 'lib': 1345, 'pc': 1457}
    True
    >>> e.results_for('r1', 'lib')
    1345
    >>> e.party_seats() == {'ndp': 0, 'lib': 0, 'pc': 2}
    True
    """
    _d: date
    _ridings: List[str]
    _parties: List[str]
    _results: Dict[str, Dict[str, int]]

    def __init__(self, d: date) -> None:
        """Initialize a new election on date d and with no ridings, parties,
        or votes recorded so far.

        >>> e = Election(date(2000, 2, 8))
        >>> e._d
        datetime.date(2000, 2, 8)
        """
        self._d = d
        self._ridings = []
        self._parties = []
        self._results = {}

    def ridings_recorded(self) -> List[str]:
        """Return the ridings in which votes have been recorded in this
         election.

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1)
        >>> e.ridings_recorded()
        ['r1']
        >>> e.update_results('r2', 'ndp', 1)
        >>> e.ridings_recorded()
        ['r1', 'r2']
        """
        return self._ridings

    def update_results(self, riding: str, party: str, votes: int) -> None:
        """Update this election to reflect that in <riding>, <party> received
        <votes> additional votes.

        <riding> may or may not already have some votes recorded in this
        election.  <party> may or may not already have some votes recorded in
        this riding in this election.

        Precondition: votes >= 1

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1)
        >>> e.results_for('r1', 'ndp')
        1
        >>> e.update_results('r1', 'ndp', 1000)
        >>> e.results_for('r1', 'ndp')
        1001
        """
        if riding not in self._results:
            self._results[riding] = {}
            self._ridings.append(riding)
        if party not in self._results[riding]:
            self._results[riding][party] = 0
            self._parties.append(party)
        if riding and party in self._results[riding]:
            self._results[riding][party] += votes

    def read_results(self, input_stream: TextIO) -> None:
        """Update this election with the results in input_stream.

        Precondition: input_stream is an open csv file, in the format defined
        in the A0 handout.
        """
        # Get data from c1, c3, c17
        # Remove double quotes from strings
        # Be careful not to alias
        data = []
        input_stream.readline()
        for line in input_stream:
            line = line.replace('\"', '')
            data.append(line.strip().split(","))

        for line in data:
            if int(line[VOTES]) >= 1:
                if line[RIDING] not in self._results:
                    self._results[line[RIDING]] = {}
                    self._ridings.append(line[RIDING])
                if line[PARTY] not in self._results[line[RIDING]]:
                    self._results[line[RIDING]][line[PARTY]] = 0
                    self._parties.append(line[PARTY])
                if line[RIDING] and line[PARTY] in self._results[line[RIDING]]:
                    self._results[line[RIDING]][line[PARTY]] += int(line[VOTES])

    def results_for(self, riding: str, party: str) -> Optional[int]:
        """Return the number of votes received in <riding> by <party> in
        this election.

        Return None if <riding> does not have any votes recorded in this
        election, or if it does, but <party> does not have any votes recorded
        in this riding in this election.

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1234)
        >>> e.update_results('r1', 'lib', 1345)
        >>> e.update_results('r1', 'pc', 1456)
        >>> e.update_results('r2', 'pc', 1)
        >>> e.results_for('r1', 'pc')
        1456
        >>> e.results_for('r2', 'pc')
        1
        """
        # Return None if for all parties or just party
        # self._results[riding][party] == 0
        if self._results[riding][party] == 0:
            return None
        return self._results[riding][party]

    def riding_winners(self, riding: str) -> List[str]:
        """Return the winners, in <riding>, of this election.

        The winner is the party or parties that received the most votes in
        total. (There may have been a tie.) The return value is a list so
        that, in the case of ties, we can return a list of election_winners.
        If there is no tie, the length of the returned list is 1.

        Precondition: <riding> has at least 1 vote recorded in this election.

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1)
        >>> e.update_results('r1', 'lib', 2)
        >>> e.update_results('r1', 'pc', 3)
        >>> e.riding_winners('r1')
        ['pc']
        """
        election_winners = []
        values = self._results[riding].values()
        t = max(values)
        for party in self._results[riding]:
            if self._results[riding][party] == t:
                election_winners.append(party)
        return election_winners

    def popular_vote(self) -> Dict[str, int]:
        """For each party, return the total number of votes it earned, across
        all ridings, in this election.

        Include only parties that have at least one vote recorded in at least
        one riding.

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1)
        >>> e.update_results('r1', 'lib', 2)
        >>> e.update_results('r1', 'pc', 3)
        >>> e.update_results('r2', 'pc', 4)
        >>> e.update_results('r2', 'lib', 5)
        >>> e.update_results('r2', 'green', 6)
        >>> e.update_results('r2', 'ndp', 7)
        >>> e.popular_vote() == {'ndp': 8, 'lib': 7, 'pc': 7, 'green': 6}
        True
        """
        total = {}
        for riding in self._results:
            for party in self._results[riding]:
                if self._results[riding][party] == 0:
                    continue
                if party not in total:
                    total[party] = 0
                total[party] += self._results[riding][party]
        return total

    def party_seats(self) -> Dict[str, int]:
        """For each party, return the number of ridings that it won in this
        election.

        Include only parties that have at least one vote recorded in at least
        one riding.  If there was a tie in a riding, the riding doesn't
        contribute to the seat count for any of the parties that were tied in
        that riding.

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1)
        >>> e.update_results('r1', 'lib', 2)
        >>> e.update_results('r1', 'pc', 3)
        >>> e.update_results('r2', 'pc', 4)
        >>> e.update_results('r2', 'lib', 5)
        >>> e.update_results('r2', 'green', 6)
        >>> e.update_results('r2', 'ndp', 7)
        >>> e.party_seats() == {'pc': 1, 'ndp': 1, 'lib': 0, 'green': 0}
        True
        """
        # include parties with at least one vote
        # if there is a tie, that riding is not counted.
        winning_seats = {}
        for riding in self._results:
            for party in self._results[riding]:
                # init winning_seats and make sure parties with at least one
                # vote are included.
                if party in self.popular_vote() and \
                        party not in winning_seats:
                    winning_seats[party] = 0

            for winner in self.riding_winners(riding):
                # increment winning_seats of the winner if there was no tie
                if len(self.riding_winners(riding)) == 1:
                    winning_seats[winner] += 1

        return winning_seats

    def election_winners(self) -> List[str]:
        """Return the party (or parties, in the case of a tie) that won the
        most seats in this election.

        If no votes have been recorded in any riding in this election,
        return the empty list.

        >>> e = Election(date(2000, 2, 8))
        >>> e.update_results('r1', 'ndp', 1)
        >>> e.update_results('r1', 'lib', 2)
        >>> e.update_results('r1', 'pc', 3)
        >>> e.update_results('r2', 'lib', 5)
        >>> e.update_results('r2', 'green', 6)
        >>> e.update_results('r2', 'ndp', 7)
        >>> e.update_results('r2', 'pc', 8)
        >>> e.election_winners()
        ['pc']
        """
        seats = self.party_seats()
        if seats == {}:
            return []
        t = max(seats.values())
        winner = []
        for party in seats:
            if seats[party] == t:
                winner.append(party)
        return winner


class Jurisdiction:
    """The election history for a jurisdiction that is a parliamentary
    democracy.

    === Private Attributes ===
    _name: the name of this jurisdiction.
    _elections: the election history for this jurisdiction.  Each key is a date,
        and its value holds the results of an election that was held on that
        date.

    === Representation Invariants ==
    None.

    === Sample Usage ===
    # See the method docstrings for sample usage.
    """
    _name: str
    _elections: Dict[date, Election]

    def __init__(self, name: str) -> None:
        """Initialize this jurisdiction, with no elections so far.

        >>> country = Jurisdiction('Canada')
        >>> country._name
        'Canada'
        >>> country._elections
        {}
        """
        self._name = name
        self._elections = {}

    def read_results(self, year: int, month: int, day: int,
                     input_stream: TextIO) -> None:
        """Read and record results for an election in this jurisdiction.

        If there are already some results stored for an election on this date,
        add to them.

        Precondition: input_stream is an open csv file, in the format defined
        in the A0 handout.
        """
        # update self._elections with new election.
        if date(year, month, day) not in self._elections:
            self._elections[date(year, month, day)] = \
                Election(date(year, month, day))
        # read and record the results for that election.
        self._elections[date(year, month, day)].read_results(input_stream)

    def party_wins(self, party: str) -> List[date]:
        """Return a list of all dates on which <party> won an election in this
        jurisdiction.

        If the party tied for most seats in an election, do include that date
        in the result.

        >>> e1 = Election(date(2000, 2, 8))
        >>> e1.update_results('r1', 'ndp', 1)
        >>> e1.update_results('r1', 'lib', 2)
        >>> e1.update_results('r1', 'pc', 3)
        >>> e1.update_results('r2', 'lib', 10)
        >>> e1.update_results('r2', 'pc', 20)
        >>> e1.update_results('r3', 'ndp', 200)
        >>> e1.update_results('r3', 'pc', 100)
        >>> e2 = Election(date(2004, 5, 16))
        >>> e2.update_results('r1', 'ndp', 10)
        >>> e2.update_results('r1', 'lib', 20)
        >>> e2.update_results('r2', 'lib', 50)
        >>> e2.update_results('r2', 'pc', 5)
        >>> e3 = Election(date(2008, 6, 1))
        >>> e3.update_results('r1', 'ndp', 101)
        >>> e3.update_results('r1', 'lib', 102)
        >>> e3.update_results('r2', 'ndp', 1001)
        >>> e3.update_results('r2', 'lib', 1002)
        >>> j = Jurisdiction('Canada')
        >>> j._elections[date(2000, 2, 8)] = e1
        >>> j._elections[date(2003, 5, 16)] = e2
        >>> j._elections[date(2003, 6, 1)] = e3
        >>> j.party_wins('lib')
        [datetime.date(2003, 5, 16), datetime.date(2003, 6, 1)]
        """
        dates = []
        # iterate through the dates
        for d in self._elections:
            # if the party is a winner (even when it is a tie), append it
            if party in self._elections[d].election_winners():
                dates.append(d)

        return dates

    def party_history(self, party: str) -> Dict[date, float]:
        """Return this party's percentage of the popular vote in each election
        in this jurisdiction's history.

        Each key in the result is a date on which there was an election in
        this jurisdiction.  Its value is the percentage of the popular vote
        earned by party in that election.

        >>> j = Jurisdiction('Canada')
        >>> e1 = Election(date(2000, 2, 8))
        >>> e1.update_results('r1', 'ndp', 1)
        >>> e1.update_results('r1', 'lib', 2)
        >>> e1.update_results('r1', 'pc', 3)
        >>> e1.update_results('r2', 'pc', 4)
        >>> e1.update_results('r2', 'lib', 5)
        >>> e1.update_results('r2', 'green', 6)
        >>> e1.update_results('r2', 'ndp', 7)
        >>> e1.popular_vote() == {'ndp': 8, 'lib': 7, 'pc': 7, 'green': 6}
        True
        >>> j._elections[date(2000, 2, 8)] = e1
        >>> e2 = Election(date(2004, 5, 16))
        >>> e2.update_results('r1', 'ndp', 40)
        >>> e2.update_results('r1', 'lib', 5)
        >>> e2.update_results('r2', 'lib', 10)
        >>> e2.update_results('r2', 'pc', 20)
        >>> e2.popular_vote() == {'ndp': 40, 'lib': 15, 'pc': 20}
        True
        >>> j._elections[date(2004, 5, 16)] = e2
        >>> j.party_history('lib') == {date(2000, 2, 8): 0.25, \
        date(2004, 5, 16): 0.2}
        True
        """
        history = {}

        # iterate through dates
        for d in self._elections:
            total = 0

            # grab the dict of popular votes
            popvote = self._elections[d].popular_vote()

            # if party not in popvote:  # Deal with the case that party is not
            #     # in popular vote.
            #     popvote[party] = 0

            # sum all votes
            total += sum(popvote.values())

            # update history to reflect the percentage
            if total != 0:
                history[d] = popvote[party] / total

        return history

    def riding_changes(self) -> List[Tuple[Set[str], Set[str]]]:
        """Return the changes in ridings across elections in this jurisdiction.

        Include a tuple for each adjacent pair of elections, in order by date.
        The tuple should contain, first, a set of ridings that were removed
        between these two elections, and then a set of ridings that were added.

        Precondition: There is at least one election recorded for this
        jurisdiction.

        >>> j = Jurisdiction('Canada')
        >>> e1 = Election(date(2000, 2, 8))
        >>> e1.update_results('r1', 'ndp', 1)
        >>> e1.update_results('r1', 'lib', 1)
        >>> e1.update_results('r1', 'pc', 1)
        >>> e1.update_results('r2', 'pc', 1)
        >>> e1.update_results('r2', 'lib', 1)
        >>> e1.update_results('r2', 'green', 1)
        >>> e1.update_results('r2', 'ndp', 1)
        >>> j._elections[date(2000, 2, 8)] = e1
        >>> e2 = Election(date(2004, 5, 16))
        >>> e2.update_results('r1', 'ndp', 1)
        >>> e2.update_results('r3', 'pc', 1)
        >>> j._elections[date(2004, 5, 16)] = e2
        >>> j.riding_changes() == [({'r2'}, {'r3'})]
        True
        """
        changes = []
        dates = []

        # change dict into ordered list
        for d in self._elections:
            dates.append(d)
        dates.sort()

        # iterate through dates' indices
        for d in range(len(dates) - 1):
            # grab prev election
            r1 = self._elections[dates[d]].ridings_recorded()
            # grab next election
            r2 = self._elections[dates[d + 1]].ridings_recorded()
            # create sets for removed/added
            removed = set()
            added = set()

            for r in r1:
                # if missing from next election, add to removed
                if r not in r2:
                    removed = removed.union({r})

            for r in r2:
                # if missing from prev election, add to added.
                if r not in r1:
                    added = added.union({r})

            changes.append((removed, added))

        return changes


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'allowed-io': ['Election.read_results', 'Jurisdiction.read_results'],
        'allowed-import-modules': [
            'doctest', 'python_ta', 'datetime', 'typing'
        ],
        'max-attributes': 15
    })

    import doctest
    doctest.testmod()

    # An example of reading election results from a file.
    c = Jurisdiction('Canada')
    with open('data/parkdale-highpark.csv') as file:
        c.read_results(2015, 2, 3, file)
    with open('data/nunavut.csv') as file:
        c.read_results(2015, 2, 3, file)
    with open('data/labrador.csv') as file:
        c.read_results(2015, 2, 3, file)
    # An example of using that data to calculate some things.
    print(c.party_history('Liberal'))
    print(c.party_history('Conservative'))
    print(c.party_history('Green Party'))
    print(c.party_history('NDP-New Democratic Party'))
