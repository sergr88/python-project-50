import json
import os.path

import yaml


def parse_file(file_path):
    _, extension = os.path.splitext(file_path)
    match extension.lower():
        case '.json':
            return json.load(open(file_path, encoding='utf-8'))
        case '.yaml' | '.yml':
            return yaml.load(
                open(file_path, encoding='utf-8'),
                Loader=yaml.Loader,
            )
        case _:
            return ''


def parse_files(file_path1, file_path2):
    properties1 = parse_file(file_path1)
    properties2 = parse_file(file_path2)
    return properties1, properties2
