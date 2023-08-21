#!/usr/bin/python3
"""
Log parser
"""

import sys

total_file_size = 0
status_codes = {}
num_of_lines = 0
possible_status_code = [200, 301, 400, 401, 403, 404, 405, 500]


def stat():
    print(f"File size: {total_file_size}")
    for status, count in sorted(status_codes.items()):
        print(f"{status}: {count}")


try:
    for line in sys.stdin:
        try:
            line = line.split()
            file_size = int(line[-1])
            code = int(line[-2])
            if code in possible_status_code and isinstance(code, int):
                total_file_size += file_size
                num_of_lines += 1
                if code in status_codes:
                    status_codes[code] += 1
                else:
                    status_codes[code] = 1
            if (num_of_lines % 10) == 0:
                stat()
        except ValueError:
            pass
except KeyboardInterrupt:
    sys.exit(0)
finally:
    stat()
