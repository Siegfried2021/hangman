from utils.game import Hangman

def main():
    """
        Main function allowing for the creating of a Hangman game object, launching the game until the player either finds
        the secret word or exceeds his lives allowance.
    """
    hangman = Hangman()
    while hangman.lives > 0 and hangman.correclty_guessed_letters != list(hangman.word_to_find):
        hangman.start_game(hangman.play, hangman.game_over, hangman.well_played)

if __name__ == "__main__":
    main()