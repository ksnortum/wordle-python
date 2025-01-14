from termcolor import colored
from words import Word

class Game:
    def __init__(self):
        self.words = Word()
        self.guesses = []
        self.not_used = ""
        self.no_letter = lambda letter: colored(letter, attrs=['underline'])
        self.right_place = lambda letter: colored(letter, 'green', 'on_light_grey', attrs=['bold'])
        self.in_word = lambda letter: colored(letter, 'red', attrs=['bold'])
        
    # Play one game of Wordle
    # Returns True if the user wants to quit
    def play(self, first_time: bool) -> bool:
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
            if guess == word_to_guess:
                print(f"You guessed the word in {guess_no} guesses!")
                return

            self.guesses.append(guess)
            for letter in guess:
                if letter in self.not_used:
                    self.not_used = self.not_used.replace(letter, "")
            self.display_all(word_to_guess)
            guess_no += 1

        print(f"Sorry, you're out of guesses. The word was '{word_to_guess}'.")
        return False

    def help(self) -> None:
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
        guess = ""
        invalid = True

        while invalid:
            guess = input("Enter your guess: ")
            if guess in ("/quit", "/display", "/help"): 
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
        for guess in self.guesses:
            print(self.display_word_to_guess(guess, word_to_guess))
        print("You are on guess", len(self.guesses))
        unused_letters = ",".join([letter.upper() for letter in self.not_used if letter not in self.guesses])
        print("Unused letters:", unused_letters)

    def display_word_to_guess(self, guess: str, word_to_guess: str) -> str:
        display = ""
        processed_letters = []
        for index in range(5):
            if guess[index] in processed_letters or guess[index] not in word_to_guess:
                display += self.no_letter(guess[index].upper()) + ' '
            else:
                if guess[index] == word_to_guess[index]:
                    display += self.right_place(guess[index].upper()) + ' '
                else:
                    display += self.in_word(guess[index].upper()) + ' '
                processed_letters.append(guess[index])

        return display
