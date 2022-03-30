"""Object-Oriented Programming: Twitter example, 19 January 2022

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===
As of today we have:
- implemented Tweet.edit correctly, after tracing a broken version
- seen the outline of a new User class
- implemented its initializer and tweet methods
- made a memory-model diagram that shows what it looks like when one class
  references an instance of another. We say that the classes have a
  "composition" relationship: Instances of one contain instances of the other,
  among other things.

This module uses date.today() to find out what the date is.  Here's an
example of how to do this in the shell, quite separate from anything
to do with writing classes:
>>> from datetime import date
>>> date.today()
datetime.date(2022, 1, 19)
"""
# Allows forward references in type annotations.
from __future__ import annotations
from datetime import date  # Python library for working with dates (and times)
from typing import List    # Python library for expressing complex types


class Tweet:
    """A tweet, like in Twitter.

    === Attributes ===
    content: the contents of the tweet.
    userid: the id of the user who wrote the tweet.
    created_at: the date the tweet was written.
    likes: the number of likes this tweet has received.

    === Representation Invariants ===
    - len(self.content) <= 280
    - self.likes >= 0

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

        If len(new_content) > 280, only store the first 280 characters.

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        'Rukhsana is cool'
        """
        self.content = new_content


class User:
    """A Twitter user.

    === Attributes ===
    userid: the userid of this Twitter user.
    bio: the bio of this Twitter user.
    tweets: a list of the tweets that this user has made.
    """
    # Attribute types
    userid: str
    bio: str
    tweets: List[Tweet]

    def __init__(self, userid: str, bio: str) -> None:
        """Initialize a new User with the given id and bio.

        The new user initially has no tweets.

        >>> u = User('Rukhsana', 'Roller coaster fanatic')
        >>> u.userid
        'Rukhsana'
        >>> u.bio
        'Roller coaster fanatic'
        >>> u.tweets
        []
        """
        self.userid = userid
        self.bio = bio
        # We don't need a parameter to tell us how to initialize this attribute
        # because all User objects start out with no tweets.
        self.tweets = []

    def tweet(self, message: str) -> None:
        """Record that this User made a tweet with the given content.

        Use date.today() to get the current date for the newly created tweet.

        >>> u1 = User('Rukhsana', 'Roller coaster fanatic')
        >>> u1.tweet('Wheeeeee!')
        >>> u1.tweet('Again! Again!')
        >>> len(u1.tweets)
        2
        """
        t = Tweet(self.userid, date.today(), message)
        self.tweets.append(t)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Uncomment this to run pyTA:
    # import python_ta
    # python_ta.check_all(config={'extra-imports': ['datetime']})
