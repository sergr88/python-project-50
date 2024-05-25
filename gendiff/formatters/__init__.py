from gendiff.formatters.plain import format_plainly
from gendiff.formatters.stylish import format_stylishly


def format_difference(difference, output_format):
    match output_format:
        case 'plain':
            return format_plainly(difference)
        case 'stylish':
            return format_stylishly(difference)
        case _:
            return f'Output format "{output_format}" is not implemented'
