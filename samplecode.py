
def add(a: int, b: int):
    """Add two numbers."""
    # return a + b
    return a + b

def subtract(a: int, b: int):
    """Subtract the second number from the first."""
    return a - b

class Calculator:
    """A simple calculator class."""

    def multiply(self, a: int, b: int):
        """Multiply two numbers."""
        return a * b

    def divide(self, a: int, b: int):
        """Divide the first number by the second."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b