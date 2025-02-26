import inspect
import pkgutil
import importlib
from app.commands import CommandHandler, Command
class App:
    def __init__(self, command=None):
        if command is None:
            command = CommandHandler()
        self.command_handler = command
        self.load_plugins()  # Automatically load plugins

    def load_plugins(self):
        '''Dynamically loading the plugins'''
        plugins_package = "app.plugins"  
        for _, plugin_name, _ in pkgutil.iter_modules([plugins_package.replace(".","/")]):  
            try:
                plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        init_signature=inspect.signature(item.__init__)
                        if len(init_signature.parameters)>1:
                            if plugin_name.replace("_command", "") not in self.command_handler.commands:
                                self.command_handler.Register_Command(plugin_name.replace("command", "").strip("_"), item(self.command_handler))
                        else:
                            if plugin_name.replace("_command", "") not in self.command_handler.commands:
                                self.command_handler.Register_Command(plugin_name.replace("command", "").strip("_"), item())
            except Exception as e:
                print(f"Failed to load plugin {plugin_name}: {e}")

    def start(self):
        print("Welcome to the calculator program! Type 'menu' to see available commands, or 'exit' to quit.")
        self.command_handler.Execute_Command("menu")
        while True:
            try:
                c = input("Enter the command: ").strip().lower()
                if c == "exit":
                    raise SystemExit("Exiting..")
                
                user_input_split = c.split()
                command_name = user_input_split[0]
                args = user_input_split[1:]

                command_name=command_name.lower()
                if not self.command_handler.Execute_Command(command_name, *args):
                    print(f"Error: '{command_name}' is not a recognized command")
            except Exception as e:
                print(f"An error occurred: {e}")

