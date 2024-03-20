"""Representation of a person."""


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, email: str = "prenom.nom@mail.com", phone: str = "1234567890") -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.upper()
        self.age = age
        self.email = email
        self.phone = phone


def main():
    john = Person("John", "Doe", 30)
    print(f"First name: {john.first_name}")
    print(f"Last name: {john.last_name}")
    print(f"Age: {john.age}")
    print(f"Email: {john.email}")
    print(f"Phone: {john.phone}")   


if __name__ == "__main__":
    main()
