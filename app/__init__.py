import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_plugins()  # Load plugins only once here

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Check if item is a subclass of Command
                            self.command_handler.register_command(plugin_name.lower(), item())  # Lowercase plugin name for consistency
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        print("This is the calculator program. Enter Menu to see the commands available")
        print("Type 'exit' to exit.")
        while True:  # REPL (Read, Evaluate, Print, Loop)
            user_input = input(">>> ").strip().lower()  # Convert to lowercase for easier matching
            self.command_handler.Execute_Command(user_input)
