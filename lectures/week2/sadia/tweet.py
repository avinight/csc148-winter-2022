"""Object-Oriented Programming: Twitter example

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains two sample classes Tweet and User that we developed
as way to introduce the major concepts of object-oriented programming.
"""
from __future__ import annotations  # Reference: 1.4 Type Annotations

from datetime import date  # Python library for working with dates (and times)
from typing import List    # Python library for expressing complex types


class Tweet:
    """A tweet, like in Twitter.

    === Attributes ===
    content: the contents of the tweet.
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    likes: the number of likes this tweet has received.

    === Sample Usage ===

    Creating a tweet:
    >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
    >>> t.userid
    'Rukhsana'
    >>> t.created_at
    datetime.date(2017, 9, 16)
    >>> t.content
    'Hey!'

    Tracking likes for a tweet:
    >>> t.likes
    0
    >>> t.like(1)
    >>> t.likes
    1
    >>> t.like(10)
    >>> t.likes
    11
    """
    # Attribute types
    content: str
    userid: str
    created_at: date
    likes: int

    def __init__(self, who: str, when: date, what: str) -> None:
        """Initialize a new Tweet.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.userid
        'Rukhsana'
        >>> t.created_at
        datetime.date(2017, 9, 16)
        >>> t.content
        'Hey!'
        >>> t.likes
        0
        """
        self.userid = who
        self.content = what
        self.created_at = when
        self.likes = 0

    def like(self, n: int) -> None:
        """Record the fact that this tweet received <n> likes.

        These likes are in addition to the ones <self> already has.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.like(3)
        >>> t.likes
        3
        """
        self.likes += n

    def edit(self, new_content: str) -> None:
        """Replace the contents of this tweet with the new message.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        'Rukhsana is cool'
        """
        # Note: this is the incorrect version from the worksheet.
        # Notice how both PyCharm and python_ta pick up on this error.
        old_user = self.userid
        old_date = self.created_at
        self = Tweet(old_user, old_date, new_content)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={'extra-imports': ['datetime']})
