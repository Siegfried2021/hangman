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
