from mystack import Stack
from typing import Optional


def undo(i: str, stack: Stack) -> Optional[str]:
    """Returns the most recently stored string,
    and removes it from the stack."""

    if i == "UNDO":
        return stack.pop()
    stack.push(i)


s = Stack()
while True:
    user_input = input('Enter a string: ')
    undo_out = undo(user_input, s)
    print(undo_out)

