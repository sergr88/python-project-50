import json


def parse_files(file_path1, file_path2):
    properties1 = parse_file(file_path1)
    properties2 = parse_file(file_path2)
    return properties1, properties2
