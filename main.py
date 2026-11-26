#!/usr/bin/env python3
"""make.fun bounty entry: The Word You'd Delete From the Dictionary.

If you could delete one word from the dictionary, which would it be?
This program deletes one — in one line — and the dictionary
has agreed not to press charges.
"""

WORD = "synergy (and its cousin, 'circle back')"


def word():
    """Return the word you'd delete from the dictionary."""
    return WORD


def main():
    print(word())


if __name__ == "__main__":
    main()
