import random

class Hangman:
    def __init__(self, lives: int=5):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions', 'python', 'success', 'burger']
        self.word_to_find = random.choice(self.possible_words)
        self.lives = lives
        self.correclty_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        
    def play(self):
        while True:
            letter_proposed = input("Which letter do you want to propose? ").lower()
            if len(letter_proposed) != 1:
                print("You should propose only one letter!")
                continue
            if letter_proposed in self.correclty_guessed_letters or letter_proposed in self.wrongly_guessed_letters:
                print("You already proposed this letter!")
                continue
            self.turn_count += 1
            self.turn_count
            if letter_proposed in self.word_to_find:
                self.correclty_guessed_letters.append(letter_proposed)
            else:
                self.wrongly_guessed_letters.append(letter_proposed)
                self.error_count += 1
            
            return self.turn_count, self.error_count, self.wrongly_guessed_letters, self.correclty_guessed_letters
            
    def well_played(self):
        displayed_word = len(self.word_to_find) * "_"
        list_displayed = list(displayed_word)
        for letter in self.correclty_guessed_letters:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    list_displayed[i] = letter
                    displayed_word = "".join(list_displayed)
        print(displayed_word)
        if displayed_word == self.word_to_find:
            print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
            return True
        else:
            return False
        
    def game_over(self):
        if self.error_count == self.lives:
            self.lives = 0
            print(f"Game over... The secret word was {self.word_to_find}.")