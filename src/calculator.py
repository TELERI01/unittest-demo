class Calculator:
    """Simple calculator with a few safe helpers."""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        """Divide a by b. Raises ZeroDivisionError for b == 0."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
