from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command

class Add(Command):
    def execute(self, *args):
        if not args:  # If no arguments are provided, prompt for input
            x=input("Enter number 1:")
            y=input("Enter number 2:")
        if len(args) != 2:  # Ensure exactly two arguments
            print("Usage: add <number1> <number2>")
            return

        try:
            x, y = map(Decimal, args)  
            result = Calculator.add(x, y)
            print(f"{x} + {y} = {result}")
        except InvalidOperation:
            print("Enter valid inputs.")
        except Exception as e:
            print(f"{e}")