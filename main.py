from utils.game import Hangman

def main():
    hangman = Hangman("becode")
    if hangman.word_to_find in hangman.possible_words:
        while hangman.lives > 0 and hangman.well_played() == False:
            hangman.well_played()
            hangman.game_over()
            hangman.play()
    else:
        print("The target word is not accepted")

if __name__ == "__main__":
    main()