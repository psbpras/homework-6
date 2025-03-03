from app.command_handler import SubtractCommand

def register_command(plugins):
    plugins["subtract"] = SubtractCommand

