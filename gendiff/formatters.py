def replaced_bool(value):
    return str(value).lower() if isinstance(value, bool) else value


def format_stylishly(difference):
    lines = [
        f'  {prefix} {key}: {replaced_bool(value)}'
        for prefix, key, value
        in difference
    ]
    return '\n'.join(['{', *lines, '}'])
