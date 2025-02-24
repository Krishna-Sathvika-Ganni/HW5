from app.commands.addcommand import Add 
from app.commands.subtractcommand import Subtract
from app.commands.menucommand import Menu
from app.commands import CommandHandler

class App:
    def __init__(self):
        self.command_handler=CommandHandler()
        self.command_handler.Register_Command("Add", Add())
        self.command_handler.Register_Command("Subtract",Subtract())
        self.command_handler.Register_Command("Menu", Menu(self.command_handler))

    def start(self):
        print("This is the calculator program. Enter Menu to see the commands available")
        self.command_handler.Execute_Command("Menu")
        while True:
            c=input("Enter the command:").strip()
            if c.lower() == "exit":
                print("Exiting..")
                break
            else:
                self.command_handler.Execute_Command(*c.split())
