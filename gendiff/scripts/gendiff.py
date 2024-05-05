#!/usr/bin/env python3

import argparse

from gendiff import DEFAULT_OUTPUT_FORMAT, generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default=DEFAULT_OUTPUT_FORMAT,
                        help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
