from gendiff.gendiff import generate_diff


def test_main():
    with open('./tests/fixtures/result.txt', 'r') as input_file:
        assert generate_diff(
            './tests/fixtures/input1.json',
            './tests/fixtures/input2.json'
        ) == input_file.read()
