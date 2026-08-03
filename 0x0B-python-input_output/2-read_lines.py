#!/usr/bin/python3
"""Read a requested number of lines from a UTF-8 text file."""


def read_lines(filename="", nb_lines=0):
    """Print nb_lines lines from filename, or the whole file when needed."""
    with open(filename, encoding="utf-8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
            return

        for line_number, line in enumerate(file, 1):
            print(line, end="")
            if line_number >= nb_lines:
                break
