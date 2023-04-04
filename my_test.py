import unittest
from my_romans import decimal2roman
class MyTest(unittest.TestCase):
    def test_I(self):
        self.assertEqual (decimal2roman(1),"I")

if __name__== "__main__":
    unittest.main()
