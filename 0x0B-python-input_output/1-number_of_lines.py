#!/usr/bin/python3
"""Count the number of lines in a UTF-8 text file."""


def number_of_lines(filename=""):
    """Return the number of lines contained in filename."""
    with open(filename, encoding="utf-8") as file:
        return sum(1 for _ in file)
