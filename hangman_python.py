import random

def load_word_list(filename="words.txt"):
    """Load the list of words from a file. Each word should be on a separate line."""
    try:
        with open(filename, "r") as file:
            # Read each line, strip whitespace and ignore empty lines
            words = [line.strip() for line in file if line.strip()]
        if not words:
            print("⚠️ Warning: The word list is empty.")
        return words
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
        return []

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

def choose_word(word_list):
    """Randomly select a word from the provided word list."""
    if not word_list:
        raise ValueError("The word list is empty. Please ensure the file has words.")
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    """Display the word with correctly guessed letters and underscores for missing ones."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    """Main function to run the Hangman game."""
    words = load_word_list()
    try:
        word_to_guess = choose_word(words)  # Get a random word
    except ValueError as e:
        print(e)
        return

    guessed_letters = set()     # Store correct guesses
    incorrect_guesses = set()   # Store incorrect guesses
    max_attempts = 6            # Maximum allowed incorrect guesses

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

if __name__ == "__main__":
    hangman()
