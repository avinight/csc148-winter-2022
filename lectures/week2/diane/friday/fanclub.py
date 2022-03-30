"""Client code example that motivates the use of private attributes

=== CSC148 winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains client code of the Tournament class.  Because the client
code accesses attributes of Tournament that were not marked as private, it is
vulnerable to breaking if the implementation of Tournament changes.

See the comments in the main block for much more detail.
"""
# from tournament import Tournament
from tournament_elaborate import Tournament
from typing import List


def losing_teams(t: Tournament) -> List[str]:
    """Return the names of teams in Tournament t that have not won any game.
    """
    answer = []
    for team, record in t.team_stats.items():
        if record[1] == 0:
            # This team has 0 wins.  Count them.
            answer.append(team)
    return answer


def num_losses(t: Tournament, team) -> int:
    """Return the number of games team played Tournament t and did not win.

    Precondition: team was in Tournament t.
    """
    record = t.team_stats[team]
    return record[0] - record[1]


if __name__ == '__main__':
    GTHL_cup = Tournament(['Leaside Flames', 'Toronto Aeros',
                           'Don Mills Mustangs', 'York Mills HC'])
    GTHL_cup.record_game('Don Mills Mustangs', 'Toronto Aeros', 4, 1)
    GTHL_cup.record_game('Leaside Flames', 'York Mills HC', 2, 3)
    GTHL_cup.record_game('Don Mills Mustangs','York Mills HC', 2, 0)
    GTHL_cup.record_game('Toronto Aeros','Leaside Flames', 4, 3)

    print(GTHL_cup)

    # This line uses a method provided by the class.  The method was correctly
    # implemented in both versions of the class, so it works properly whichever
    # version we import.
    print(GTHL_cup.best_percentage())

    # The next two lines call functions that the client code wrote and that
    # accesses attributes of the class.  The attributes were not marked with
    # an underscore to indicate that they are private and should not be
    # accessed, so accessing them was reasonable.

    # Both lines work just fine on the original version of the Tournament class,
    # defined in the tournament module.  If we instead import new_tournament,
    # they don't work.  The first line runs without error but gives the wrong
    # answer. (This is even worse than creating an error!)  Debug it and
    # see for yourself.
    print(losing_teams(GTHL_cup))
    # This second line creates an error.  Can you see why?
    print(num_losses(GTHL_cup, 'Toronto Aeros'))

    # Moral of the story: Because we defined the Tournament class without
    # saying that any of the attributes were private, the client code here
    # did nothing wrong, and yet it broke when we changed our implementation
    # of Tournament.  We didn't really have the freedom to change it.

    # If we had made the attributes private, the client code would have had
    # no right to access them, and we would have had the freedom to make any
    # changes we wished to the implementation.

    # Of course, we would have had to provide a good set of services to
    # the client so that they would find our class useful.  (Because it's a
    # toy example, the class isn't very useful as is.)
