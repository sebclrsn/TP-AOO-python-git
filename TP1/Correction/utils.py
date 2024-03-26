"""Some utils functions that are useful in many exercises."""

from pathlib import Path

CURRENT_DIR = Path.cwd().resolve()


def get_int_from_user(
    prompt_msg: str,
    value_min: int | None = None,
    value_max: int | None = None,
    max_attempts: int = 2,
) -> int:
    """Ask the user to enter a number in the console within the valid range if a range is provided.
    Will raise a ValueError if the user enters an input that cannot be converted to an integer
    `max_attempts` times.
    """
    for _ in range(max_attempts):
        user_input = input(prompt_msg)
        try:
            user_input_as_float = float(user_input)
        except ValueError:
            print(f"{user_input} is invalid: please enter a number!")
        user_input_as_int = round(user_input_as_float)
        if user_input_as_float != user_input_as_int:
            print(f"{user_input} is invalid: please enter a non-floating point number")
            continue

        if value_min is not None and value_min > user_input_as_int:
            print(f"{user_input_as_int} has to be greater than {value_min}")
            continue
        if value_max is not None and value_max < user_input_as_int:
            print(f"{user_input_as_int} has to be smaller than {value_max}")
            continue

        return user_input_as_int

    raise ValueError("User input cannot be converted to an integer")


def get_file_from_user(prompt_msg: str, max_attempts: int = 3) -> Path:
    """Ask the user to enter the path to a file from the current directly in the console.
    Will raise a FileNotFoundError if the user enters an invalid path
    `max_attempts` times.
    """
    for _ in range(max_attempts):
        user_input = input(prompt_msg)
        path = CURRENT_DIR / user_input
        if not path.exists() and not path.is_file():
            print(f"{path} does not exist or is not a file. Please enter a valid path:")
        else:
            return path
    raise FileNotFoundError("User input invalid path")
