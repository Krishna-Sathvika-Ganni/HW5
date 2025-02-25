'''This is the test_command file'''

from unittest.mock import patch
from app.commands.addcommand import Add
from app.commands.subtractcommand import Subtract
from app.commands.multiplycommand import Multiply
from app.commands.dividecommand import Divide

# Testing the AddCommand
def test_add_command(capfd):
    """Test the Add command."""
    command = Add()
    command.execute('5', '3')
    out, _ = capfd.readouterr()
    assert "Result: 5 + 3 = 8" in out, "AddCommand should add two numbers correctly"

# Testing the SubtractCommand
def test_subtract_command(capfd):
    """Test the Subtract command."""
    command = Subtract()
    command.execute('5', '3')
    out, _ = capfd.readouterr()
    assert "Result: 5 - 3 = 2" in out, "SubtractCommand should subtract two numbers correctly"

# Testing the MultiplyCommand
def test_multiply_command(capfd):
    """Test the Multiply command."""
    command = Multiply()
    command.execute('5', '3')
    out, _ = capfd.readouterr()
    assert "Result: 5 × 3 = 15" in out, "MultiplyCommand should multiply two numbers correctly"

# Testing the DivideCommand
def test_divide_command(capfd):
    """Test the Divide command."""
    command = Divide()
    command.execute('6', '2')
    out, _ = capfd.readouterr()
    assert "Result: 6 ÷ 2 = 3" in out, "DivideCommand should divide two numbers correctly"

# Testing divide by zero in the DivideCommand
def test_divide_by_zero(capfd):
    """Test Divide command when dividing by zero."""
    command = Divide()
    command.execute('5', '0')
    out, _ = capfd.readouterr()
    assert "Error: Division by zero is not allowed" in out, "DivideCommand should handle division by zero correctly"

# Testing invalid arguments count for AddCommand
def test_add_invalid_args_count(capfd):
    """Test Add command with wrong number of arguments."""
    command = Add()
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Usage: add <number1> <number2>" in out, "AddCommand should prompt correct usage message for invalid arguments count"

# Testing invalid number inputs for AddCommand
def test_add_invalid_numbers(capfd):
    """Test Add command with invalid number inputs."""
    command = Add()
    command.execute("abc", "3")
    out, _ = capfd.readouterr()
    assert "Invalid input. Please enter valid numbers." in out, "AddCommand should handle invalid number inputs correctly"

# Testing general error handling in AddCommand
def test_add_general_error(capfd):
    """Test Add command when a general error occurs."""
    with patch('app.calculator.Calculation.add', side_effect=ValueError("Test error")):
        command = Add()
        command.execute("5", "3")
        out, _ = capfd.readouterr()
        assert "Error: Test error" in out, "AddCommand should handle and display general errors"

# Testing invalid arguments count for SubtractCommand
def test_subtract_invalid_args_count(capfd):
    """Test Subtract command with wrong number of arguments."""
    command = Subtract()
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Usage: subtract <number1> <number2>" in out, "SubtractCommand should prompt correct usage message for invalid arguments count"

# Testing invalid number inputs for SubtractCommand
def test_subtract_invalid_numbers(capfd):
    """Test Subtract command with invalid number inputs."""
    command = Subtract()
    command.execute("abc", "3")
    out, _ = capfd.readouterr()
    assert "Invalid input. Please enter valid numbers." in out, "SubtractCommand should handle invalid number inputs correctly"

# Testing general error handling in SubtractCommand
def test_subtract_general_error(capfd):
    """Test Subtract command when a general error occurs."""
    with patch('app.calculator.Calculation.subtract', side_effect=ValueError("Test error")):
        command = Subtract()
        command.execute("5", "3")
        out, _ = capfd.readouterr()
        assert "Error: Test error" in out, "SubtractCommand should handle and display general errors"

# Testing invalid arguments count for MultiplyCommand
def test_multiply_invalid_args_count(capfd):
    """Test Multiply command with wrong number of arguments."""
    command = Multiply()
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Usage: multiply <number1> <number2>" in out, "MultiplyCommand should prompt correct usage message for invalid arguments count"

# Testing invalid number inputs for MultiplyCommand
def test_multiply_invalid_numbers(capfd):
    """Test Multiply command with invalid number inputs."""
    command = Multiply()
    command.execute("abc", "3")
    out, _ = capfd.readouterr()
    assert "Invalid input. Please enter valid numbers." in out, "MultiplyCommand should handle invalid number inputs correctly"

# Testing general error handling in MultiplyCommand
def test_multiply_general_error(capfd):
    """Test Multiply command when a general error occurs."""
    with patch('app.calculator.Calculation.multiply', side_effect=ValueError("Test error")):
        command = Multiply()
        command.execute("5", "3")
        out, _ = capfd.readouterr()
        assert "Error: Test error" in out, "MultiplyCommand should handle and display general errors"

# Testing invalid arguments count for DivideCommand
def test_divide_invalid_args_count(capfd):
    """Test Divide command with wrong number of arguments."""
    command = Divide()
    command.execute("5")
    out, _ = capfd.readouterr()
    assert "Usage: divide <number1> <number2>" in out, "DivideCommand should prompt correct usage message for invalid arguments count"

# Testing invalid number inputs for DivideCommand
def test_divide_invalid_numbers(capfd):
    """Test Divide command with invalid number inputs."""
    command = Divide()
    command.execute("abc", "3")
    out, _ = capfd.readouterr()
    assert "Invalid input. Please enter valid numbers." in out, "DivideCommand should handle invalid number inputs correctly"

# Testing general error handling in DivideCommand
def test_divide_general_error(capfd):
    """Test Divide command when a general error occurs."""
    with patch('app.calculator.Calculation.divide', side_effect=ValueError("Test error")):
        command = Divide()
        command.execute("5", "3")
        out, _ = capfd.readouterr()
        assert "Error: Test error" in out, "DivideCommand should handle and display general errors"
