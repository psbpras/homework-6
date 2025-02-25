from app.command_handler import MultiplyCommand

def register_command(plugins):
    plugins["multiply"] = MultiplyCommand
