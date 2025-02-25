import pytest
from app import App
from app.commands.addcommand import Add
from app.commands.subtractcommand import Subtract
from app.commands.multiplycommand import Multiply
from app.commands.dividecommand import Divide
from app.commands.menucommand import Menu

def test_add_command(capfd):
    command=Add()
    command.execute('2','3')
    out, _=capfd.readouterr()
    assert "2 + 3 = 5" in out, "AddCommand should add two numbers"

def test_subtract_command(capfd):
    command=Subtract()
    command.execute('3','2')
    out, _=capfd.readouterr()
    assert "3 - 2 = 1" in out, "SubtractCommand should subtract two numbers"

def test_multiply_command(capfd):
    command=Multiply()
    command.execute('2','3')
    out, _=capfd.readouterr()
    assert "2 * 3 = 6" in out, "MultiplyCommand should multiply two numbers"

def test_divide_command(capfd):
    command=Divide()
    command.execute('4','2')
    out, _=capfd.readouterr()
    assert "4 / 2 = 2" in out, "DivideCommand should divide two numbers"

def test_divide_by_zero(capfd):
    command=Divide()
    command.execute('2','0')
    out, _=capfd.readouterr()
    assert "Division by zero cannot happen" in out, "DivideCommand should handle division by zero"

def test_menu_command(capfd):
    command_handler={}
    command=Menu(command_handler)
    command.execute()
    out, _=capfd.readouterr()
    assert "Available commands:" in out, "MenuCommand should display available commands"


