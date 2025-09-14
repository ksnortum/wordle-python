import random

# Class to get a random word from a list of words
class Word():
    """ Class to get a random word from a list of words. """

    def __init__(self):
        """ Initialize the Word class by loading words from a file. """
        self.words = []
        file_name = 'words.txt'
        with open(file_name, 'r') as f:
            for line in f:
                self.words.append(line.strip())

    def random_word(self) -> str:
        """ Return a random word from the list of words. """
        return random.choice(self.words)
