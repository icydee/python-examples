import unittest
from fibonacci import fib_recursive,fib_dynamic,fib_optimize

class DefaultFibRecursiveTestCase(unittest.TestCase):
    def test_valid_input(self):
        result = fib_recursive(10)
        self.assertEqual(result, 55)

        result = fib_dynamic(10)
        self.assertEqual(result, 55)

        result = fib_optimize(10)
        self.assertEqual(result, 55)

    def test_invalid_input(self):
        result = fib_recursive(0)
        self.assertEqual(result, 0)

        result = fib_dynamic(0)
        self.assertEqual(result, 0)

        result = fib_optimize(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
