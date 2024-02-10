#!/usr/bin/env python
import json
import yaml


def detect_file_format(file):
    fileExtension = file.split('.')[1].lower
    if fileExtension == 'json':
        return json.load(open(file))
    elif fileExtension == 'yaml' or 'yml':
        return yaml.safe_load(open(file))
