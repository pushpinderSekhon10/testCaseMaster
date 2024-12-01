<<<<<<< HEAD:fils/samplecode.py
=======
# sample_code.py

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b
>>>>>>> c15e9c9 (Added parameter and return type to json):samplecode.py

class Calculator:
    """A simple calculator class."""

    def multiply(self, a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: int, b: int) -> float:
        """Divide the first number by the second."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    class ScientificCalculator:
        """A subclass of Calculator with advanced operations."""

        def power(self, base: int, exponent: int) -> int:
            """Calculate the power of a base raised to an exponent."""
            return base ** exponent

        def square_root(self, number: float) -> float:
            """Calculate the square root of a number."""
            if number < 0:
                raise ValueError("Cannot calculate the square root of a negative number!")
            return number ** 0.5
