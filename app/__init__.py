import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    def __init__(self, command=None):
        if command is None:
            command= CommandHandler()
        self.command_handler=command
        self.load_plugins()  # Automatically load plugins

    def load_plugins(self):
        """Dynamically load all plugins from the `app/plugins` directory."""
        plugins_package = "app.plugins"
        for _, plugin_name, _ in pkgutil.iter_modules([plugins_package.replace(".", "/")]):
            try:
                plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                        init_signature = inspect.signature(item.__init__)
                        if len(init_signature.parameters) > 1:
                            self.command_handler.register_command(plugin_name.replace("_command", ""), item(self.command_handler))
                        else:
                            self.command_handler.register_command(plugin_name.replace("_command", ""), item())
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
                    break
        
                user_input_split = c.split()
                command_name = user_input_split[0]
                args = user_input_split[1:]
            
                if not self.command_handler.Execute_Command(command_name, *args):
                    print(f"{command_name} : Command not found")
            except Exception as e:
                print(f"And error occured: {e}")
