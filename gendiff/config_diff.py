#!/usr/bin/env python


def compare_config_files(data1: dict, data2: dict):
    diff = []
    all_keys = sorted(set(data1) | set(data2))

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(
                    {'key': key, 'operation': 'same', 'value': data1[key]}
                )
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                diff.append(
                    {'key': key,
                     'operation': 'nested',
                     'value': compare_config_files(data1[key], data2[key])}
                )
            else:
                diff.append(
                    {'key': key,
                     'operation': 'changed',
                     'old': data1[key], 'new': data2[key]}
                )
        elif key not in data1:
            diff.append({'key': key, 'operation': 'add', 'new': data2[key]})
        else:  # key not in data2
            diff.append({'key': key, 'operation': 'removed', 'old': data1[key]})

    return diff
