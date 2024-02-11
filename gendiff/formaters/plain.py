from typing import Any, Union


def to_str(value: Any) -> Union[str, int]:
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return value
    return f"'{value}'"


def handle_addition(node, property_path):
    value = to_str(node['new'])
    return f"Property '{property_path}' was added with value: {value}"


def handle_removal(node, property_path):
    return f"Property '{property_path}' was removed"


def handle_nesting(node, property_path):
    nested_value = build_plain_iter(node['value'], f"{property_path}.")
    return nested_value if nested_value else ""


def handle_change(node, property_path):
    old_value = to_str(node['old'])
    new_value = to_str(node['new'])
    return (f"Property '{property_path}' was updated. "
            f"From {old_value} to {new_value}")


def build_plain_iter(diff: dict, path="") -> str:
    lines = []
    for node in diff:
        property_path = f"{path}{node['key']}"
        operation_handlers = {
            'add': handle_addition,
            'removed': handle_removal,
            'nested': handle_nesting,
            'changed': handle_change,
        }
        handler = operation_handlers.get(node['operation'])
        line = handler(node, property_path) if handler else ""
        if line:
            lines.append(line)

    return '\n'.join(lines)


def render_plain(diff: dict) -> str:
    return build_plain_iter(diff)
