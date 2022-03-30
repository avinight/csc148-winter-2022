"""Lab and lecture code: Tournament, with the same interface as before,
but with a more elaborate data structure.

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains a new version of Tournament.  Here we change the attributes
so we keep track of more information and can do more things, if we wish to write
some new methods.

We have been careful not to change the interface to any of the methods, but
of course the method bodies have to change to support the new way the attributes
are working.
"""
from typing import List, Dict


class Tournament:
    """A sports tournament.

    === Attributes ===
    teams:
        The names of the teams in this tournament.
    team_stats:
        The history of each team in this tournament. Each key is a team name,
        and each value is a list of game results for this team.  Each game
        result is itself a list containing this team's score and the opposing
        team's score.

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
    team_stats: Dict[str, List[List]]   # This type had to change.

    def __init__(self, teams: List[str]) -> None:
        """Initialize a new Tournament among the given teams.

        Note: Does not make an alias to <teams>.
        """
        self.team_stats = {}
        self.teams = []
        for team_name in teams:
            self.teams.append(team_name)
            # This line had to change.  Instead of starting with 0 games played
            # and 0 wins, we start with an empty list of game results.
            self.team_stats[team_name] = []

    def record_game(self, team1: str, team2: str,
                    score1: int, score2: int) -> None:
        """Record the fact that <team1> played <team2> with the given scores.

        <team1> scored <score1> and <team2> scored <score2> in this game.

        Precondition: team1 and team2 are both in this tournament.
        """
        # Record a game played for both teams.
        # This method had to completely be re-writeen:
        self.team_stats[team1].append([score1, score2])
        self.team_stats[team2].append([score2, score1])

    def best_percentage(self) -> str:
        """Return the team name with the highest percentage of games won.

        If no team has won a game, return the empty string.
        Otherwise if there is a tie for best percentage, return the name of any
        of the tied teams.
        """
        best_team_so_far = ''
        best_percentage_so_far = 0
        for team, record in self.team_stats.items():
            # The body of this loop had to be rewritten:
            if len(record) != 0:
                wins = 0
                played = 0
                for game_result in record:
                    played += 1
                    if game_result[0] > game_result[1]:
                        wins += 1
                percentage = wins / played
                if percentage > best_percentage_so_far:
                    best_percentage_so_far = percentage
                    best_team_so_far = team
        return best_team_so_far


if __name__ == '__main__':
    import doctest
    doctest.testmod()
