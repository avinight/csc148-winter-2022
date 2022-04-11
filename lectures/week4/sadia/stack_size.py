from stack import Stack


def size(s: Stack) -> int:
    """Return the number of items in s.

    >>> st = Stack()
    >>> size(st)
    0
    >>> st.push('hi')
    >>> st.push('more')
    >>> st.push('stuff')
    >>> size(st)
    3
    """

    temp = Stack()
    count = 0

    # Pop everything off <s> and onto <temp>, counting as we go
    while not s.is_empty():
        temp.push(s.pop())
        count += 1

    # Now pop everything off <temp> and back into <s>
    while not temp.is_empty():
        s.push(temp.pop())

    # <s> is now restored to its state at the start of the function call
    # We consider that it was not mutated

    return count


def size_v2(s: Stack) -> int:
    """Return the number of items in s.

    >>> st = Stack()
    >>> size_v2(st)
    0
    >>> st.push('hi')
    >>> st.push('more')
    >>> st.push('stuff')
    >>> size_v2(st)
    3
    """

    temp = []
    count = 0

    # Pop everything off <s> and onto <temp>, counting as we go
    while not s.is_empty():
        temp.append(s.pop())
        count += 1

    # Now take everything from <temp> back into <s>
    temp.reverse()
    for elm in temp:
        s.push(elm)

    # ALTERNATE TO THE ABOVE, use list.pop
    #while len(temp) > 0:
    #    s.push(temp.pop())

    # <s> is now restored to its state at the start of the function call
    # We consider that it was not mutated

    return count
