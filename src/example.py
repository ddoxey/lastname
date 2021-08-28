#!/usr/bin/env python3

import sys
from pprint import pprint
from lastname import LastName


def run(name):

    ln = LastName()
    x = ln.lookup(name)
    pprint(x)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('USAGE: {sys.argv[0]} <name>', file=sys.stderr)
    elif len(sys.argv) == 2:
        run(sys.argv[1])
