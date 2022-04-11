"""A module demonstrating special methods (also known as magic methods).
"""

from __future__ import annotations
from typing import Any, Optional


class Snowball:
    pass


class Shoe:
    """The implementations for these special methods are all completely
    silly, but they demonstrate how special methods work.
    """
    def __str__(self) -> str:
        return "hee hee"

    def __eq__(self, other: Shoe) -> bool:
        return True

    def __contains__(self, item: Any) -> bool:
        return False

    def __len__(self) -> int:
        return 1000

    def __getitem__(self, item: Any) -> Optional[Any]:
        return 42


if __name__ == '__main__':
    # Class snowball defines no methods, but it inherits a lot from object.
    print('=== First some snow ===')
    # The inherited __init__ is called here. It can't set up any instance
    # variables, but it does allow this line to run without error.
    fluffy = Snowball()
    icy = Snowball()
    # The inherited __str__ is called here. It can't print anything specific
    # to Snowballs, so it report's fluffy's type and id.
    print(fluffy)
    # The inherited __eq__ is called here. It can't compare based on anything
    # specific to Snowballs, so it compares based on ids.
    if fluffy == icy:
        print('Samesies')
    else:
        print('Different')
    # There is no __contains__ in object to inherit, so this raises an error.
    # if 13 in fluffy:
    #     print('Yup')
    # else:
    #     print('Nope')
    # There is no __len__ in object to inherit, so this raises an error.
    # print(len(fluffy))
    # There is no __getitem__ in object to inherit, so this raises an error.
    # print(fluffy[5])

    print('=== Now for some shoes ===')
    fluevog = Shoe()
    birkenstock = Shoe()
    # In class Shoe, we override the inherited __str__ and __eq__,
    # so they are called instead.
    print(fluevog)
    if fluevog == birkenstock:
        print('Samesies')
    else:
        print('Different')
    # And we define __contains__, __len__, and __getitem__ so that the code
    # below all works.
    if 13 in fluevog:
        print('Yup')
    else:
        print('Nope')
    print(len(fluevog))
    print(fluevog[5])
