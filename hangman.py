
import random

# Colors for terminal
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
BOLD = "\033[1m"


with open("words.txt", "r", encoding="utf-8") as file:
    words = [
        word.strip().upper()
        for line in file
        for word in line.split()
        if word.isalpha() and len(word) >= 3
    ]

# Large and clear Hangman drawings
stages = [
    r"""
       +-----------+
       |           |
       |
       |
       |
       |
    ===+===============
    """,
    r"""
       +-----------+
       |           |
       |          ( )
       |
       |
       |
    ===+===============
    """,
    r"""
       +-----------+
       |           |
       |          ( )
       |           |
       |           |
       |
    ===+===============
    """,
    r"""
       +-----------+
       |           |
       |          ( )
       |          /|
       |           |
       |
    ===+===============
    """,
    r"""
       +-----------+
       |           |
       |          ( )
       |          /|\
       |           |
       |          /
    ===+===============
    """,
    r"""
       +-----------+
       |           |
       |          ( )
       |          /|\
       |           |
       |          / \
    ===+===============
    """
]


def show_title():
    print(CYAN + BOLD)
    print("=" * 45)
    print("       H A N G M A N   G A M E")
    print("=" * 45)
    print(RESET)


def play_hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    show_title()

    print(YELLOW + "Guess the hidden word, one letter at a time!")
    print("You have 6 chances. Good luck!\n" + RESET)

    while True:
        # Display the Hangman
        if wrong_guesses == 0:
            print(CYAN + stages[wrong_guesses] + RESET)
        else:
            print(RED + stages[wrong_guesses] + RESET)

        # Display the word
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print(BOLD + YELLOW + "WORD: " + display_word + RESET)
        print(GREEN + "Correct letters: " +
              ", ".join(sorted(guessed_letters)) + RESET)

        print(RED + f"Wrong guesses: {wrong_guesses}/{max_attempts}" + RESET)
        print(CYAN + f"Attempts left: {max_attempts - wrong_guesses}" + RESET)

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + GREEN + BOLD)
            print("*" * 45)
            print("       CONGRATULATIONS! YOU WON!")
            print("*" * 45)
            print(RESET)
            print("The correct word was:", secret_word)
            break

        # Check for defeat
        if wrong_guesses >= max_attempts:
            print("\n" + RED + BOLD)
            print("*" * 45)
            print("          GAME OVER!")
            print("*" * 45)
            print(RESET)
            print(YELLOW + "The correct word was: " +
                  secret_word + RESET)
            break

        guess = input(CYAN + "\nEnter a letter (A-Z): " + RESET)
        guess = guess.strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print(YELLOW + "Please enter only one English letter!\n" + RESET)
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print(YELLOW + "You already guessed that letter!\n" + RESET)
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(GREEN + BOLD + "Great! Correct guess!\n" + RESET)
        else:
            wrong_guesses += 1
            print(RED + BOLD + "Oops! Wrong guess!\n" + RESET)

    print(CYAN + "\nThanks for playing Hangman!" + RESET)


if __name__ == "__main__":
    play_hangman()
