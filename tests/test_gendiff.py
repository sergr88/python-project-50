import os.path

from gendiff import generate_diff

BASE_PATH = os.path.join('tests', 'fixtures')


def test_plain_json():
    with open(os.path.join(BASE_PATH, 'flat_result.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'flat_input1.json'),
            os.path.join(BASE_PATH, 'flat_input2.json'))
        assert difference == input_file.read()


def test_plain_yaml():
    with open(os.path.join(BASE_PATH, 'flat_result.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'flat_input1.yaml'),
            os.path.join(BASE_PATH, 'flat_input2.yaml'))
        assert difference == input_file.read()


def test_nested_json():
    with open(os.path.join(BASE_PATH, 'nested_result.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'nested_input1.json'),
            os.path.join(BASE_PATH, 'nested_input2.json'))
        assert difference == input_file.read()


def test_nested_yaml():
    with open(os.path.join(BASE_PATH, 'nested_result.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'nested_input1.yaml'),
            os.path.join(BASE_PATH, 'nested_input2.yaml'))
        assert difference == input_file.read()
