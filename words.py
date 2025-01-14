import random

# Class to get a random word from a list of words
class Word():
    def __init__(self):
        self.words = []
        file_name = 'words.txt'
        with open(file_name, 'r') as f:
            for line in f:
                self.words.append(line.strip())

    def random_word(self) -> str:
        return random.choice(self.words)
