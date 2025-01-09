import random

def get_random_word():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words)

def draw_hangman(attempts):
    stages = [
        """
           ------
           |    |
                |
                |
                |
                |
        """
        ,
        """
           ------
           |    |
           O    |
                |
                |
                |
        """
        ,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        """
        ,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        """
        ,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        """
        ,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        """
        ,
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        """
    ]
    # Print the corresponding stage for the number of attempts left
    print(stages[6 - attempts])

def hangman():
    word = get_random_word()
    guessed_word = ['_'] * len(word)
    attempts = 6

    print("Welcome to Hangman!")
    print(' '.join(guessed_word))
    draw_hangman(attempts)  # Draw the initial hangman

    while attempts > 0 and '_' in guessed_word:
        guess = input(f"You have {attempts} attempts left. Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(' '.join(guessed_word))
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.")
            draw_hangman(attempts)  # Draw hangman after each wrong guess

    if '_' not in guessed_word:
        print("Congratulations, you've guessed the word!")
    else:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
