# piglatin.py

class PigLatinTranslator:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        words = self.phrase.split()
        translated_words = []
        for word in words:
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
            translated_words.append("-".join(translated_sub_words))
        return " ".join(translated_words)
