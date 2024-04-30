import json
import os.path

import yaml


def parse_file(file_path):
    _, extension = os.path.splitext(file_path)
    match extension.lower():
        case '.json':
            return json.load(open(file_path))
        case '.yaml' | '.yml':
            return yaml.load(open(file_path), Loader=yaml.Loader)
        case _:
            return ''


def parse_files(file_path1, file_path2):
    properties1 = parse_file(file_path1)
    properties2 = parse_file(file_path2)
    return properties1, properties2
