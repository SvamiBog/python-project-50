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

def build_plain_iter(diff: dict, path="") -> str:
    lines = []
    for node in diff:
        property_path = f"{path}{node['key']}"

        if node['operation'] == 'add':
            value = to_str(node['new'])
            lines.append(f"Property '{property_path}' was added with value: {value}")

        elif node['operation'] == 'removed':
            lines.append(f"Property '{property_path}' was removed")

        elif node['operation'] == 'nested':
            nested_value = build_plain_iter(node['value'], f"{property_path}.")
            if nested_value:
                lines.append(nested_value)

        elif node['operation'] == 'changed':
            old_value = to_str(node['old'])
            new_value = to_str(node['new'])
            lines.append(f"Property '{property_path}' was updated. From {old_value} to {new_value}")

    return '\n'.join(lines)

def render_plain(diff: dict) -> str:
    return build_plain_iter(diff)
