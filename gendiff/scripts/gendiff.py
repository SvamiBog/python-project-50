#!/usr/bin/env python
from gendiff.cli import parse
from gendiff.config_diff import compare_config_files


def main():
    args = parse()
    print(compare_config_files(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
