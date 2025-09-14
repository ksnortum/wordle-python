from termcolor import colored
from words import Word

class Game:
    """ Class to play one game of Wordle. """

    def __init__(self):
        """ Initialize the Game class. """
        self.words = Word()
        self.guesses = []
        self.not_used = ""
        self.no_letter = lambda letter: colored(letter, attrs=['underline'])
        self.right_place = lambda letter: colored(letter, 'white', 'on_green', attrs=['bold'])
        self.in_word = lambda letter: colored(letter, 'light_red', attrs=['bold'])

    def play(self, first_time: bool) -> bool:
        """Play a game of Wordle.

        Args:
            first_time (bool): Whether this is the first time the user is playing.

        Returns:
            bool: True if the user wants to quit, False otherwise.
        """
        guess_no = 1
        self.guesses = []
        self.not_used = "abcdefghijklmnopqrstuvwxyz"
        word_to_guess = self.words.random_word()
        if first_time: self.help()

        while (guess_no <= 6):
            guess = self.get_guess()
            if guess == "/quit":
                return True
            if guess == "/help":
                self.help()
                continue
            if guess == "/display":
                self.display_all(word_to_guess)
                continue
            if guess == "/admin":
                word_to_guess = input("Enter new word to guess: ")
                guess_no = 1
                self.guesses = []
                self.not_used = "abcdefghijklmnopqrstuvwxyz"
                continue
            if guess == word_to_guess:
                print(f"You guessed the word in {guess_no} guesses!")
                return False

            self.guesses.append(guess)
            for letter in guess:
                if letter in self.not_used:
                    self.not_used = self.not_used.replace(letter, "")
            self.display_all(word_to_guess)
            guess_no += 1

        print(f"Sorry, you're out of guesses. The word was '{word_to_guess}'.")
        return False

    def help(self) -> None:
        """Display help information about the game."""
        print("Wordle is a game where you try to guess a five-letter word.")
        print("After each guess, you will see a display of your guess.")
        print("Each letter in the display means something:")
        print(f"  {self.no_letter('W')} - The letter is not in the word.")
        print(f"  {self.right_place('W')} - The letter is in the word and in the right place.")
        print(f"  {self.in_word('W')} - The letter is in the word but in the wrong place.")
        print("You can use the command '/quit' to exit the game.")
        print("You can use the command '/display' to show all your guesses.")
        print("You can use the command '/help' to show this help message.")
        print("Good luck!")

    def get_guess(self) -> str:
        """Get a valid guess from the user. /quit, /help, and /display are also valid commands.

        Returns:
            str: The user's guess.
        """
        guess = ""
        invalid = True

        while invalid:
            guess = input("Enter your guess: ")
            if guess in ("/quit", "/display", "/help", "/admin"): 
                break
            if len(guess) != 5:
                print("You must enter a five-letter word.")
                continue 
            if guess not in self.words.words:
                print("Your guess must be a word in the dictionary.")
                continue
            invalid = False

        return guess
    
    def display_all(self, word_to_guess: str) -> None:
        """
        Display all the user's guesses so far and unused letters.

        Args:
            word_to_guess (str): The word the user is trying to guess.
        """
        for guess in self.guesses:
            print(self.display_word_to_guess(guess, word_to_guess))
        print("You are on guess", len(self.guesses))
        unused_letters = ",".join([letter.upper() for letter in self.not_used if letter not in self.guesses])
        print("Unused letters:", unused_letters)

    def display_word_to_guess(self, guess: str, word_to_guess: str) -> str:
        """
        Display the user's guess and its relation to the word to guess.

        Args:
            guess (str): The user's guess.
            word_to_guess (str): The word the user is trying to guess.

        Returns:
            str: A string representation of the guess's relation to the word to guess.
        """
        display = ""
        processed_letters = []

        for index in range(5):
            letter = guess[index]
            display_letter = letter.upper()

            # Guessed letter is in the right place
            if letter == word_to_guess[index]:
                display += self.right_place(display_letter) + ' '
            # Guessed letter is not in the word or has already been processed
            elif letter in processed_letters or letter not in word_to_guess:
                display += self.no_letter(display_letter) + ' '
            else:
                # We know the letter is in the word, but there may be an exact match later
                if self.exact_match_later(guess, word_to_guess, index):
                    display += self.no_letter(display_letter) + ' '
                else:
                    display += self.in_word(display_letter) + ' '

            # Only consider a letter processed if it doesn't appear later in the guess.
            # (Letter may appear twice or three time in the word to guess.)
            if letter not in word_to_guess[index + 1:]:
                processed_letters.append(letter)

        return display
    
    def exact_match_later(self, guess: str, word_to_guess: str, index: int) -> bool:
        """
        Check if there is an exact match for the guessed letter after the index in the word.

        Args:
            guess (str): The user's guess.
            word_to_guess (str): The word the user is trying to guess.
            index (int): The index of the letter to check.

        Returns:
            bool: True if there is an exact match later, False otherwise.
        """
        letter = guess[index]
        for later_index in range(index + 1, 5):
            if guess[later_index] == letter and word_to_guess[later_index] == letter:
                return True
            
        return False
