from operator import itemgetter

from gendiff.parse_files import parse_files


def replaced_bool(value):
    return str(value).lower() if isinstance(value, bool) else value


def generate_diff(file_path1, file_path2):
    properties1, properties2 = parse_files(file_path1, file_path2)

    diff1 = [
        (' ' if value == properties2.get(key) else '-', key, value)
        for key, value in properties1.items()
    ]
    diff2 = [
        ('+', key, value)
        for key, value in properties2.items()
        if value != properties1.get(key)
    ]
    difference = sorted(diff1 + diff2, key=itemgetter(1))

    lines = [
        f'  {prefix} {key}: {replaced_bool(value)}'
        for prefix, key, value
        in difference
    ]
    return '\n'.join(['{', *lines, '}'])
