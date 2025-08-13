# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if self.is_anagram(anagram)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return candidate_lower != self.word and sorted(candidate_lower) == sorted(self.word)