def square(x: int | float) -> int | float:
    """Returns the square of the argument (x * x)."""
    if not isinstance(x, (int, float)):
        raise TypeError("Error: the parameter should be int or float")
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of the argument by itself (x ** x)."""
    if not isinstance(x, (int, float)):
        raise TypeError("Error: the parameter should be int or float")
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an inner function (a closure) that maintains and updates the
    state 'x' with the result of the provided 'function' on each call.
    """
    # Initialize the state variable with the input 'x'
    count = 0
    curr_value = x

    def inner() -> float:
        """Inner function of the outer function"""
        nonlocal count
        nonlocal curr_value
        curr_value = function(curr_value)
        count += 1
        return curr_value

    return inner


def main():
    """Main Entrypoing for ex01"""
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == '__main__':
    main()
