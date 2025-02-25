import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.load_plugins()  # Automatically load plugins

    def load_plugins(self):
        # Dynamically load all plugins from the 'app.plugins' package
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if not is_pkg:  # Only load files (not directories)
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        # Register plugin class (e.g., Add, Subtract, etc.)
                        self.command_handler.Register_Command(item_name.lower(), item(self.command_handler))

    def start(self):
        print("Welcome to the calculator program! Type 'menu' to see available commands, or 'exit' to quit.")
        self.command_handler.Execute_Command("menu")
        while True:
            c = input("Enter the command: ").strip().lower()
            if c == "exit":
                print("Exiting..")
                break
            else:
                parts = user_input.split()
                command_name = parts[0]  # First word is the command
                args = parts[1:]
                self.command_handler.Execute_Command(c)
