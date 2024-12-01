import unittest
import samplecode

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        # TODO: Implement test for add
        # Expected return value of type Any
        result = samplecode.add(4, 3)
        self.assertEqual(result, 7)  # Replace None with the expected result

    def test_subtract(self):
        # TODO: Implement test for subtract
        # Expected return value of type Any
        result = samplecode.subtract(7, 2)
        self.assertEqual(result, 5)  # Replace None with the expected result


if __name__ == "__main__":
    unittest.main()
