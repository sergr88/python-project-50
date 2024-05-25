from gendiff.formatters.stylish import format_stylishly


def format_difference(difference, output_format):
    match output_format:
        case 'stylish':
            return format_stylishly(difference)
        case _:
            return f'Output format "{output_format}" is not implemented'
