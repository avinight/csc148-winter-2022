from stack import Stack

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
    pass

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
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(is_balanced(input('--> ')))
