from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command

class add(Command):
    def execute(self, *args):
        if not args:  # If no arguments are provided, prompt for input
            args = input("Enter two numbers separated by space: ").split()
        if len(args) != 2:  # Ensure exactly two arguments
            print("Usage: add <number1> <number2>")
            return

        try:
            num1, num2 = map(Decimal, args)  # Convert input to decimals
            result = Calculator.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        except InvalidOperation:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")