import json


def replace_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    json1 = json.load(open(file_path1))
    json2 = json.load(open(file_path2))

    items = []
    for key, value1 in json1.items():
        if key in json2:
            value2 = json2[key]
            if value1 == value2:
                items.append((key, 0, value1))
            else:
                items.append((key, 1, value1))
                items.append((key, 2, value2))
            del json2[key]
        else:
            items.append((key, 1, value1))

    for key, value2 in json2.items():
        items.append((key, 2, value2))

    items.sort()

    replaces = {1: '-', 2: '+', 0: ' '}
    lines = [
        f'  {replaces[place]} {key}: {replace_value(value)}'
        for key, place, value
        in items
    ]
    return '{\n' + '\n'.join(lines) + '\n}\n'
