import random
import string

def generate_word():
    with open('wordlist.txt', 'r') as file:
        words = file.readlines()
        return random.choice(words).strip()

def get_clue(word, guess):
    return ''.join(
        '◯' if g in word else '✕' if g == w else ' ' for w, g in zip(word, guess)
    )

def play_wordle():
    word = generate_word()
    attempts = 6

    while attempts > 0:
        guess = input(f"{attempts} attempts left. Enter your 5-letter guess: ").lower()

        if len(guess) != 5 or not all(c in string.ascii_lowercase for c in guess):
            print("Invalid guess. Please enter a 5-letter word.")
            continue

        if guess == word:
            print("Congratulations! You've guessed the word!")
            break

        clue = get_clue(word, guess)
        print(f"Clue: {clue}")

        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    play_wordle()