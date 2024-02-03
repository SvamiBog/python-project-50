#!/usr/bin/env python
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='stylish'
        )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(link_file1, link_file2):
    file1 = json.load(open(link_file1))
    file2 = json.load(open(link_file2))

    keys = sorted(set(file1) | set(file2))
    lines = []

    for key in keys:
        val1 = file1.get(key)
        val2 = file2.get(key)

        if val1 == val2:
            lines.append(f"  {key}: {val1}")
        else:
            if key in file1:
                lines.append(f"- {key}: {val1}")
            if key in file2:
                lines.append(f"+ {key}: {val2}")

    return "{\n" + "\n".join(lines) + "\n}"


if __name__ == "__main__":
    main()
