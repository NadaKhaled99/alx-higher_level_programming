#!/usr/bin/python3
'''for log parsing script'''
import sys

if __name__ == "__main__":
    ssize = [0]
    code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''Check for regexp match in line'''
        try:
            lines = lines[:-1]
            words = lines.split(" ")
            ssize[0] += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except:
            pass

    def print_stats():
        '''Print accumulated statistics'''
        print("File size: {}".format(ssize[0]))
        for k in sorted(codes.keys()):
            if codes[k]:
                print("{}: {}".format(k, codes[k]))
    j = 1
    try:
        for lines in sys.stdin:
            check_match(lines)
            if j % 10 == 0:
                print_stats()
            j += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
