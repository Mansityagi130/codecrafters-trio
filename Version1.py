import random

# List of words for the game
words = {
    "easy": ["python", "java", "ruby", "html", "css"],
    "medium": ["hangman", "programming", "computer", "science", "algorithm"],
    "hard": ["software", "developer", "javascript", "engineering", "database"]
}

# ASCII art for the Hangman
hangman_art = [
    """
     ------
    |    |
    |
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    -
    """
]

# Function to choose a random word from the list based on difficulty
def choose_word(difficulty):
    return random.choice(words[difficulty])

# Function to display the current state of the word with underscores for unknown letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Function to check if the player has won
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main function to run the game
def hangman():
    print("Welcome to Hangman!")
    name = input("What's your name? ")
    print(f"Hello, {name}!")

    # Choose difficulty level
    while True:
        difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
        if difficulty in words:
            break
        else:
            print("Invalid difficulty level. Please choose again.")

    word = choose_word(difficulty)
    guessed_letters = []
    attempts = 0

    while True:
        print(hangman_art[attempts])
        print("Word:", display_word(word, guessed_letters))
        print("Number of letters:", len(word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print("Incorrect guess!")

        if check_win(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break

        if attempts == len(hangman_art) - 1:
            print(hangman_art[attempts])
            print("You've run out of attempts! The word was:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing, " + name + "!")

# Run the game
hangman()
import random

# List of words for the game
words = {
    "easy": ["python", "java", "ruby", "html", "css"],
    "medium": ["hangman", "programming", "computer", "science", "algorithm"],
    "hard": ["software", "developer", "javascript", "engineering", "database"]
}

# ASCII art for the Hangman
hangman_art = [
    """
     ------
    |    |
    |
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |    |
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   /
    |
    -
    """,
    """
     ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    -
    """
]

# Function to choose a random word from the list based on difficulty
def choose_word(difficulty):
    return random.choice(words[difficulty])

# Function to display the current state of the word with underscores for unknown letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Function to check if the player has won
def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Main function to run the game
def hangman():
    print("Welcome to Hangman!")
    name = input("What's your name? ")
    print(f"Hello, {name}!")

    # Choose difficulty level
    while True:
        difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
        if difficulty in words:
            break
        else:
            print("Invalid difficulty level. Please choose again.")

    word = choose_word(difficulty)
    guessed_letters = []
    attempts = 0

    while True:
        print(hangman_art[attempts])
        print("Word:", display_word(word, guessed_letters))
        print("Number of letters:", len(word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print("Incorrect guess!")

        if check_win(word, guessed_letters):
            print("Congratulations! You've guessed the word:", word)
            break

        if attempts == len(hangman_art) - 1:
            print(hangman_art[attempts])
            print("You've run out of attempts! The word was:", word)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing, " + name + "!")

# Run the game
hangman()