def find_value(nodes, prefix, key):
    reference = (prefix, key)
    values = [node[2] for node in nodes if (node[0], node[1]) == reference]
    return (True, values[0]) if values else (False, None)


def format_value(value):
    match value:
        case None:
            return 'null'
        case bool():
            return str(value).lower()
        case str():
            return f"'{value}'"
        case dict():
            return '[complex value]'
        case _:
            return value


def format_unchanged(value, current_path, parent_path):
    if isinstance(value, list):
        return format_node(value, f'{current_path}.')
    return None


def format_removed(nodes, key, value, line_prefix):
    is_found, value2 = find_value(nodes, '+', key)
    if is_found:
        return (
            f'{line_prefix}'
            f' updated. From {format_value(value)}'
            f' to {format_value(value2)}'
        )
    return f'{line_prefix} removed'


def format_added(nodes, key, value, line_prefix):
    is_found, _ = find_value(nodes, '-', key)
    if not is_found:
        return f'{line_prefix} added with value: {format_value(value)}'
    return None


def format_node(nodes, parent_path):
    lines = []
    for prefix, key, value in nodes:
        current_path = f'{parent_path}{key}'
        line_prefix = f"Property '{current_path}' was"
        match prefix:
            case ' ':
                result = format_unchanged(value, current_path, parent_path)
            case '-':
                result = format_removed(nodes, key, value, line_prefix)
            case '+':
                result = format_added(nodes, key, value, line_prefix)
            case _:
                result = None
        if result is not None:
            lines.append(result)
    return '\n'.join(lines)


def format_plainly(difference):
    return format_node(difference, '')
