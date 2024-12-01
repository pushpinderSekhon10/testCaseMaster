import unittest
import arithmetic

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        # TODO: Implement test for add
        # Expected return value of type Any
        result = arithmetic.add({'name': 'a', 'type': 'Any'}=None, {'name': 'b', 'type': 'Any'}=None)
        self.assertEqual(result, None)  # Replace None with the expected result

    def test_subtract(self):
        # TODO: Implement test for subtract
        # Expected return value of type Any
        result = arithmetic.subtract({'name': 'a', 'type': 'Any'}=None, {'name': 'b', 'type': 'Any'}=None)
        self.assertEqual(result, None)  # Replace None with the expected result


if __name__ == "__main__":
    unittest.main()
