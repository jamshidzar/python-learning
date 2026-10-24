"""
Hangman: guess the hidden word one letter at a time.
Keeps score across games.
"""

import random

WORDS = [
    "python",
    "banana",
    "computer",
    "keyboard",
    "network",
    "database",
    "algorithm",
    "function",
    "variable",
    "dictionary",
]
MAX_LIVES = 6


def get_guess(guessed):
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in guessed:
            print(f"You already guessed {guess}.")
        else:
            return guess


def update_board(secret_word, board, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            board[i] = guess


def play_game():
    secret_word = random.choice(WORDS)
    board = ["_" for ch in secret_word]
    lives = MAX_LIVES
    guessed = set()

    while "_" in board and lives > 0:
        print("\n" + " ".join(board))
        print(f"Lives: {lives}")

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in secret_word:
            update_board(secret_word, board, guess)
        else:
            lives -= 1
            print(f"Wrong! {guess} is not in the word.")

    if lives == 0:
        print(f"\nYou lost! The word was {secret_word}.")
        return False

    print(f"\nYou got it! The word was {secret_word}.")
    return True


def ask_play_again():
    answer = input("Play again? (y/n): ").strip().lower()
    return answer == "y"


def main():
    wins = 0
    losses = 0

    print("=== HANGMAN ===")

    while True:
        if play_game():
            wins += 1
        else:
            losses += 1

        print(f"Score: {wins} wins, {losses} losses")

        if not ask_play_again():
            print("Thanks for playing!")
            break


main()