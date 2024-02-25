#!/usr/bin/env python
from gendiff.file_reader import detect_file_format
from gendiff.config_diff import compare_config_files
from gendiff.formaters import get_formatter
from gendiff.parser import parse


def generate_diff(
        file1_path: str,
        file2_path: str,
        formater: str = 'stylish'
) -> str:
    data_file1, extension1 = detect_file_format(file1_path)
    data_file2, extension2 = detect_file_format(file2_path)
    parsed_data1 = parse(data_file1, extension1)
    parsed_data2 = parse(data_file2, extension2)
    diff = compare_config_files(parsed_data1, parsed_data2)
    return get_formatter(formater)(diff)
