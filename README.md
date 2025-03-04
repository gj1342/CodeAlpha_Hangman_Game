# Hangman Game

This Python script implements a classic Hangman game. Players try to guess a hidden word by guessing one letter at a time. The game displays the Hangman figure as the player makes incorrect guesses.

## Features

-   **Random Word Selection:** The game randomly chooses a word from a predefined list.
-   **Hangman Stages:** Displays different stages of the Hangman figure based on the number of incorrect guesses.
-   **Input Validation:** Checks if the player's input is a single letter.
-   **Guess Tracking:** Keeps track of correctly and incorrectly guessed letters.
-   **Win/Lose Conditions:** Determines the winner or loser based on the guesses.
-   **Clear Display:** Shows the current state of the word, incorrect guesses, and Hangman figure.

## Prerequisites

-   Python 3.x

## How to Run

1.  **Save the script:** Save the provided Python code as `hangman.py`.
2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved `hangman.py`, and run the following command:

    ```bash
    python hangman.py
    ```

3.  **Play the game:** Follow the prompts to guess the letters and try to figure out the hidden word.

## Game Instructions

1.  The game will start by displaying the Hangman figure in its initial state and the hidden word represented by underscores.
2.  You will be prompted to enter a letter.
3.  If the letter is in the hidden word, it will be revealed.
4.  If the letter is not in the hidden word, a part of the Hangman figure will be drawn, and the letter will be added to the list of incorrect guesses.
5.  Try to guess the word before the Hangman figure is fully drawn (6 incorrect guesses).
6.  If you guess the word correctly, you win! If the Hangman figure is completed, you lose.

## Code Structure

-   `hangman.py`: Contains the Hangman game implementation.
    -   `word_list`: A list of words used in the game.
    -   `hangman_stages`: A list of strings representing the different stages of the Hangman figure.
    -   `choose_word()`: Randomly selects a word from the `word_list`.
    -   `display_word(word, guessed_letters)`: Displays the word with correctly guessed letters and underscores.
    -   `hangman()`: The main function that runs the Hangman game.

## Example Gameplay

```bash
🎯 Welcome to Hangman! 🎯
Guess the word, one letter at a time.
-----
|   |
    |
    |
    |
    |
--------
Word: _ _ _ _ _ _ _
Incorrect guesses (0/6):
Enter a letter: e
✅ Correct!
-----
|   |
    |
    |
    |
    |
--------
Word: _ e _ _ _ _ _
Incorrect guesses (0/6):
Enter a letter: a
✅ Correct!
... (Continue guessing)
