from game import Game

def run():
    """Run the Wordle game."""
    play_again = "yes"
    we_quit = False
    first_time = True
    game = Game()
    while play_again == "yes":
        we_quit = game.play(first_time=first_time)
        if we_quit:
            break
        play_again = yes_no_input("Do you want to play again? (yes/no) ")
        first_time = False

def yes_no_input(prompt: str) -> str:
    """
    Prompt the user with a yes/no question until they provide a valid response. 
    Args:
        prompt (str): The question to ask the user. 
    Returns:
        str: The user's response, either "yes" or "no".
    """
    while True:
        response = input(prompt)
        if response == "yes" or response == "no":
            return response
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    run()
