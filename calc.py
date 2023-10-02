#!/usr/bin/env python

import argparse


def add(numbers):
    return sum(numbers)


def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def main():

    parser = argparse.ArgumentParser(description="A simple calculator with add and multiply commands.")    

    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser('add', help='Adds the provided numbers.')
    add_parser.add_argument('numbers', type=int, nargs='+', help='The numbers to add.')
    add_parser.set_defaults(func=add)

    multiply_parser = subparsers.add_parser('multiply', help='Multiplies the provided numbers.')
    multiply_parser.add_argument('numbers', type=int, nargs='+', help='The numbers to multiply.')
    multiply_parser.set_defaults(func=multiply)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        result = args.func(args.numbers)
        print(result)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
