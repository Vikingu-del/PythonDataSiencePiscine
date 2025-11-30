import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character ID using lowercase ASCII letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A dataclass representing a student with calculated login and generated ID.

    - login and id are set with init=False to prevent initialization via the
        constructor.
    - active defaults to True.
    - Uses default __repr__ (no custom __str__ or __repr__).
    """
    # Fields that must be initialized
    name: str
    surname: str

    # Field with a default value
    active: bool = field(default=True)

    # Fields that are calculated and cannot be initialized via the constructor
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        Calculates and assigns values to fields where init=False,
        after the initial __init__ has completed.
        """

        # 1. Calculate Login:
        #    First letter of name (uppercase) + surname (lowercase)
        # Example: Edward + agle -> Eagle
        self.login = f"{self.name[0].upper()}{self.surname.lower()}"

        # 2. Generate ID
        self.id = generate_id()


def main():
    """main entrypoint for student object"""
    student = Student(name="Edward", surname="agle", active="false")
    print(student)


if __name__ == '__main__':
    main()
