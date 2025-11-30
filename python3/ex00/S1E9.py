from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract character class"""
    def __init__(self, name, alive=True):
        """Constructor for abstract class Character"""
        self.first_name = name
        self.is_alive = alive

    @abstractmethod
    def die(self):
        """Makes character ded"""
        if self.is_alive:
            self.is_alive = False
        else:
            print(f'{self.first_name} is already ded')


class Stark(Character):
    """A Stark class which inherits from character"""
    def __init__(self, name, alive=True):
        """Constructor for Stark class with required argument name
and optional argument alive"""
        super().__init__(name, alive)

    def die(self):
        """Makes a Stark character die"""
        super().die()


def main():
    """Main entrypoint program to the character and stark classes"""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == '__main__':
    main()
