#!/usr/bin/env python
from gendiff.generate_diff import generate_diff
import pytest
import os


def get_path(file, fileToOpenType):
    if fileToOpenType == 'input':
        return os.path.join('tests', 'fixtures', 'input', file)
    elif fileToOpenType == 'expected':
        return os.path.join('tests', 'fixtures', 'expected', file)


@pytest.mark.parametrize(
    "test_input1, test_input2, formater, expected",
    [
        pytest.param(
            'file1.json',
            'file2.json',
            'stylish',
            'expected_result_stylish.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'stylish',
            'expected_result_stylish.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.json',
            'stylish',
            'expected_result_stylish.txt',
            id="flat_mix_file"
        ),
        pytest.param(
            'file1_big.json',
            'file2_big.json',
            'stylish',
            'expected_result_big_stylish.txt',
            id="big_json_file"
        ),
        pytest.param(
            'file1_big.yml',
            'file2_big.yml',
            'stylish',
            'expected_result_big_stylish.txt',
            id="big_yml_file"
        ),
        pytest.param(
            'file1_big.yaml',
            'file2_big.yaml',
            'stylish',
            'expected_result_big_stylish.txt',
            id="big_yaml_file"
        ),
        pytest.param(
            'file1_big.json',
            'file2_big.yml',
            'stylish',
            'expected_result_big_stylish.txt',
            id="big_stylich_file_mix"
        ),
        pytest.param(
            'file1_big.yaml',
            'file2_big.yaml',
            'plain',
            'expected_result_big_plain.txt',
            id="big_plain_file"
        ),
        pytest.param(
            'file1_big.yaml',
            'file2_big.json',
            'stylish',
            'expected_result_big_stylish.txt',
            id="big_plain_file_mix"
        ),
        pytest.param(
            'file1_big.json',
            'file2_big.json',
            'json',
            'expected_result_big_json.txt',
            id="big_json_file"
        ),
    ],
)
def test_generare_diff(test_input1, test_input2, formater, expected):
    expected_path = get_path(expected, 'expected')
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_path(test_input1, 'input')
        test_path2 = get_path(test_input2, 'input')
        assert generate_diff(test_path1, test_path2, formater) == result_data
