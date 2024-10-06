import unittest
from simple_calculator import SimpleCalculator # type: ignore

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        # Add more assertions to thoroughly test the subtract method.
    def test_multiplying(self):
        """Test the multiplying method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Add more assertions to thoroughly test the multiply method.
    def test_dividing(self):
        """Test the dividing method."""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(1, 0), None)
        # Add more assertions to thoroughly test the divide method.
