"""Representation of a person."""


class Person:
    def __init__(self, first_name: str, last_name: str, age: int , mail: str, phone: str) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.upper()
        self.age = age
        self.mail= mail
        self.phone= phone
    def __str__(self)->str:
        return f"{self.first_name}  {self.last_name}"


def main():
    john = Person("John", "Doe", 30, "john.doe@uha.fr", "+33 06 82 72 22 76")
    print(f"First name: {john.first_name}")
    print(f"Last name: {john.last_name}")
    print(f"Age: {john.age}")
    print(f"mail: {john.mail}")
    print(f"Phone number: {john.phone}")
    print(john)


if __name__ == "__main__":
    main()

