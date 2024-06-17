from utils.game import Hangman

def main():
    hangman = Hangman()
    while hangman.lives > 0 and hangman.well_played() == False:
            hangman.play()
            hangman.well_played()
            hangman.game_over()

if __name__ == "__main__":
    main()