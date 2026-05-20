import unittest
from src.math_ops import add

class TestAdd(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -4), -5)

if __name__ == "__main__":
    unittest.main()
