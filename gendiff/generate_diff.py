#!/usr/bin/env python
from gendiff.file_opener import detect_file_format
from gendiff.config_diff import compare_config_files
from gendiff.formaters import get_formatter


def generate_diff(
        file1_path: str,
        file2_path: str,
        formater: str = 'stylish'
) -> str:
    date_file1 = detect_file_format(file1_path)
    date_file2 = detect_file_format(file2_path)
    diff = compare_config_files(date_file1, date_file2)
    return get_formatter(formater)(diff)
