"""Object-Oriented Programming: Twitter example, 21 January 2022

=== CSC148 Winter 2021 ===
Department of Computer Science,
University of Toronto

=== Module description ===
Today we discussed the things that should always be true about any instance
of Tweet: the Representation Invariants. These are included in the class
docstring (see below) and are a critical part of documentation because they help
you write correct code -- and keep it correct as the code evolves over time and
is perhaps worked on by different people.

We discussed 3 strategies for enforcing the RI that self.likes >= 0.
Below I have implemented Stratey 1 (precondition), which is my preference for
this particular RI. Notice that the precondition, which goes on method likes,
concerns a parameter (n) as preconditions always do, while the RI concerns
an instance attribute (self.likes) as RIs always do.

I have left enforcing the RI that len(self.content) <= 280 as an exercise.
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

        Precondition: n >= 0.

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
