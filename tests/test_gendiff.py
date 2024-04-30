import os.path

from gendiff.gendiff import generate_diff

BASE_PATH = os.path.join('tests', 'fixtures')


def test_plain_json():
    with open(os.path.join(BASE_PATH, 'result.txt')) as input_file:
        assert generate_diff(
            os.path.join(BASE_PATH, 'flat_input1.json'),
            os.path.join(BASE_PATH, 'flat_input2.json')
        ) == input_file.read()
