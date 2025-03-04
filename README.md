# Hangman Game with External Word List

This Python script implements a classic Hangman game where the words to guess are loaded from an external text file (`words.txt`). This allows for easy customization of the game's vocabulary.

## Features

-   **External Word List:** Loads words from a `words.txt` file, allowing for easy updates to the game's vocabulary.
-   **Error Handling:** Checks if the `words.txt` file exists and handles empty word lists.
-   **Random Word Selection:** Randomly chooses a word from the loaded list.
-   **Hangman Stages:** Displays different stages of the Hangman figure based on the number of incorrect guesses.
-   **Input Validation:** Checks if the player's input is a single letter.
-   **Guess Tracking:** Keeps track of correctly and incorrectly guessed letters.
-   **Win/Lose Conditions:** Determines the winner or loser based on the guesses.
-   **Clear Display:** Shows the current state of the word, incorrect guesses, and Hangman figure.

## Prerequisites

-   Python 3.x
-   A text file named `words.txt` containing one word per line.

## How to Run

1.  **Create `words.txt`:** Create a text file named `words.txt` in the same directory as the Python script. Add one word per line to this file.
2.  **Save the script:** Save the provided Python code as `hangman_with_file.py`.
3.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved `hangman_with_file.py`, and run the following command:

    ```bash
    python hangman_with_file.py
    ```

4.  **Play the game:** Follow the prompts to guess the letters and try to figure out the hidden word.

## Game Instructions

1.  The game will start by displaying the Hangman figure in its initial state and the hidden word represented by underscores.
2.  You will be prompted to enter a letter.
3.  If the letter is in the hidden word, it will be revealed.
4.  If the letter is not in the hidden word, a part of the Hangman figure will be drawn, and the letter will be added to the list of incorrect guesses.
5.  Try to guess the word before the Hangman figure is fully drawn (6 incorrect guesses).
6.  If you guess the word correctly, you win! If the Hangman figure is completed, you lose.

## File Structure

-   `hangman_with_file.py`: Contains the Hangman game implementation.
-   `words.txt`: Contains the list of words to be used in the game (one word per line).
