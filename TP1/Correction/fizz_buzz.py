"""Implementation of the FizzBuzz game."""

import utils


def fizz_buzz(number: int) -> str:
    """Return Fizz if the number is divisible by 3, Buzz if divisible by 5
    FizzBuzz if divisible by both 3 and 5. Otherwise returns the input number as a string.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FIzzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def main() -> None:
    """Implementation of the FizzBuzz game."""
    number = utils.get_int_from_user("Enter any number: ")
    print(fizz_buzz(number))


if __name__ == "__main__":
    main()
