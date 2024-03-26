"""Count the number of words in a file."""

from collections import Counter

import utils

DEFAULT_WORD_TO_SEARCH = "python"


def get_word_occurrence(text: str, word: str, case_sensitive: bool = False) -> int:
    """Return the number of times `word` appears in `text`."""
    if not case_sensitive:
        text = text.lower()
        word = word.lower()

    word_occurrence = 0
    for line in text.split("\n"):
        for word in line.split(" "):
            if word == DEFAULT_WORD_TO_SEARCH:
                word_occurrence += 1

    return word_occurrence


def main(word_to_search: str) -> None:
    """Count the number of times a word is written in a text file provided by the user."""
    path = utils.get_file_from_user("Path to file to search: ")
    text = path.read_text()
    word_occurrence = get_word_occurrence(text, word_to_search)
    print(f"The word {word_to_search} appears {word_occurrence} times in {path.name}")


if __name__ == "__main__":
    main(DEFAULT_WORD_TO_SEARCH)
