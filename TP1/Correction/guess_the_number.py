"""Implementation of a "Guess the number" game"""

import random

import utils

NUMBER_TO_GUESS_MIN = 0
NUMBER_TO_GUESS_MAX = 100


def generate_rules(number_to_guess_min: int, number_to_guess_max: int) -> str:
    """Return the rules of the game."""
    return f"""GUESS THE NUMBER
The computer will randomly pick a number between {number_to_guess_min} and {number_to_guess_max}
Try to guess the number, and the computer will tell you if you guess too high or too low.
The game ends when you guess correctly.
"""


def choose_number_to_guess(lower_limit: int, upper_limit: int) -> int:
    """Randomly choose a number and return it."""
    return random.randint(lower_limit, upper_limit)


def main() -> None:
    """Entry point for the game"""
    print(generate_rules(NUMBER_TO_GUESS_MIN, NUMBER_TO_GUESS_MAX))
    number_to_guess = choose_number_to_guess(NUMBER_TO_GUESS_MIN, NUMBER_TO_GUESS_MAX)

    while True:
        player_guess = utils.get_int_from_user("Guess the number: ")
        if player_guess == number_to_guess:
            print("Correct!")
            return

        if player_guess < number_to_guess:
            print("Your number is too low")
        else:
            print("Your number is too high")


if __name__ == "__main__":
    main()
