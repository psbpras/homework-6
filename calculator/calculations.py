class Calculations:
    """Manages history of calculations."""
    
    history = []

    @classmethod
    def add_calculation(cls, calculation):
        """Adds a new calculation to history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls):
        """Retrieves the most recent calculation."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls):
        """Clears the history of calculations."""
        cls.history.clear()
