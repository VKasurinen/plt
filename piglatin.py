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
            if word[0].lower() in "aeiou":
                if word[-1].lower() == "y":
                    translated_words.append(word + "nay")
                elif word[-1].lower() in "aeiou":
                    translated_words.append(word + "yay")
                else:
                    translated_words.append(word + "ay")
            else:
                translated_words.append(word[1:] + word[0] + "ay")
        return " ".join(translated_words)
