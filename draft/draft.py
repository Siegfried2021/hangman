def main():
    word_to_find = get_word()
    lives = get_lives()
    suggested_letters = []
    while lives > 0:
        letter = get_guess(suggested_letters)
        lives = access_guess(word_to_find, letter, lives)
        current_state = display_word(word_to_find, suggested_letters)
        print(current_state)
        if current_state == target_word:
            print("Congratulations! You won!")
            break
    if lives == 0:
        print("Game over! You used all your lives!")

def get_word():
    word_to_find = input("What is the word to be guessed ?").lower()
    return word_to_find

def get_lives():
    number_lives = int(input("How many lives does the player will have?"))
    return number_lives
        
def get_guess(suggested_letters):
    while True:
        guess = input("Which letter do you want to propose?").lower()
        
        if len(guess) != 1:
            print("You should propose only one letter!")
            continue
            
        if guess in suggested_letters:
            print("You already proposed this letter!")
            continue
            
        suggested_letters.append(guess)
            
        return guess
        
def access_guess(secret_word, guessed_letter, lives):
    if guessed_letter in secret_word:
        print(f"Well done! The letter {guessed_letter} is in the secret word!")
    else:
        lives = lives - 1
        if lives > 1:
            print(f"Sorry! Your guess is wrong! You have {lives} lives left.")
        else:
            print(f"Sorry! Your guess is wrong! You have {lives} life left.")
    return lives

def display_word(secret_word, suggested_letters):
    displayed_word = len(secret_word) * "_"
    list_displayed = list(displayed_word)
    for letter in suggested_letters:
        for i in range(len(secret_word)):
            if secret_word[i] == letter:
                list_displayed[i] = letter
                displayed_word = "".join(list_displayed)
    return displayed_word

main()