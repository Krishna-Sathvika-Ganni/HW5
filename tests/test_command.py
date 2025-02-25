'''This is test_command file'''
from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.dividecommand import Divide
from app.plugins.menucommand import Menu

# Testing the add command
def test_add_command(capfd):
    """Test the Add command."""
    command = Add()
    command.execute('2', '3')
    out, _ = capfd.readouterr()
    assert "2 + 3 = 5" in out, "AddCommand should add two numbers"

# Testing the subtract command
def test_subtract_command(capfd):
    """Test the Subtract command."""
    command = Subtract()
    command.execute('3', '2')
    out, _ = capfd.readouterr()
    assert "3 - 2 = 1" in out, "SubtractCommand should subtract two numbers"

# Testing multiply command
def test_multiply_command(capfd):
    """Test the Multiply command."""
    command = Multiply()
    command.execute('2', '3')
    out, _ = capfd.readouterr()
    assert "2 x 3 = 6" in out, "MultiplyCommand should multiply two numbers"

# Testing divide command
def test_divide_command(capfd):
    """Test the Divide command."""
    command = Divide()
    command.execute('4', '2')
    out, _ = capfd.readouterr()
    assert "4 / 2 = 2" in out, "DivideCommand should divide two numbers"

# Testing divide by zero
def test_divide_by_zero(capfd):
    """Test the Divide command when dividing by zero."""
    command = Divide()
    command.execute('2', '0')
    out, _ = capfd.readouterr()
    assert "Cannot be divided by zero" in out, "DivideCommand should handle division by zero"

# Testing menu command
def test_menu_command(capfd):
    """Test that the Menu command displays the list of available commands."""
    class MockCommandHandler:
        """Mocked CommandHandler class."""
        def get_registered_commands(self):
            """Return a list of registered commands."""
            return ["Add", "Subtract", "Multiply", "Divide", "Menu"]

    command_handler = MockCommandHandler()
    command = Menu(command_handler)
    command.execute()
    out, _ = capfd.readouterr()
    assert "Commands Available:" in out, "MenuCommand should display the available commands"