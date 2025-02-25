from app.commands.addcommand import Add 
from app.commands.subtractcommand import Subtract
from app.commands.multiplycommand import Multiply
from app.commands.dividecommand import Divide
from app.commands.menucommand import Menu
from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler=CommandHandler()
        self.command_handler.Register_Command("Add", Add())
        self.command_handler.Register_Command("Subtract",Subtract())
        self.command_handler.Register_Command("Multiply", Multiply())
        self.command_handler.Register_Command("Divide", Divide())
        self.command_handler.Register_Command("Menu", Menu(self.command_handler))

    def start(self):
        print("This is the calculator program. Enter Menu to see the commands available")
        self.command_handler.Execute_Command("Menu")
        
        while True:
            c=input("Enter the command:").strip()
            if c.lower() == "exit":
                print("Exiting..")
                raise SystemExit
                break
            else:
                command_parts = c.split()
                if command_parts:
                    command_name = command_parts[0]
                    # Execute the command if it's registered
                    if command_name in self.command_handler.commands:
                        self.command_handler.Execute_Command(*command_parts)
                    else:
                        print(f"{command_name} : Command not found")
                else:
                    print("Invalid input. Please enter a command.")
