#!/usr/bin/python3
import sys
import signal
"""script reads metrics from stdin and prints statistics"""


def stats_output(stats: dict, size: int) -> None:
    """prints metric stats"""
    print("File size {:d}".format(size))
    for i, j in sorted(stats.items()):
        if j:
            print("{}: {}".format(i, j))


def main() -> None:
    """reads metrics from stdin"""
    size, cnt = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in codes}

    try:
        for line in sys.stdin:
            cnt += 1
            info = line.split()
            try:
                status_code = info[-2]
                if status_code in stats:
                    stats[status_code] += 1
            try:
                size += int(info[-1])
            except BaseException:
                pass
            if cnt % 10 == 0:
                stats_output(stats, size)
        stats_output(stats, size)
    except KeyboardInterrupt:
        stats_output(stats, size)
        raise


if __name__ == '__main__':
    main()
