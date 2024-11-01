import unittest
from piglatin import PigLatinTranslator, PigLatinError

class TestPigLatinTranslator(unittest.TestCase):

    def test_initial_phrase(self):
        translator = PigLatinTranslator("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_translate_empty_string(self):
        translator = PigLatinTranslator("")
        self.assertEqual(translator.translate(), "nil")

    def test_translate_word_starting_with_vowel_ending_with_y(self):
        translator = PigLatinTranslator("any")
        self.assertEqual(translator.translate(), "anynay")

    def test_translate_word_starting_with_vowel_ending_with_vowel(self):
        translator = PigLatinTranslator("apple")
        self.assertEqual(translator.translate(), "appleyay")

    def test_translate_word_starting_with_vowel_ending_with_consonant(self):
        translator = PigLatinTranslator("ask")
        self.assertEqual(translator.translate(), "askay")

    def test_translate_word_starting_with_single_consonant(self):
        translator = PigLatinTranslator("hello")
        self.assertEqual(translator.translate(), "ellohay")

    def test_translate_word_starting_with_multiple_consonants(self):
        translator = PigLatinTranslator("known")
        self.assertEqual(translator.translate(), "ownknay")

    def test_translate_phrase_with_multiple_words(self):
        translator = PigLatinTranslator("hello world")
        self.assertEqual(translator.translate(), "ellohay orldway")

    def test_translate_phrase_with_composite_word(self):
        translator = PigLatinTranslator("well-being")
        self.assertEqual(translator.translate(), "ellway-eingbay")

    def test_translate_phrase_with_punctuation(self):
        translator = PigLatinTranslator("hello world!")
        self.assertEqual(translator.translate(), "ellohay orldway!")

    def test_translate_phrase_with_invalid_punctuation(self):
        translator = PigLatinTranslator("hello @world")
        with self.assertRaises(PigLatinError):
            translator.translate()

if __name__ == "__main__":
    unittest.main()
