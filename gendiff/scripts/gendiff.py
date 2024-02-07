#!/usr/bin/env python
import json
from gendiff.cli import parse


def main():
    args = parse()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def format_line(key, value, prefix=" "):
    formatted_value = format_value(value)
    return f"{prefix} {key}: {formatted_value}"


def handle_key(key, file1, file2):
    val1 = file1.get(key, "DNE")
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
