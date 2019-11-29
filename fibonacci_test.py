import unittest
import time
from fibonacci import fib_recursive,fib_dynamic,fib_optimize,fib_exception

class TimingFibonacci(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print ("%s: %.3f" % (self.id(), t))

    def test_time_recursive(self):
        fib_recursive(32)
        fib_recursive(32)

    def test_time_dynamic(self):
        fib_dynamic(32)
        fib_dynamic(32)

    def test_time_optimize(self):
        fib_optimize(32)
        fib_optimize(32)


class DefaultFibonacci(unittest.TestCase):
    def test_valid_input(self):
        valid_input_tests = {
            '10':   55,
            '30':   832040
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
