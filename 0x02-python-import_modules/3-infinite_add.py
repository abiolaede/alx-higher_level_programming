#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    res = 0
    ac = 1

    while ac < len(argv):
        res += int(argv[ac])
        ac += 1
    print(res)
