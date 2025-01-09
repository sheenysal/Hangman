# Hangman Game

This is a simple implementation of the classic **Hangman** game in Python. The game selects a random word from a file (`words.txt`), and the player has to guess it by suggesting letters within a limited number of attempts. 

The game displays a visual representation of a hangman as the player makes incorrect guesses.

## Features
- Random word selection from a `words.txt` file.
- Hangman drawing that updates with each incorrect guess.
- User input validation to ensure only letters are entered.
- Displays the number of attempts remaining.
- Player can guess the word one letter at a time.

## How to Play
1. The program will display a series of underscores representing the letters of the word to guess.
2. You can guess one letter at a time. If the letter is in the word, it will replace the corresponding underscore(s).
3. After each incorrect guess, a part of the hangman will be drawn.
4. You have 6 attempts to guess the word before the game ends.

## Setup

### Requirements
- Python 3.x
- A file named `words.txt` containing a list of words for the game.

### Installing Dependencies
Before running the game, you may need to install the required dependencies. You can install them using pip:

```bash
pip install requests
