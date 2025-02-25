class Calculator:
    """Simple calculator to store history and execute operations."""

    def __init__(self):
        self.history = []

    def execute(self, command):
        """Execute a command and store the result in history."""
        try:
            result = command.execute()
            self.history.append((command.__class__.__name__, result))
            return result
        except Exception as e:
            return f"Error: {str(e)}"
