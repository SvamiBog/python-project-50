#!/usr/bin/env python
FORMATS = ('yaml', 'yml', 'json')


def detect_file_format(file_path):
    extension = file_path.split('.')[-1]
    if extension in FORMATS:
        with open(file_path) as f:
            data = f.read()
            return data, extension
