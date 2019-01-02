#!/usr/bin/env python
import functools
import argparse
parser = argparse.ArgumentParser(description='Calculating summ of range')
parser.add_argument('one', type=int, help='first element of range')
parser.add_argument('two', type=int, help='second element of range')
args = parser.parse_args()
counts = range(args.one, args.two)
sum = reduce(lambda x, y: x + y, counts)
print("Summ of range[{:n}, {:n}] is {:n}".format(args.one, args.two, sum))
