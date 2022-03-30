"""Lab and lecture code: Same as the original Tournament class, but safer
for client code because _team_stats is private.

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a class used in lecture and lab.

The difference here is that _team_stats is now marked as private.  Programmers
writing client code that uses this class has been warned that their code 
should not even look at _team_stats. A professional programmer will follow
that rule, and their code therefore won't break if later we change the data 
structure. This gives us, the programmers working on the Tournament class,
freedom to make changes while still protecting client code.
"""
from typing import List, Dict


class Tournament:
    """A sports tournament.

    === Attributes ===
    teams:
        The names of the teams in this tournament.
    _team_stats:
        The history of each team in this tournament. Each key is a team name,
        and each value is a list storing two non-negative integers:
        the number of games played and the number won.

    === Sample usage ===

    >>> t = Tournament(['a', 'b', 'c'])
    >>> t.record_game('a', 'b', 10, 4)
    >>> t.record_game('a', 'c', 5, 1)
    >>> t.record_game('b', 'c', 2, 0)
    >>> t.best_percentage()
    'a'
    """
    # Attribute types
    teams: List[str]
    _team_stats: Dict[str, List[int]]

    def __init__(self, teams: List[str]) -> None:
        """Initialize a new Tournament among the given teams.

        Note: Does not make an alias to <teams>.
        """
        self._team_stats = {}
        self.teams = []
        for team_name in teams:
            self.teams.append(team_name)
            self._team_stats[team_name] = [0, 0]

    def record_game(self, team1: str, team2: str,
                    score1: int, score2: int) -> None:
        """Record the fact that <team1> played <team2> with the given scores.

        <team1> scored <score1> and <team2> scored <score2> in this game.

        Precondition: team1 and team2 are both in this tournament.
        """
        # Record a game played for both teams.
        self._team_stats[team1][0] += 1
        self._team_stats[team2][0] += 1
        # Record a game won for the appropriate team.
        # If it was a tie, no win is recorded.
        if score1 > score2:
            self._team_stats[team1][1] += 1
        elif score2 > score1:
            self._team_stats[team2][1] += 1

    def best_percentage(self) -> str:
        """Return the team name with the highest percentage of games won.

        If no team has won a game, return the empty string.
        Otherwise if there is a tie for best percentage, return the name of any
        of the tied teams.
        """
        best_team_so_far = ''
        best_percentage_so_far = 0
        for team, record in self._team_stats.items():
            if record[1] != 0:
                percentage = record[1] / record[0]
                if percentage > best_percentage_so_far:
                    best_percentage_so_far = percentage
                    best_team_so_far = team
        return best_team_so_far


if __name__ == '__main__':
    import doctest
    doctest.testmod()
