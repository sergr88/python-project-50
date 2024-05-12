import os.path

from gendiff import generate_diff

BASE_PATH = os.path.join('tests', 'fixtures')


def test_flat_json_stylish_format():
    with open(os.path.join(BASE_PATH, 'flat_stylish_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'flat_in1.json'),
            os.path.join(BASE_PATH, 'flat_in2.json'),
            'stylish')
        assert difference == input_file.read()


def test_flat_json_plain_format():
    with open(os.path.join(BASE_PATH, 'flat_plain_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'flat_in1.json'),
            os.path.join(BASE_PATH, 'flat_in2.json'),
            'plain')
        assert difference == input_file.read()


def test_flat_yaml_stylish_format():
    with open(os.path.join(BASE_PATH, 'flat_stylish_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'flat_in1.yaml'),
            os.path.join(BASE_PATH, 'flat_in2.yaml'),
            'stylish')
        assert difference == input_file.read()


def test_flat_yaml_plain_format():
    with open(os.path.join(BASE_PATH, 'flat_plain_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'flat_in1.yaml'),
            os.path.join(BASE_PATH, 'flat_in2.yaml'),
            'plain')
        assert difference == input_file.read()


def test_nested_json_stylish_format():
    with open(os.path.join(BASE_PATH, 'nested_stylish_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'nested_in1.json'),
            os.path.join(BASE_PATH, 'nested_in2.json'),
            'stylish')
        assert difference == input_file.read()


def test_nested_json_plain_format():
    with open(os.path.join(BASE_PATH, 'nested_plain_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'nested_in1.json'),
            os.path.join(BASE_PATH, 'nested_in2.json'),
            'plain')
        assert difference == input_file.read()


def test_nested_yaml_stylish_format():
    with open(os.path.join(BASE_PATH, 'nested_stylish_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'nested_in1.yaml'),
            os.path.join(BASE_PATH, 'nested_in2.yaml'),
            'stylish')
        assert difference == input_file.read()


def test_nested_yaml_plain_format():
    with open(os.path.join(BASE_PATH, 'nested_plain_out.txt')) as input_file:
        difference = generate_diff(
            os.path.join(BASE_PATH, 'nested_in1.yaml'),
            os.path.join(BASE_PATH, 'nested_in2.yaml'),
            'plain')
        assert difference == input_file.read()
