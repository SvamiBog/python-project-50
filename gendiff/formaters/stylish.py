from typing import Any, Dict

DEFAULT_INDENT = 4


def format_dict(value: Dict, depth: int) -> str:
    lines = ["{"]
    for key, nested_value in value.items():
        formatted_value = format_value_as_string(
            nested_value, depth + DEFAULT_INDENT
        )
        lines.append(f"{' ' * depth}    {key}: {formatted_value}")
    lines.append(f"{' ' * depth}}}")
    return "\n".join(lines)


def format_value_as_string(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        return format_dict(value, depth)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def format_line(dictionary: Dict, key: Any, depth: int, sign: str) -> str:
    return (
        f"{' ' * depth}{sign}{dictionary['key']}: "
        f"{format_value_as_string(dictionary[key], depth + DEFAULT_INDENT)}"
    )


def build_stylish_iter(diff: Dict, depth=0) -> str:
    lines = ["{"]
    operation_handlers = {
        "same": lambda node: format_line(node, "value", depth, "    "),
        "add": lambda node: format_line(node, "new", depth, "  + "),
        "removed": lambda node: format_line(node, "old", depth, "  - "),
        "changed": lambda node: (
            format_line(node, "old", depth, "  - ") + "\n"
            + format_line(node, "new", depth, "  + ")
        ),
        "nested": lambda node: (
            f"{' ' * depth}    {node['key']}: "
            f"{build_stylish_iter(node['value'], depth + DEFAULT_INDENT)}"
        )
    }

    for node in diff:
        handler = operation_handlers.get(node["operation"])
        if handler:
            lines.append(handler(node))

    lines.append(f"{' ' * depth}}}")
    return "\n".join(lines)


def render_stylish(diff: Dict) -> str:
    return build_stylish_iter(diff)
