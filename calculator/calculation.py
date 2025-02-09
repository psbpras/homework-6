class Calculation:
    """Represents a single calculation operation."""
    
    def __init__(self, operation, a: float, b: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = self.perform_calculation()

    def perform_calculation(self) -> float:
        """Executes the stored operation."""
        return self.operation(self.a, self.b)

    def __str__(self) -> str:
        return f"{self.a} {self.operation.__name__} {self.b} = {self.result}"
