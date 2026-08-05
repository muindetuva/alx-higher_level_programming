#!/usr/bin/python3
"""Find and replace an ASCII string in a Linux process heap."""

import sys


def heap_range(pid):
    """Return the start and end addresses of the process heap mapping."""
    maps_path = "/proc/{}/maps".format(pid)
    with open(maps_path, encoding="utf-8") as maps_file:
        for line in maps_file:
            if "[heap]" in line:
                addresses = line.split()[0]
                start, end = addresses.split("-")
                return int(start, 16), int(end, 16)
    raise RuntimeError("heap mapping not found")


def replace_heap_string(pid, search_string, replace_string):
    """Replace the first matching ASCII string in the process heap."""
    start, end = heap_range(pid)
    memory_path = "/proc/{}/mem".format(pid)
    search_bytes = search_string.encode("ascii")
    replace_bytes = replace_string.encode("ascii")
    replacement = replace_bytes + b"\0" * max(
        0, len(search_bytes) - len(replace_bytes)
    )

    with open(memory_path, "rb+") as memory:
        memory.seek(start)
        heap = memory.read(end - start)
        offset = heap.find(search_bytes)
        if offset < 0:
            raise RuntimeError("search string not found in heap")
        memory.seek(start + offset)
        memory.write(replacement)


def main():
    """Validate arguments and perform the requested heap replacement."""
    if len(sys.argv) != 4:
        print("Usage: {} pid search_string replace_string".format(sys.argv[0]))
        return 1

    try:
        replace_heap_string(int(sys.argv[1]), sys.argv[2], sys.argv[3])
    except (OSError, RuntimeError, ValueError) as error:
        print("Error: {}".format(error))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
