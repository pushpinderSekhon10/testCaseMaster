import unittest
import samplecode
import json

class TestSamplecode(unittest.TestCase):
    # Class-level attribute to store results across all tests
    results = []

    @classmethod
    def tearDownClass(cls):
        # Write results to a JSON file after all tests have run
        with open('test_results.json', 'w') as f:
            json.dump(cls.results, f, indent=4)

    def record_result(self, test_name, result, error=None):
        """Helper method to record test results."""
        if error:
            self.__class__.results.append({
                "test": test_name,
                "result": result,
                "error": error
            })
        else:
            self.__class__.results.append({
                "test": test_name,
                "result": result
            })

    def test_add(self):
        # Test for add function
        result = samplecode.add(a=2, b=3)
        self.assertEqual(result, 5)
        self.record_result("test_add", "success")

    def test_subtract(self):
        # Test for subtract function
        result = samplecode.subtract(a=10, b=4)
        self.assertEqual(result, 6)
        self.record_result("test_subtract", "success")

    def test_Calculator_multiply(self):
        # Test for Calculator.multiply method
        obj = samplecode.Calculator()
        result = obj.multiply(a=3, b=4)
        self.assertEqual(result, 12)
        self.record_result("test_Calculator_multiply", "success")

    def test_Calculator_divide(self):
        # Test for Calculator.divide method
        obj = samplecode.Calculator()
        result = obj.divide(a=10, b=2)
        self.assertEqual(result, 5)
        self.record_result("test_Calculator_divide", "success")

    def test_Calculator_divide_by_zero(self):
        # Test for Calculator.divide method when dividing by zero
        obj = samplecode.Calculator()
        with self.assertRaises(ValueError) as context:
            obj.divide(a=10, b=0)
        self.assertEqual(str(context.exception), "Cannot divide by zero!")
        self.record_result("test_Calculator_divide_by_zero", "success")

if __name__ == "__main__":
    unittest.main()
