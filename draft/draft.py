def main():
    target_word = get_word()
    lives = get_lives()
    suggested_letters = []
    while lives > 0:
        letter = get_guess(suggested_letters)
        lives = access_guess(target_word, letter, lives)
        current_state = display_word(target_word, suggested_letters)
        print(current_state)
        if current_state == target_word:
            print("Congratulations! You won!")
            break
    print("Game over! You used all your lives!")

def get_word():
    target_word = input("What is the word to be guessed ?").lower()
    return target_word

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
        print("Well done! The letter is in the secret word!")
    else:
        print("Sorry! Your guess is wrong and you lost one life")
        lives = lives - 1
    return lives

def display_word(secret_word, suggested_letters):
    displayed_word = len(secret_word) * "_"
    for letter in suggested_letters:
        if letter in secret_word:
            index = secret_word.index(letter)
            list_displayed = list(displayed_word)
            list_displayed[index] = letter
            displayed_word = "".join(list_displayed)
    return displayed_word

main()       