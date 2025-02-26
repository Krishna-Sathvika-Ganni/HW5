import inspect
import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
<<<<<<< HEAD
    '''This is the App class'''
    def __init__(self):
        self.command_handler=CommandHandler()
        self.command_handler.Register_Command("Add", Add())
        self.command_handler.Register_Command("Subtract",Subtract())
        self.command_handler.Register_Command("Multiply", Multiply())
        self.command_handler.Register_Command("Divide", Divide())
        self.command_handler.Register_Command("Menu", Menu(self.command_handler))

    def start(self):
        '''This is the start function'''
        print("This is the calculator program. Enter Menu to see the commands available.")
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
                    # Executes registered commands
                    if command_name in self.command_handler.commands:
                        self.command_handler.Execute_Command(*command_parts)
                    else:
                        print(f"{command_name} : Command not found")
                else:
                    print("Enter command is invalid. Enter a valid command. Type Menu to see the available commands.")

# End of program
=======
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
>>>>>>> Plugins
