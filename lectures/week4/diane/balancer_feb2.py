"""An application for stacks, Feb 2, 2022

=== CSC148 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for two functions that use one or more
stacks to check for balanced brackets.  The first version handles only
round brackets, and the second extends to additional types of bracket.

In class today, we acted out bracket-balancing (with just round brackets),
and used that experience to come up with a proposed strategy, which we tested
out on some examples on paper.  Then we implemented the method and observed
that it passed the doctests on the first try!  Thinking before coding can
really pay off.

As an exercise, try to generalize the algorithm to handle square, round, and
curly brackets, and implement it in the commented-out function is_balanced_v2
below.
"""

from adts import Stack


def is_balanced(line: str) -> bool:
    """Return True iff <line> contains balanced round brackets.

    >>> is_balanced('(a * (3 + b))')
    True
    >>> is_balanced('(a * (3 + b]]')
    False
    >>> is_balanced('1 + 2(x - y)}')
    True
    >>> is_balanced('3 - (x')
    False
    """
    # Keep a stack of unmatched open brackets.
    # QU: could this code ever pop from an empty stack?
    unmatched = Stack()
    for c in line:
        if c == '(':
            unmatched.push(c)
        elif c == ')':
            if unmatched.is_empty():
                return False
            else:
                # We know unmatched is NOT empty, so this is safe:
                unmatched.pop()
        # Otherwise, c is some other character; ignore it!
    return unmatched.is_empty()


# Exercise:
def is_balanced_v2(line: str) -> bool:
    """Return True iff <line> contains balanced brackets.

    Accept round, square, and curly brackets.

    >>> is_balanced_v2('[a * (3 + b)]')
    True
    >>> is_balanced_v2('[a * (3 + b]]')
    False
    >>> is_balanced_v2('1 + 2(x - y)}')
    False
    >>> is_balanced_v2('3 - (x')
    False
    """
    unmatched = Stack()
    p_open = ['[', '{', '(']
    p_close = [']', '}', ')']
    for c in line:
        if c in p_open:
            unmatched.push(c)
        elif c in p_close:
            if unmatched.is_empty():
                return False
            else:
                if p_open.index(unmatched.pop()) != p_close.index(c):
                    return False
    return unmatched.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(is_balanced(input('--> ')))
