from gendiff.config_diff import compare_config_files


def test_flat_json_diff():
    expected_diff = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''

    actual_diff = compare_config_files('file1.json', 'file2.json')

    assert actual_diff == expected_diff


def test_flat_yml_diff():
    expected_diff = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''

    actual_diff = compare_config_files('file1.yml', 'file2.yml')

    assert actual_diff == expected_diff


def test_flat_yaml_diff():
    expected_diff = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''

    actual_diff = compare_config_files('file1.yaml', 'file2.yaml')

    assert actual_diff == expected_diff
