import pkgutil
import importlib
import inspect
from app.commands import Command, CommandHandler
from app.plugins import addcommand
from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.dividecommand import Divide
from app.plugins.menucommand import Menu

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.register_core_commands()
        self.load_plugins()  # Load plugins dynamically

    def register_core_commands(self):
        """ Register core commands directly in the app """
        self.command_handler.Register_Command("Add", Add())
        self.command_handler.Register_Command("Subtract", Subtract())
        self.command_handler.Register_Command("Multiply", Multiply())
        self.command_handler.Register_Command("Divide", Divide())
        self.command_handler.Register_Command("Menu", Menu(self.command_handler))
    
    def load_plugins(self):
        '''Dynamically load all plugins from the `app/plugins` directory.'''
        plugins_package = "app.plugins"
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace(".", "/")]):
            if not is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}') 
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command) and item is not Command:
                            self.command_handler.Register_Command(plugin_name.replace("command", ""), item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        """Start the REPL loop for user interaction."""
        print("Welcome to Calculator! Type 'menu' to see available commands, or 'exit' to quit.")
        self.command_handler.Execute_Command("Menu")  # Show available commands at startup

        while True:
            c = input("Enter the command: ").strip()
            if c.lower() == "exit":
                print("Exiting...")
                break
            user_input_split = c.split()
            command_name = user_input_split[0]
            args = user_input_split[1:]
            self.command_handler.Execute_Command(command_name, *args)