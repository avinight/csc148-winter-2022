from typing import List
from itertools import combinations


def is_prime(n: int) -> bool:
    """Precondition n > 1."""
    if n == 1 or n == 2:
        return True
    elif n > 2:
        d = 2
        while d <= (n ** 1/2):
            if is_prime(d) and n % d == 0:
                return False
            d += 1
        return True
    return False


def find_factors(n: int) -> List[int]:
    """Precondition n > 1."""
    factors = []
    d = 1
    while d <= n:
        if n % d == 0:
            factors.append(d)
        d += 1
    return factors


def find_prime_factors(n: int) -> List[int]:
    lst = find_factors(n)
    lst2 = []
    for num in lst:
        if is_prime(num):
            lst2.append(num)
    return lst2


def remove_duplicates(lst: List[int]) -> List[int]:
    pass


def prime_combos(n: int):
    """Return the list of combinations of n."""
    combos = combinations(find_factors(n), 3)
    lst = []
    for combo in combos:
        a = 1
        for item in combo:
            a = a * item
        if a == n:
            lst.append(combo)
    return lst


def n_prime_combos(n: int):
    k = []
    for y in range(n + 1):
        count = 0
        for i in prime_combos(y):
            if is_prime(int(''.join(map(str, i)))):
                count += 1
        if count < 3:
            k.extend(prime_combos(y))
    k.sort()
    return k



