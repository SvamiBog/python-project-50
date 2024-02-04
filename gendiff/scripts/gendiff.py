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


def format_line(key, value, prefix=" "):
    return f"{prefix} {key}: {value}"


def handle_key(key, file1, file2):
    val1 = file1.get(key, "DNE")  # DNE - Does Not Exist
    val2 = file2.get(key, "DNE")

    if val1 == val2:
        return format_line(key, val1)
    lines = []
    if val1 != "DNE":
        lines.append(format_line(key, val1, "-"))
    if val2 != "DNE":
        lines.append(format_line(key, val2, "+"))
    return "\n".join(lines)


def generate_diff(link_file1, link_file2):
    file1 = json.load(open(link_file1))
    file2 = json.load(open(link_file2))

    keys = sorted(set(file1) | set(file2))
    lines = [handle_key(key, file1, file2) for key in keys]

    return "{\n" + "\n".join(lines) + "\n}"


if __name__ == "__main__":
    main()
