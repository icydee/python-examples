import unittest
from time_24 import time_convert_24

class DefaultTimeConvertTestCase(unittest.TestCase):
    def test_12_AM(self):
        result = time_convert_24('12:01:02 AM')
        self.assertEqual(result, '00:01:02')

    def test_12_PM(self):
        result = time_convert_24('12:33:44 PM')
        self.assertEqual(result, '12:33:44')

    def test_morning(self):
        result = time_convert_24('05:06:07 AM')
        self.assertEqual(result, '05:06:07')

    def test_afternoon(self):
        result = time_convert_24('05:06:07 PM')
        self.assertEqual(result, '17:06:07')

if __name__ == '__main__':
    unittest.main()
