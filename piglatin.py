import re


class PigLatinError(Exception):
    pass


class PigLatinTranslator:
    allowed_punctuation = ".,;:!?()'"

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"

        if any(char for char in self.phrase if
               char not in self.allowed_punctuation and not char.isalnum() and not char.isspace() and char != '-'):
            raise PigLatinError("Invalid character in input")

        words = re.findall(r"[\w'-]+|[.,;:!?()]", self.phrase)
        translated_output = []

        for word in words:
            if word in self.allowed_punctuation:
                translated_output.append(word)
            else:
                sub_words = word.split("-")
                translated_sub_words = []
                for sub_word in sub_words:
                    if sub_word[0].lower() in "aeiou":
                        if sub_word[-1].lower() == "y":
                            translated_sub_words.append(sub_word + "nay")
                        elif sub_word[-1].lower() in "aeiou":
                            translated_sub_words.append(sub_word + "yay")
                        else:
                            translated_sub_words.append(sub_word + "ay")
                    else:
                        consonant_prefix = ""
                        for char in sub_word:
                            if char.lower() not in "aeiou":
                                consonant_prefix += char
                            else:
                                break
                        translated_sub_words.append(sub_word[len(consonant_prefix):] + consonant_prefix + "ay")
                translated_output.append("-".join(translated_sub_words))

        result = []
        for i, item in enumerate(translated_output):
            if i > 0 and item not in self.allowed_punctuation:
                result.append(item)
            else:
                result.append(item)

        return " ".join(result).replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?").replace(
            " ;", ";").replace(" :", ":")
