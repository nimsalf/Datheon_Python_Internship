# Hangman Word Guessing Game 🎮

## 1. Project Introduction

The Hangman Word Guessing Game is a simple, interactive, console-based game developed using Python 3.

In this game, the computer randomly selects a secret word from a predefined list. The player must guess the word by entering one letter at a time. The player has a maximum of six incorrect attempts to guess the word correctly.

The game displays ASCII Hangman artwork that changes with each incorrect guess. It also tracks previously guessed letters and prevents duplicate guesses from reducing the remaining attempts.

This project was developed to practise Python programming fundamentals, including loops, conditional statements, functions, sets, strings, and user input validation.

## 2. Features

- **Random Word Selection:** Selects a secret word randomly using Python's `random` module.
- **Interactive Gameplay:** Allows players to guess letters one at a time.
- **ASCII Hangman Art:** Displays Hangman drawings that update after incorrect guesses.
- **Six Attempts:** Gives the player up to six incorrect guesses.
- **Masked Word Display:** Shows correctly guessed letters and hides the remaining letters.
- **Duplicate Guess Prevention:** Prevents previously guessed letters from reducing attempts again.
- **Input Validation:** Handles invalid inputs such as numbers, symbols, and multiple characters.
- **Colored Terminal Output:** Uses ANSI escape codes to distinguish messages and game information.
- **Win and Lose Messages:** Displays the result and reveals the correct word at the end.

## 3. Requirements

### Software Requirements

- Python 3
- Visual Studio Code or PyCharm
- A terminal or command prompt

### Python Libraries

This project uses Python's built-in `random` module. No external packages are required.

## 4. Installation and Execution

### Step 1: Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH** if that option is available.

### Step 2: Download the Project

Clone the repository:

```bash
git clone https://github.com/nimsalf/Datheon_Python_Internship.git
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Step 3: Open the Project

Open the project folder in Visual Studio Code or PyCharm.

Make sure the `hangman.py` file is available in the folder.

### Step 4: Run the Game

Open the terminal in the project folder and execute:

```bash
python hangman.py
```

If the `python` command does not work on Windows, try:

```bash
py hangman.py
```

### Step 5: Play the Game

1. Run the program.
2. Read the hidden word displayed as underscores.
3. Enter one English letter at a time.
4. Try to guess the word before using all six incorrect attempts.
5. Win by guessing all letters correctly.

## 5. Sample Game Output

The following is an illustrative example of the terminal output:

```text
=============================================
       H A N G M A N   G A M E
=============================================

Guess the hidden word, one letter at a time!
You have 6 chances. Good luck!

WORD: A _ _ L E
Correct letters: A, E
Wrong guesses: 1/6
Attempts left: 5

Enter a letter (A-Z):
```

The actual word, Hangman drawing, and number of remaining attempts will vary during gameplay.

**Note:** This is an illustrative output, not an actual screenshot.

## 6. Project Structure

```text
Datheon_Python_Internship/
│
├── hangman.py
├── README.md
└── Hangman.zip
```

The `hangman.py` file contains the game logic, while `README.md` provides project documentation. `Hangman.zip` is an optional archive of the original project.

## 7. Concepts Used

- Variables and data types
- Lists and sets
- Strings and string manipulation
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions
- Random word selection
- Input validation
- ANSI terminal colors

## 8. Future Improvements

- Add difficulty levels.
- Allow users to play multiple rounds.
- Add a score and statistics system.
- Load words from an external text file.
- Add a graphical user interface.

## 9. Author

**Alfiya Nizam**

Python Internship Project

GitHub: https://github.com/nimsalf/Datheon_Python_Internship
