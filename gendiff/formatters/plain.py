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


def format_node(nodes, parent_path):
    lines = []
    for prefix, key, value in nodes:
        current_path = f'{parent_path}{key}'
        line_prefix = f"Property '{current_path}' was"
        match prefix:
            case ' ':
                if isinstance(value, list):
                    lines.append(format_node(value, f'{current_path}.'))
            case '-':
                is_found, value2 = find_value(nodes, '+', key)
                if is_found:
                    lines.append(f'{line_prefix}'
                                 f' updated. From {format_value(value)}'
                                 f' to {format_value(value2)}')
                else:
                    lines.append(f'{line_prefix} removed')
            case '+':
                is_found, _ = find_value(nodes, '-', key)
                if not is_found:
                    lines.append(f'{line_prefix}'
                                 f' added with value: {format_value(value)}')
    return '\n'.join(lines)


def format_plainly(difference):
    return format_node(difference, '')
