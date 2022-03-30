def is_prime3(n: int) -> bool:
    """Precondition n > 1."""
    if n == 2:
        return True
    elif n > 2:
        count = 0
        d = 2
        while d <= (n ** 1/2):
            if is_prime3(d) and n % d == 0:
                return False
            d += 1
        return count == 0
    return False
