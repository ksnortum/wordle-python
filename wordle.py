from game import Game

def run():
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

def yes_no_input(prompt):
    while True:
        response = input(prompt)
        if response == "yes" or response == "no":
            return response
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    run()
