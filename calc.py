#!/usr/bin/env python

import argparse


def add(numbers):
    return sum(numbers)


def multiply(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def divide(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required for division.")
    if len(numbers) > 2:
        raise ValueError("Cannot divide with more than two numbers.")
    if numbers[1] == 0:
        raise ValueError("Division by zero is not allowed.")

    return numbers[0] / numbers[1]


def main():

    parser = argparse.ArgumentParser(description="A simple calculator with add and multiply commands.")    

    subparsers = parser.add_subparsers()

    parser.add_argument('-d', '--debug', action='store_true', help='Run in debug mode')

    add_parser = subparsers.add_parser('add', help='Adds the provided numbers.')
    add_parser.add_argument('numbers', type=int, nargs='+', help='The numbers to add.')
    add_parser.set_defaults(func=add)

    multiply_parser = subparsers.add_parser('multiply', help='Multiplies the provided numbers.')
    multiply_parser.add_argument('numbers', type=int, nargs='+', help='The numbers to multiply.')
    multiply_parser.set_defaults(func=multiply)

    divide_parser = subparsers.add_parser('divide', help='Divides the first number by the second.')
    divide_parser.add_argument('numbers', type=float, nargs=2, help='The numbers to divide, given as two numbers where the first is divided by the second.')
    divide_parser.set_defaults(func=divide)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        if args.debug:
            print(f'[DEBUG] Will execute: {args.func}')
        result = args.func(args.numbers)
        print(result)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
