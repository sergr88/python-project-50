def format_value(node, level):
    match node:
        case None:
            return 'null'
        case bool():
            return str(node).lower()
        case list():
            return format_nodes(node, level)
        case dict():
            nodes = [(' ', key, value) for key, value in node.items()]
            return format_nodes(nodes, level)
        case _:
            return node


def format_nodes(nodes, level):
    indent = ' ' * (level * 4)
    lines = []
    for prefix, key, value in nodes:
        formatted_value = format_value(value, level + 1)
        lines.append(f'{indent}  {prefix} {key}: {formatted_value}')
    return '\n'.join(['{', *lines, f'{indent}}}'])


def format_stylishly(difference):
    return format_nodes(difference, 0)
