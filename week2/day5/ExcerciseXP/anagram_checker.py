# Mini-project : Anagram checker

class AnagramChecker:
    def __init__(self, word_list_file):

        with open(word_list_file, "r") as file:
            self.words = set(
                word.strip().lower()
                for word in file
                if word.strip()
            )

    def is_valid_word(self, word):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):

        word = word.lower()
        anagrams = []

        for candidate in self.words:
            if candidate != word and self.is_anagram(word, candidate):
                anagrams.append(candidate)

        return anagrams