from stack import Stack


# Notice that we ignore everything except round brackets.
# This is why the correct result in the third doctest is True.
def is_balanced(line: str) -> bool:
    """Return whether <line> contains balanced parentheses.

    Ignore square and curly brackets.

    >>> is_balanced('(a * (3 + b))')
    True
    >>> is_balanced('(a * (3 + b]]')
    False
    >>> is_balanced('1 + 2(x - y)}')
    True
    >>> is_balanced('3 - (x')
    False
    """
    unmatched = Stack()
    for c in line:
        if c == '(':
            unmatched.push(c)
        elif c == ')':
            if unmatched.is_empty():
                return False
            else:
                unmatched.pop()
        # If c is neither character, ignore it!
    return unmatched.is_empty()


def is_balanced_v2(line: str) -> bool:
    """Return whether <line> contains balanced parentheses.

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
    # The opening and closing brackets that are accepted.
    # len(openers) = len(closers).
    # For 0 <= i <= len(openers) - 1, brackets openers[i] and closers[i] match.
    openers = '([{'
    closers = ')]}'
    unmatched = Stack()
    for c in line:
        if c in openers:
            unmatched.push(c)
        elif c in closers:
            if unmatched.is_empty():
                return False
            else:
                opening_bracket = unmatched.pop()
                if openers.find(opening_bracket) != closers.find(c):
                    return False
        # If c is neither character, ignore it!
    return unmatched.is_empty()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
