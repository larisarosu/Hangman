import random
import string

from hangman_words import word_list
from hangman_art import stages, logo

# keep lives in sync with the art for stages
lives = len(stages) - 1

print(logo)

chosen_word = random.choice(word_list).lower()

# Uncomment while developing if you want to see the answer
# print(f'[debug] the solution is {chosen_word}')

# initial placeholder
display = " ".join("_" for _ in chosen_word)
print(display)

game_over = False
correct_letters = []   # letters found in the word
wrong_letters = []     # letters guessed but not in the word

while not game_over:
    print(f"\n******************** {lives}/{len(stages)-1} LIVES LEFT ********************")
    if correct_letters or wrong_letters:
        print(f"Used: {' '.join(sorted(set(correct_letters + wrong_letters)))}")

    guess = input("Guess a letter: ").strip().lower()

    # basic input validation (single a–z letter)
    if len(guess) != 1 or guess not in string.ascii_lowercase:
        print("Please enter a single letter (a–z).")
        print(stages[lives])
        continue

    # already guessed? don't penalize
    if guess in correct_letters or guess in wrong_letters:
        print(f"You've already guessed '{guess}'.")
        print(display)
        print(stages[lives])
        continue

    if guess in chosen_word:
        # record correct guess once
        correct_letters.append(guess)

        # rebuild the display from scratch each time
        display = " ".join(ch if ch in correct_letters else "_" for ch in chosen_word)
        print(display)

        if "_" not in display:
            game_over = True
            print("\n🎉 You win!")
            print(f"The word was: {chosen_word}")
    else:
        wrong_letters.append(guess)
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(f"\n💀 You lose. The word was: {chosen_word}")

    if not game_over:
        print(stages[lives])
