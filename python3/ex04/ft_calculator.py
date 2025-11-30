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

    @classmethod
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product between 2 vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list)\
            or not all(isinstance(x, float | int) for x in V1)\
                or not all(isinstance(x, float | int) for x in V1):
            print("V1 and V2 should be vectors of floats or ints")
            return
        if len(V1) != len(V2):
            print("V1 and V2 should be the same size")
            return
        dot_product = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {float(dot_product)}")

    @classmethod
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Calculates the addition between 2 vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list)\
            or not all(isinstance(x, float | int) for x in V1)\
                or not all(isinstance(x, float | int) for x in V1):
            print("V1 and V2 should be vectors of floats or ints")
            return
        if len(V1) != len(V2):
            print("V1 and V2 should be the same size")
            return
        add_result = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is : {add_result}")

    @classmethod
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """Calculates the substraction between 2 vectors"""
        if not isinstance(V1, list) or not isinstance(V2, list)\
            or not all(isinstance(x, float | int) for x in V1)\
                or not all(isinstance(x, float | int) for x in V1):
            print("V1 and V2 should be vectors of floats or ints")
            return
        if len(V1) != len(V2):
            print("V1 and V2 should be the same size")
            return
        substract_vec = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {substract_vec}")


def main():
    """Main entrypoint for calculator"""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == '__main__':
    main()
