#!/usr/bin/env python
from gendiff.file_opener import detect_file_format


def compare_config_files(file_path1, file_path2):
    file1 = detect_file_format(file_path1)
    file2 = detect_file_format(file_path2)
    keys = sorted(set(file1) | set(file2))
    lines = [compare_and_format(key, file1, file2) for key in keys]
    return "{\n" + "\n".join(lines) + "\n}"


def compare_and_format(key, file1, file2):
    val1, val2 = file1.get(key, "DNE"), file2.get(key, "DNE")
    if val1 == val2:
        return format_line(key, val1)
    lines = []
    if val1 != "DNE":
        lines.append(format_line(key, val1, "-"))
    if val2 != "DNE":
        lines.append(format_line(key, val2, "+"))
    return "\n".join(lines)


def format_line(key, value, prefix=" "):
    value = str(value).lower() if isinstance(value, bool) else value
    return f"{prefix} {key}: {value}"
