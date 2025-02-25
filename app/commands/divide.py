from app.command_handler import DivideCommand

def register_command(plugins):
    plugins["divide"] = DivideCommand
