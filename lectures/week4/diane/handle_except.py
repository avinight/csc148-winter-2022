"""
Dealing with exceptions.
"""

if __name__ == '__main__':
    stuff = ['31', '8', 'mwahaha', '52']
    # Python, try to do this.  Don't try to stop it from raising a ValueError.
    # If it does, jump immediately to the "except ValueError" clause, do
    # what's there, and continue the program.
    try:
        total = 0
        for item in stuff:
            total += int(item)
    except ValueError:
        pass
    # Whether or not we end up in the except clause, the program continues here.
    print(total)
