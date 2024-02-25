#!/usr/bin/env python
import json
import yaml


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    elif extension == 'yaml' or 'yml':
        return yaml.safe_load(data)
