"""Catching exceptions

=== Copyright information ===
CSC148
Department of Computer Science
University of Toronto

=== Module description ===
This module demonstrates the basics of 'catching' and dealing with exceptions,
rather than letting them clear the stack and report a nasty error message to
the user.

Here's the general rule for when an exception is raised (directly by saying
"raise" or indirectly, eg by dividing by zero):
- If the line of code that caused the exception is in a try-except clause,
  check the except clauses in order, to see if any of them matches the type
  of exception raised.
- If one of them does match, do the code in its except block. (If several match,
  take the first one). Then continue on with the next line after the try-except
  clause. Emergency over!
- If none of them matches, or if there was no try-except clause surrounding the
  problematic line of code, then stop this method/function immediately, pop the
  stack frame, and give the exception to the line of code that called this
  function/method.

It is possible to end with a 'bare' except clause, that is, one with no
specific type of exception named.  This is similar to a final else clause
with no condition.  While fine for if-statements, this is considered bad style
for exceptions. The reason is that a bare except clause will catch any kind
of exception, including one the programmer didn't anticipate. They might never
realize that this kind of exception is happening, and this may allow a bug to
fester. Instead we should name all the kinds of exceptions we anticipate. Then
if an unanticipated type of exception arises, it will stop the program and get
the programmer's attention, allowing them to address the problem.

Try running this and giving an integer as input, then run it with "bad" input.
Then modify the code so that f2 handles the two kinds of error instead.
Run the code again and observe how it is different. Modify the code again to
move the error handling to f1 or to the main block, or split it up so that
one function handles one kind of error and the other is handled elsewhere.
"""


def f3() -> None:
    # The 'try' says to Python: Go ahead and try running the code inside
    # this block.  But if an error is raised, (1) jump immediately to the
    # first 'except', (2) find the first 'except' clause that matches the
    # error (3) do what is in its block, and (4) carry on with the
    # program.
    try:
        x = input('Enter a number: ')
        print(100 / int(x))
        print('That went well')
    except ZeroDivisionError:
        print('do not divide by zero!')
    except ValueError:
        print('That was not a number!')
    print('Okay, let\'s continue with this program')


def f2() -> None:
    f3()


def f1() -> None:
    f2()


if __name__ == '__main__':
    f1()
    print('All done.')
