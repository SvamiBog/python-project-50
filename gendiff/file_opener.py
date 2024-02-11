#!/usr/bin/env python
import json
import yaml


def detect_file_format(file_path):
    fileExtension = file_path.split('.')[-1]
    if fileExtension == 'json':
        return json.load(open(file_path))
    elif fileExtension == 'yaml' or 'yml':
        return yaml.safe_load(open(file_path))
