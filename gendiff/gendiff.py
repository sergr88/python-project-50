from operator import itemgetter

from gendiff.formatters import format_difference
from gendiff.parsers import parse_files

DEFAULT_OUTPUT_FORMAT = 'stylish'


def is_dict(value):
    return isinstance(value, dict)


def calculate_difference(properties1, properties2):
    diff1 = []
    for key, value1 in properties1.items():
        value2 = properties2.get(key)
        if is_dict(value1) and is_dict(value2):
            node_difference = ' ', key, calculate_difference(value1, value2)
        elif value1 == value2:
            node_difference = ' ', key, value1
        else:
            node_difference = '-', key, value1
        diff1.append(node_difference)

    diff2 = []
    for key, value2 in properties2.items():
        value1 = properties1.get(key)
        if value2 == value1 or (is_dict(value2) and is_dict(value1)):
            continue
        diff2.append(('+', key, value2))

    return sorted(diff1 + diff2, key=itemgetter(1))


def generate_diff(file_path1, file_path2, output_format=DEFAULT_OUTPUT_FORMAT):
    properties1, properties2 = parse_files(file_path1, file_path2)
    difference = calculate_difference(properties1, properties2)
    formatted_difference = format_difference(difference, output_format)
    return formatted_difference
