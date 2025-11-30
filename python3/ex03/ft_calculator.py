class calculator:
    """Calculator class"""
    def __init__(self, numb: list[float]):
        """Init method of calculator taking a list of
        ints and floats or just a single one"""
        if isinstance(numb, (int, float)):
            self.numb = [float(numb)]
            return
        if isinstance(numb, list) and all(isinstance(
                                        x,
                                        float | int) for x in numb):
            self.numb = numb
            return
        raise TypeError("Numb must be a float, int, or a list of floats/ints")

    def __add__(self, object) -> None:
        """Addition operator for calculator"""
        if not isinstance(object, int | float):
            print("Error: object should be int or float")
            return
        self.numb = [x + object for x in self.numb]
        print(self.numb)

    def __mul__(self, object) -> None:
        """Multiplication operator for calculator"""
        if not isinstance(object, int | float):
            print("Error: object should be int or float")
            return
        self.numb = [x * object for x in self.numb]
        print(self.numb)

    def __sub__(self, object) -> None:
        """Substraction operator for calculator"""
        if not isinstance(object, int | float):
            print("Error: object should be int or float")
            return
        self.numb = [x - object for x in self.numb]
        print(self.numb)

    def __truediv__(self, object) -> None:
        """Division operator for calculator"""
        if not isinstance(object, int | float):
            print("Error: object should be int or float")
            return
        if object == 0:
            print("Error: Division with 0 is not allowed")
            return
        self.numb = [x / object for x in self.numb]
        print(self.numb)


def main():
    """Main entrypoint for calculator"""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    try:
        v4 = calculator(['erik', 'seferi'])
    except TypeError as e:
        print(f'Error: {e}')
    v4 = calculator(2)
    v4 + 5
    v4 / 0


if __name__ == '__main__':
    main()
