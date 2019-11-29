import unittest
from fibonacci import fib_recursive,fib_dynamic,fib_optimize,fib_exception

class DefaultFibonacci(unittest.TestCase):
    def test_valid_input(self):
        valid_input_tests = {
            '10':     55
        }

        for index in valid_input_tests:
            for test in [fib_recursive, fib_dynamic, fib_optimize]:
                result = test(int(index))
                self.assertEqual(result, valid_input_tests[index])

    def test_invalid_input(self):
        for index in [0, -1 -10]:
            self.assertRaises(fib_exception, fib_recursive, (index))
            self.assertRaises(fib_exception, fib_dynamic, (index))
            self.assertRaises(fib_exception, fib_optimize, (index))

if __name__ == '__main__':
    unittest.main()
