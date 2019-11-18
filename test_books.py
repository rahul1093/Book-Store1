import unittest
from Book_on_rent import *


class TestStringMethods(unittest.TestCase):

    # Returns True if the string contains all chanters in lower case.
    def test_isupper(self):  # testing for isupper
        self.assertTrue('regular'.islower())
        self.assertFalse('ReguLar'.islower())
        self.assertTrue('fiction'.islower())
        self.assertFalse('Fiction'.islower())
        self.assertTrue('novel'.islower())
        self.assertFalse('Novel'.islower())


if __name__ == '__main__':
    unittest.main()
