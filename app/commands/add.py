from app.command_handler import AddCommand

def register_command(plugins):
    plugins["add"] = AddCommand
