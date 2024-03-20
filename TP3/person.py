"""Representation of a person."""


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, email: str = "prenom.nom@mail.com", phone: str = "1234567890") -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.upper()
        self.age = age
        self.email = email
        self.phone = phone
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

def main():
    john = Person("John", "Doe", 30, "john.doe@mail.com", 1234567890)
    print(f"First name: {john.first_name}")
    print(f"Last name: {john.last_name}")
    print(f"Age: {john.age}")
    print(f"Email: {john.email}")
    print(f"Phone: {john.phone}")   
    print(john)


if __name__ == "__main__":
    main()
