from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class King with diamond inheritence"""

    def __init__(self, name, is_alive=True):
        """Constructor of class king"""
        super().__init__(name, is_alive)

    def set_eyes(self, eye):
        """Set eye color for the king"""
        self.eyes = eye

    def set_hairs(self, hair):
        """Set hair color for the king"""
        self.hairs = hair

    def get_eyes(self):
        """gets the eye color for the king"""
        return self.eyes

    def get_hairs(self):
        """Gets the hair color for the king"""
        return self.hairs


def main():
    """Main entrypoint script for king class"""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
    print(Joffrey.__str__.__doc__)
    print(Joffrey.__repr__.__doc__)


if __name__ == '__main__':
    main()
