#  Hangman (Python)
A simple command-line Hangman game built in Python.  
Guess letters one by one before you run out of lives!


##  Features
- Random word selection from a predefined list (`random.choice`)
- ASCII art for each stage of the hangman
- Tracks both correct and wrong guesses
- Prevents repeated guesses
- Input validation (only accepts single a–z letters)
- Clean output formatting using `join()`


## 🛠 Python knowledge demonstrated
This small project helped me practice:
- **Modules and imports** → splitting the project into multiple files (`hangman.py`, `hangman_words.py`, `hangman_art.py`)
- **Loops and conditions** → using `while` loops, `if/else` logic, and control statements like `continue`
- **String manipulation** → `.join()`, `.lower()`, `.strip()`, and f-strings for formatted output
- **Data structures** → lists (for correct/wrong guesses), sets (to remove duplicates), and string iteration
- **Randomization** → `random.choice()` to select a word
- **Basic error handling in input** → checking input length and restricting to alphabetic characters

