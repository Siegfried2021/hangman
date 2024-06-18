# hangman

# Hangman Game

This project implements the classic Hangman game in two different programming paradigms: Functional Programming and Object-Oriented Programming (OOP). The goal of the game is to guess the secret word by suggesting letters within a certain number of attempts. Unlike the traditional version, this implementation does not include the drawing of the hanged man.

## Description

The project is structured into two main parts:

1. **Functional Programming**: This implementation is contained in a single file `draft.py` where the game logic is implemented using functions.
2. **Object-Oriented Programming (OOP)**: This implementation uses a `Hangman` class to encapsulate the game logic. The OOP version is divided into two files: `game.py` (containing the `Hangman` class) and `main.py` (containing the game execution logic).

### Game Rules

- The player needs to guess the secret word letter by letter.
- If the guessed letter is correct, it is revealed in the word.
- If the guessed letter is incorrect, the number of lives is reduced.
- The game continues until the player either guesses the word or runs out of lives.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/hangman.git
   cd hangman

    Set up the environment:
        Ensure you have Python installed (version 3.6 or higher).
        You can use any IDE or text editor to edit the files. Popular choices include:
            VSCode (IDE/Text editor)
            PyCharm (IDE)
            Atom (Text editor)
            Sublime Text (Text editor)
            Vim (Text editor)

Usage
Functional Programming Version

    Navigate to the draft directory:


cd draft

Run the game:


    python draft.py

Object-Oriented Programming Version

    Navigate to the root directory of the project:


cd ..

Run the game:


    python main.py

Project Structure

The project directory structure is as follows:

css

hangman
│
└───draft
│   └──draft.py
└───utils
│   └──game.py
└───main.py

Functional Programming Files

    draft/draft.py: Contains the game logic implemented using functions.

Object-Oriented Programming Files

    utils/game.py: Contains the Hangman class with all the game logic.
    main.py: Contains the code to initiate and run the game using the Hangman class.

Game Components (OOP)

    possible_words: List of possible words, including ['becode', 'learning', 'mathematics', 'sessions'].
    word_to_find: The secret word represented as a list of letters.
    lives: Number of lives the player has left, starting at 5.
    correctly_guessed_letters: List showing the correctly guessed letters and placeholders for unguessed letters.
    wrongly_guessed_letters: List of incorrect guesses.
    turn_count: Counter for the number of turns played.
    error_count: Counter for the number of incorrect guesses.

Methods (OOP)

    play(): Handles the player's guess and updates the game state.
    start_game(): Runs the game loop until the game is won or lost.
    game_over(): Prints a game over message.
    well_played(): Congratulates the player for winning the game.

Enjoy playing Hangman!