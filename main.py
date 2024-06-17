from utils.game import Hangman

def main():
    hangman = Hangman()
    while hangman.lives > 0 and hangman.correclty_guessed_letters != list(hangman.word_to_find):
        hangman.start_game(hangman.play, hangman.game_over, hangman.well_played)

if __name__ == "__main__":
    main()