# import packages
import unittest
from translator import englishToFrench, frenchToEnglish


class TestTransEng(unittest.TestCase) :
     """Created class to test the english translator function for null input and words """
     def test_Eng(self):
         null_input = None
         self.assertIsNone(null_input, englishToFrench)
         self.assertTrue(englishToFrench('Hello'), "Bonjour")


class TestTransFr(unittest.TestCase):
     """Created class to test the french translator function for null input and words """
     def test_Fr(self):
         null_input = None
         self.assertIsNone(null_input, frenchToEnglish)
         self.assertTrue(frenchToEnglish("Bonjour"), "Hello")


if __name__ == "__main__" :
      unittest.main()
