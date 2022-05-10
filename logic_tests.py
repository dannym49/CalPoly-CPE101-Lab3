import unittest
from logic import *

class TestCases(unittest.TestCase):
   # This test here to make sure you named your functions correctly.
   # Any other tests you add should only have one assert per function.
   def test_function_names(self):
      self.assertTrue(is_even(0))
      self.assertFalse(in_an_interval(0))

   #tests for even
   def test_is_even_1(self):
      self.assertTrue(is_even(4))
   def test_is_even_2(self):
      self.assertTrue(is_even(1000))
   def test_is_even_3(self):
      self.assertFalse(is_even(9))
   def test_is_even_4(self):
      self.assertFalse(is_even(133))

   #tests for interval
   def test_interval_1(self):
      self.assertTrue(in_an_interval(2))
   def test_interval_2(self):
      self.assertTrue(in_an_interval(19))
   def test_interval_3(self):
      self.assertFalse(in_an_interval(9))
   def test_interval_4(self):
      self.assertFalse(in_an_interval(93))
   def test_interval_5(self):
      self.assertTrue(in_an_interval(102))
   def test_interval_6(self):
      self.assertTrue(in_an_interval(15))





# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

