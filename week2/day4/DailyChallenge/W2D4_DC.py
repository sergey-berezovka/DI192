import string
import re


class Text:
    def __init__(self, text):
        self.text = text

    # Step 2
    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else None

    # Step 3
    def most_common_word(self):
        words = self.text.lower().split()
        frequencies = {}

        for word in words:
            frequencies[word] = frequencies.get(word, 0) + 1

        most_common = max(frequencies, key=frequencies.get)
        return most_common

    # Step 4
    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    # Step 5
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        return cls(content)

class TextModification(Text):

    # Step 7
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned = self.text.translate(translator)
        return cleaned

    # Step 8
    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "is", "in", "at", "on", "and",
            "or", "if", "to", "of", "for", "with", "as",
            "by", "this", "that", "it"
        }

        words = self.text.split()
        filtered = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered)

    # Step 9
    def remove_special_characters(self):
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", self.text)
        return cleaned
    
text = Text("Hello world hello Python world")

print(text.word_frequency("world"))
print(text.most_common_word())
print(text.unique_words())

file_text = Text.from_file("week2/day4/DailyChallenge/sample.txt")
print(file_text.most_common_word())

mod = TextModification("Hello!!! This is a test, and it works.")
print(mod.remove_punctuation())
print(mod.remove_stop_words())
print(mod.remove_special_characters())