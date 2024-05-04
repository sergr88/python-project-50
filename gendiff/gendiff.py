from operator import itemgetter

from gendiff.formatters import format_stylishly
from gendiff.parsers import parse_files


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

    return format_stylishly(difference)
