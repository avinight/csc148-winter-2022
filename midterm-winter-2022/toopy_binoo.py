def binoo(stuff, i) -> None:
    stuff[i] = 27


def toopy(lst, add) -> None:
    binoo(lst[0], 1)
    lst.append(add)


if __name__ == '__main__':
    nums = [26, 17, 39]
    word = 'hi'
    things = [nums, word]
    toopy(things, '!')
    print(things)
