# sample_code.py

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract the second number from the first."""
    return a - b

class Calculator:
    """A simple calculator class."""

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide the first number by the second."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
