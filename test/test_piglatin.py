# test_piglatin.py

import unittest
from piglatin import PigLatinTranslator

class TestPigLatinTranslator(unittest.TestCase):

    def test_initial_phrase(self):
        translator = PigLatinTranslator("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_translate_empty_string(self):
        translator = PigLatinTranslator("")
        self.assertEqual(translator.translate(), "nil")

if __name__ == "__main__":
    unittest.main()

