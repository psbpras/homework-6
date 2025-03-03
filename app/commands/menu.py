class MenuCommand:
    """Displays available commands"""
    @staticmethod
    def execute(handler):
        return f"Available commands: {', '.join(handler.get_available_commands())}"
