class Calculation:
    """Represents a mathematical calculation."""

    def __init__(self, operation, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        self.result = operation(num1, num2)  # Ensure the operation is computed

    def __str__(self):
        """Return a string representation of the calculation."""
        result = self.result
        if isinstance(result, float) and result.is_integer():
            result = int(result)  # Convert to int if it's a whole number
        return f"{self.num1} {self.operation.__name__} {self.num2} = {result}"
