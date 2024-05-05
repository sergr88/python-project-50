def format_stylishly(difference):
    def format_node(node, level):
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
            formatted_node = format_node(value, level + 1)
            lines.append(f'{indent}  {prefix} {key}: {formatted_node}')
        return '\n'.join(['{', *lines, f'{indent}}}'])

    return format_nodes(difference, 0)


def format_difference(difference, output_format):
    match output_format:
        case 'stylish':
            return format_stylishly(difference)
        case _:
            return f'Output format "{output_format}" is not implemented'
