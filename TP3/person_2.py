"""Representation of a person."""


class Person:

    AGE_MAJORITY = 18

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.upper()
        self.age = age

    def is_of_age(self) -> bool:
        """Return if the person is over the age of majority or not."""
        return self.age >= self.AGE_MAJORITY


def main():
    john = Person("John", "Doe", 30)
    bob = Person("Bob", "Smith", 34)

    print(f"Is John of age: {john.is_of_age()}")
    print(f"Is Bob of age: {bob.is_of_age()}")

    print("Change the age of majority to 32")
    # TODO

    print(f"Is John of age: {john.is_of_age()}")
    print(f"Is Bob of age: {bob.is_of_age()}")


if __name__ == "__main__":
    main()
