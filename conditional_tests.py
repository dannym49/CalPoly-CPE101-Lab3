import unittest
from conditional import *

class TestCases(unittest.TestCase):

   # This test here to make sure you named your functions correctly.
   # Any other tests you add should only have one assert per function.
   def test_function_names(self):
      self.assertEqual(max_101(0, 0), 0)
      self.assertEqual(max_of_three(0, 0, 0), 0)
      self.assertEqual(rental_late_fee(0), 0)

   #tests for max
   def test_max_101_1(self):
      self.assertEqual(max_101(1,5), 5)
   def test_max_101_2(self):
      self.assertEqual(max_101(10,9), 10)

   #tests for max of three
   def test_max_three_1(self):
      self.assertEqual(max_of_three(1.145, 3.889, 5.431), 5.431)
   def test_max_three_2(self):
      self.assertEqual(max_of_three(10.44, 3.25, 5.18), 10.44)
   def test_max_three_3(self):
      self.assertEqual(max_of_three(10.44, 123.25, 5.18), 123.25)

   #tests for rental fee
   def test_rental_1(self):
      self.assertEqual(rental_late_fee(0), 0)
   def test_rental_2(self):
      self.assertEqual(rental_late_fee(1), 5)
   def test_rental_3(self):
      self.assertEqual(rental_late_fee(9), 5)
   def test_rental_4(self):
      self.assertEqual(rental_late_fee(10), 7)
   def test_rental_5(self):
      self.assertEqual(rental_late_fee(15), 7)
   def test_rental_6(self):
      self.assertEqual(rental_late_fee(16), 19)
   def test_rental_7(self):
      self.assertEqual(rental_late_fee(24), 19)
   def test_rental_8(self):
      self.assertEqual(rental_late_fee(25), 100)
   def test_rental_9(self):
      self.assertEqual(rental_late_fee(10000), 100)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

