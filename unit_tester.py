import unittest
import importlib
from gpt import run_func
class TestArithmetic(unittest.TestCase):
    def test(self, mod_name, class_name, method_name, expected, *args):
        # Expected return value of type Any
        result = run_func(mod_name, class_name, method_name, expected, *args)
        self.assertEqual(result, expected)  # Replace None with the expected result


if __name__ == "__main__":
    unittest.main()
