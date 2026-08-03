#!/usr/bin/python3
"""Insert text after every file line containing a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line containing search_string."""
    updated_lines = []
    with open(filename, encoding="utf-8") as file:
        for line in file:
            updated_lines.append(line)
            if search_string in line:
                updated_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(updated_lines)
