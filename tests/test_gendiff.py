from gendiff.config_diff import compare_config_files
import pytest
import os


def get_path(file, fileToOpenType):
    if fileToOpenType == 'input':
      return os.path.join('tests', 'fixtures', 'input', file)
    elif fileToOpenType == 'expected':
         return os.path.join('tests', 'fixtures', 'expected', file)

@pytest.mark.parametrize(
    "test_input1, test_input2, expected",
    [
        pytest.param(
            'file1.json',
            'file2.json',
            'expected_result.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'expected_result.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.json',
            'expected_result.txt',
            id="flat_mix_file"
        ),
    ],
)
def test_generare_diff(test_input1, test_input2, expected):
    expected_path = get_path(expected, 'expected')
    with open(expected_path, 'r') as file:
        result_data = file.read()
        test_path1 = get_path(test_input1, 'input')
        test_path2 = get_path(test_input2, 'input')
        assert compare_config_files(test_path1, test_path2) == result_data
