from gendiff.scripts.gendiff import generate_diff


def test_flat_json_diff():
    expected_diff = '''{
- follow: false
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: true
}'''

    actual_diff = generate_diff('file1.json', 'file2.json')

    assert actual_diff == expected_diff
