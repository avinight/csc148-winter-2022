"""Lab and lecture code: Tournament

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a class used in lecture and lab. It has a pretty basic
way of storing the data about a tournament, and therefore is incapable of
providing stats that depend on knowing about tied games, or knowing the number
of goals scored for or against.

It also leaves all its instance attributes as public: They don't have an
underscore at the front of their name, and so client code should feel free to
look at them and even change their value.
"""
from typing import List, Dict


class Tournament:
    """A sports tournament.

    === Attributes ===
    teams:
        The names of the teams in this tournament.
    team_stats:
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
    team_stats: Dict[str, List[int]]

    def __init__(self, teams: List[str]) -> None:
        """Initialize a new Tournament among the given teams.

        Note: Does not make an alias to <teams>.
        """
        self.team_stats = {}
        self.teams = []
        for team_name in teams:
            self.teams.append(team_name)
            self.team_stats[team_name] = [0, 0]

    def record_game(self, team1: str, team2: str,
                    score1: int, score2: int) -> None:
        """Record the fact that <team1> played <team2> with the given scores.

        <team1> scored <score1> and <team2> scored <score2> in this game.

        Precondition: team1 and team2 are both in this tournament.
        """
        # Record a game played for both teams.
        self.team_stats[team1][0] += 1
        self.team_stats[team2][0] += 1
        # Record a game won for the appropriate team.
        # If it was a tie, no win is recorded.
        if score1 > score2:
            self.team_stats[team1][1] += 1
        elif score2 > score1:
            self.team_stats[team2][1] += 1

    def best_percentage(self) -> str:
        """Return the team name with the highest percentage of games won.

        If no team has won a game, return the empty string.
        Otherwise if there is a tie for best percentage, return the name of any
        of the tied teams.
        """
        best_team_so_far = ''
        best_percentage_so_far = 0
        for team, record in self.team_stats.items():
            if record[1] != 0:
                percentage = record[1] / record[0]
                if percentage > best_percentage_so_far:
                    best_percentage_so_far = percentage
                    best_team_so_far = team
        return best_team_so_far


if __name__ == '__main__':
    import doctest
    doctest.testmod()
