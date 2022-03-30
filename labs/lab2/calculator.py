class Fraction:
    """A fraction.

    === Attributes ===
    numerator: This fraction's numerator.
    denominator: This fraction's denominator.

    === Representation Invariants ===
    - self.denominator != 0

    === Sample Usage ===
    >>> f = Fraction(2, 4)
    >>> f.numerator
    2
    >>> f.denominator
    4
    >>> f.to_decimal()
    0.5
    >>> print(f)
    2 / 4
    """
    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize this fraction's attributes.
        """
        self.numerator = numerator
        self.denominator = denominator

    def to_decimal(self) -> float:
        """Return this fraction in decimal form.

        If self.denominator == 0, raise ZeroDivisionError.

        >>> f = Fraction(2, 4)
        >>> f.numerator
        2
        >>> f.denominator
        4
        >>> f.to_decimal()
        0.5
        """
        if self.denominator == 0:
            raise ZeroDivisionError
        return self.numerator / self.denominator

    def __str__(self):
        """Return a string representation of this fraction.
        >>> f = Fraction(4, 7)
        >>> print(f)
        4 / 7
        """
        return f"{self.numerator} / {self.denominator}"


def multiply(x: Fraction, y: Fraction) -> Fraction:
    """Multiply Fractions x and y together and
    return their Fraction product.
    >>> f1 = Fraction(2, 4)
    >>> print(f1)
    2 / 4
    >>> f2 = Fraction(5, 4)
    >>> print(f2)
    5 / 4
    >>> f3 = multiply(f1, f2)
    >>> print(f3)
    10 / 16
    """
    top = x.numerator * y.numerator
    bot = x.denominator * y.denominator
    return Fraction(top, bot)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
