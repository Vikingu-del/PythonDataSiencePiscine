import sys as s


def check_input(object: list[str]) -> int:
    assert object.__len__() <= 1, 'more than one argument is provided'
    try:
        number = int(object[0])
        return number
    except ValueError:
        raise AssertionError("argument is not an integer")


def main():
    arguments = s.argv[1:]
    if arguments.__len__() == 0:
        return
    try:
        if check_input(arguments) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
