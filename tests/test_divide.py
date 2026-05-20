import unittest
from src.math_ops import divide

class TestDivide(unittest.TestCase):
    def test_divide_normal(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
