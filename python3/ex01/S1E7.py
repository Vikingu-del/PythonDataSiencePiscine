from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, name, is_alive=True):
        """Constructor of Baratheon"""
        super().__init__(name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __repr__(self):
        """Representative method for Baratheon"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """String presentation of Baratheon"""
        return self.first_name + ' ' + self.family_name

    def die(self):
        """Makes a Baratheon ded"""
        super().die()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, name, is_alive=True):
        """Constructor of Lannister class"""
        super().__init__(name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    @classmethod
    def create_lannister(cls, name, is_alive):
        """Class method of Lanister to create a lanister object"""
        return Lannister(name, is_alive=is_alive)

    def __repr__(self):
        """Representative method of Lanister"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """String represantation of Lanister"""
        return self.first_name + ' ' + self.family_name

    def die(self):
        """Makes a Lanister die"""
        super().die()


def main():
    """Main entrypoing for Lannister and Baratheon"""

    Robert = Baratheon('Robert')
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")


if __name__ == '__main__':
    main()
