#!/usr/bin/env python


def compare_config_files(data1: dict, data2: dict):
    diff = []
    for key in sorted(set(data1) | set(data2)):
        entry = {'key': key}
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                entry.update({
                    'operation': 'same',
                    'value': data1[key]
                })
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                entry.update({
                    'operation': 'nested',
                    'value': compare_config_files(data1[key], data2[key])
                })
            else:
                entry.update({
                    'operation': 'changed',
                    'old': data1.get(key),
                    'new': data2.get(key)
                })
        else:
            if key not in data1:
                entry.update({
                    'operation': 'add',
                    'new': data2[key]
                })
            else:
                entry.update({
                    'operation': 'removed',
                    'old': data1[key]
                })
        diff.append(entry)
    return diff
