#!/usr/bin/env python
import json
import yaml


def parse(data, format):
    if format == 'json':
        return json.loads(data)
    elif format == 'yaml' or 'yml':
        return yaml.safe_load(data)
