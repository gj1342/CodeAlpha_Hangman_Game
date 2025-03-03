import random

# List of words for the game
word_list = ["python", "developer", "hangman", "programming", "framework", "frontend", "backend"]

# Hangman stages from 0 (no incorrect guesses) to 6 (max incorrect guesses)
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """
]

def choose_word():
    """Randomly select a word from the word list."""
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    """Display the word with correctly guessed letters and underscores for missing ones."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    """Main function to run the Hangman game."""
    word_to_guess = choose_word()  # Get a random word
    guessed_letters = set()  # Store correct guesses
    incorrect_guesses = set()  # Store incorrect guesses
    max_attempts = 6  # Maximum allowed incorrect guesses

    print("🎯 Welcome to Hangman! 🎯")
    print("Guess the word, one letter at a time.")
    
    while len(incorrect_guesses) < max_attempts:
        # Display the current hangman drawing based on incorrect guesses
        print(hangman_stages[len(incorrect_guesses)])
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        print(f"Incorrect guesses ({len(incorrect_guesses)}/{max_attempts}): {', '.join(sorted(incorrect_guesses))}")
        
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue
        
        # Check if already guessed
        if guess in guessed_letters or guess in incorrect_guesses:
            print("⚠️ You already guessed that letter!")
            continue
        
        # Correct guess
        if guess in word_to_guess:
            guessed_letters.add(guess)
            print("✅ Correct!")
        else:
            incorrect_guesses.add(guess)
            print("❌ Wrong guess!")

        # Check if the player won
        if set(word_to_guess) <= guessed_letters:
            print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
            # Display final hangman drawing
            print(hangman_stages[len(incorrect_guesses)])
            return

    # If loop ends, player lost
    print(hangman_stages[len(incorrect_guesses)])
    print("\n💀 Game Over! The word was:", word_to_guess)

# Run the game
hangman()
