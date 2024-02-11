#!/usr/bin/env python


def compare_values(key, value1, value2):
    if value1 == value2:
        return {
            'key': key,
            'operation': 'same',
            'value': value1
        }
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return {
            'key': key,
            'operation': 'nested',
            'value': compare_config_files(value1, value2)
        }
    else:
        return {
            'key': key,
            'operation': 'changed',
            'old': value1,
            'new': value2
        }


def handle_key(key, data1, data2):
    if key in data1 and key in data2:
        return compare_values(key, data1[key], data2[key])
    elif key not in data1:
        return {'key': key, 'operation': 'add', 'new': data2[key]}
    else:
        return {'key': key, 'operation': 'removed', 'old': data1[key]}


def compare_config_files(data1: dict, data2: dict):
    diff = []
    all_keys = sorted(set(data1) | set(data2))

    for key in all_keys:
        diff.append(handle_key(key, data1, data2))

    return diff
