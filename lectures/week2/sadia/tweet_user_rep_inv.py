"""Object-Oriented Programming: Twitter example

=== CSC148 Winter 2019 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module description ===
This module contains two sample classes Tweet and Person that we developed
as way to introduce the major concepts of object-oriented programming.

Please note: this is a combined version for all students, so may contain
minor inconsistencies with what you saw during lecture.
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

    === Representation Invariants ===
    - 1 <= len(self.content) <= 280
    - self.likes >= 0
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

    # Strategy 1: Write a precondition that'll make it hold

    # Remember that self.likes >= 0  is already a precondition for this
    # method. After adding precondition that n > 0, we ensure that
    # as long as the client follows the n > 0 precondition, self.likes >= 0
    # is also a postcondition for this method.
    def like(self, n: int) -> None:
        """Record the fact that this tweet received <n> likes.

        These likes are in addition to the ones <self> already has.

        Precondition: n > 0

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.like(3)
        >>> t.likes
        3
        """

        # Strategy 2: Failing silently (ignore bad input)
        #if n > 0:
        #    self.likes += n

        # Strategy 3: Fix bad input
        self.likes += abs(n)

    def edit(self, new_content: str) -> None:
        """Replace the contents of this tweet with the new message.

        Precondition: len(new_content) <= 280

        >>> t = Tweet('Rukhsana', date(2017, 9, 16), 'Hey!')
        >>> t.edit('Rukhsana is cool')
        >>> t.content
        'Rukhsana is cool'
        """
        if len(new_content) <= 280:
            self.content = new_content
        else:
            self.content = new_content[:280]


class User:
    """A Twitter user.

    === Attributes ===
    userid: the userid of this Twitter user.
    bio: the bio of this Twitter user.
    tweets: a list of the tweets that this user has made.
    follows: a list of users that this user follows
    """
    userid: str
    bio: str
    tweets: List[Tweet]
    follows: List[User] # Alternate design choice: could be a list of just the
                        # userids in which case, the datatype would be List[str]

    def __init__(self, id_: str, bio: str) -> None:
        """Initialize this User.

        >>> david = User('David', 'is cool')
        >>> david.tweets
        []
        """
        self.userid = id_
        self.bio = bio
        self.tweets = []
        self.follows = []

    def tweet(self, message: str) -> None:
        """Record that this User made a tweet with the given content.

        Use date.today() to get the current date for the newly created tweet.
        """
        new_tweet = Tweet(self.userid, date.today(), message)
        self.tweets.append(new_tweet)

    def follow_user(self, other: User) -> None:
        """
        Record that this user follows the other user.

        >>> u1 = User('Bumbly', 'Cloud')
        >>> u2 = User('Mia', 'Smol Thundercloud')
        >>> u1.follow_user(u2)
        >>> len(u1.follows)
        1
        """
        # Just one of the many possible implementations
        # Other possibilities include:
        # - storing userid (a string) rather than the User
        # - dictionary with userid as key and User as value
        # - we could add in additional info like num_followed

        self.follows.append(other)

# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'extra-imports': ['datetime']
#     })
