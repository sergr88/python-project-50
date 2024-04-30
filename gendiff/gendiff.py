import json
from operator import itemgetter


def replaced_bool(value):
    return str(value).lower() if isinstance(value, bool) else value


def generate_diff(file_path1, file_path2):
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))

    diff1 = [
        (' ' if value == json2.get(key) else '-', key, value)
        for key, value in json1.items()
    ]
    diff2 = [
        ('+', key, value)
        for key, value in json2.items()
        if value != json1.get(key)
    ]
    difference = sorted(diff1 + diff2, key=itemgetter(1))

    lines = [
        f'  {prefix} {key}: {replaced_bool(value)}'
        for prefix, key, value
        in difference
    ]
    return '\n'.join(['{', *lines, '}'])
