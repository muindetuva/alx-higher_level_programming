#!/usr/bin/python3
"""Read HTTP access logs from standard input and print aggregate metrics."""

import sys


VALID_STATUS_CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_statistics(total_size, status_counts):
    """Print the current total file size and ordered status-code counts."""
    print("File size: {}".format(total_size))
    for status_code in VALID_STATUS_CODES:
        if status_counts[status_code]:
            print("{}: {}".format(status_code, status_counts[status_code]))


def process_line(line, total_size, status_counts):
    """Update metrics from one valid log line and return the new size."""
    parts = line.split()
    if len(parts) < 2:
        return total_size

    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
    except (TypeError, ValueError):
        return total_size

    total_size += file_size
    if status_code in status_counts:
        status_counts[status_code] += 1
    return total_size


def main():
    """Consume standard input and print metrics every ten input lines."""
    total_size = 0
    line_count = 0
    status_counts = {code: 0 for code in VALID_STATUS_CODES}

    try:
        for line in sys.stdin:
            line_count += 1
            total_size = process_line(line, total_size, status_counts)
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
