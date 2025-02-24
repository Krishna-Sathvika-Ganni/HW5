'''Test main file'''
import pytest
from main import calculate_and_print

@pytest.mark.parametrize("x_string, y_string, operation_string, expected_string", [
    ("3", "3", 'add', "The result of 3 add 3 is equal to 6"),
    ("4", "1", 'subtract', "The result of 4 subtract 1 is equal to 3"),
    ("2", "2", 'multiply', "The result of 2 multiply 2 is equal to 4"),
    ("10", "5", 'divide', "The result of 10 divide 5 is equal to 2"),
    ("4", "0", 'divide', "An error occurred: Cannot be divided by Zero"),
    ("6", "3", 'unknown', "Unknown operation: unknown"),
    ("x", "3", 'add', "Invalid number input: x or 3 is not a valid number."),
    ("5", "y", 'subtract', "Invalid number input: 5 or y is not a valid number.")
])
def test_calculate_and_print(x_string, y_string, operation_string,expected_string, capsys):
    '''defining test_calculate_and_print'''
    calculate_and_print(x_string, y_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string