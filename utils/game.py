import random

class Hangman:
    """
        A class representing the game at its initial space.
        Attributes:
        possible words : list of secret words to be selected from
        word_to_find : randomly selected secret word
        lives : number of lives to be used until the game is over
        correctly_guessed_letters : list of correct guessed placed at the right index in the secret word
        wrongly_guessed_letters : list of the player's wrongly guessed letters
        turn_count = number of game turns corresponding to the number of guesses (correct or wrong)
        error_count = number of wrong guesses leading to a decrease in lives
    """
    def __init__(self, lives: int=5):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'python', 'success', 'burger', 'software']
        self.word_to_find = random.choice(self.possible_words)
        self.lives = lives
        self.correclty_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    def start_game(self, play, game_over, well_played):
        """
        Method initiating the game, updating the turn count, printing the updated attributes and handling the two possible
        outcomes of the game: secret word found or game over.
        """
        play()
        self.turn_count += 1
        print(f"Number of turns: {self.turn_count}")
        print(f"Current state of the game: {self.correclty_guessed_letters}")
        print(f"Number of errors: {self.error_count}")
        if len(self.wrongly_guessed_letters) > 0:
            print(f"The following proposed letters are not in the secret word: {self.wrongly_guessed_letters}")
        print(f"Number of lives left: {self.lives}")
        if self.lives == 0:
            game_over()
        if self.correclty_guessed_letters == list(self.word_to_find):
            well_played()

    def play(self):
        """
        Method initiating game turns until the end of the game, prompting the player for a letter guess, and handling the outcome : 
        if correct, the guessed letter is added at the right index in the list corresponding to the length of the secret word.
        If wrong, the proposed letter is added to the list of wrongly guessed letters, the error_count is updated, and the number of lives decreases by one.
        """
        while True:
            letter_proposed = input("Which letter do you want to propose? ").lower()
            if len(letter_proposed) != 1:
                print("You should propose only one letter!")
                continue
            if letter_proposed in self.correclty_guessed_letters or letter_proposed in self.wrongly_guessed_letters:
                print("You already proposed this letter!")
                continue
            if letter_proposed in self.word_to_find:
                list_word = list(self.word_to_find)
                for i in range(len(self.word_to_find)):
                    if list_word[i] == letter_proposed:
                        self.correclty_guessed_letters[i] = letter_proposed
            else:
                self.wrongly_guessed_letters.append(letter_proposed)
                self.error_count += 1
                self.lives -= 1
            return self.turn_count, self.error_count, self.lives, self.wrongly_guessed_letters, self.correclty_guessed_letters
            
    def well_played(self):
        """
        Method printing the outcome of the game if the player finds the secret word without exhausting the number of lives.
        """
        print(f"You found the word {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
        
    def game_over(self):
        """
        Method triggering the end of the game if the player exceeds his lives count without finding the secret word.
        """
        print(f"Game over... The secret word was {self.word_to_find}.")