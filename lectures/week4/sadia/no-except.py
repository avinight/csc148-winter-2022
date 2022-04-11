"""Exceptions

=== Copyright information ===
CSC148
Department of Computer Science
University of Toronto

=== Module description ===
This demonstrates what happens when a program raises an exception.
Here there are several frames on the call stack when an exception may occur.
(f2 and f3 are nonsense functions, just used to allow us to build up
the call stack before we encounter an exception.)

Try running this and giving an integer as input, then run it with "bad" input.
What does the user see?
"""


def f3() -> None:
    # There are several kinds of input the user could give that would cause
    # trouble here.  If so, an exception is raised and the function immediately
    # returns, sending back the exception.
    x = input('Enter a number: ')
    print(100 / int(x))
    print('That went well')


def f2() -> None:
    # If the call to f3 raises an exception, it lands here -- just as if
    # f2 itself had raised one.  So f2 immediately returns, sending back the
    # exception.
    f3()


def f1() -> None:
    # If the call to f2 raises an exception, it lands here -- just as if
    # f1 itself had raised one.  So f1 immediately returns, sending back the
    # exception.
    f2()


if __name__ == '__main__':
    # If the call to f1 raises an exception, it lands here -- just as if
    # the main block itself had raised one.  So the main block immediately
    # is halted, and the error message lands in the lap of the user.
    # It's not a helpful message at all!  The user should never see such
    # things.
    f1()
    print('All done.')
