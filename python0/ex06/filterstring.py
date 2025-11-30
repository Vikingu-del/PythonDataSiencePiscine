from ft_filter import ft_filter
import sys


def validate_args(args: list[str]) -> tuple[list[str], int]:
    """Argument validation"""
    assert len(args) == 2, "the arguments are bad"
    nr = int()
    try:
        nr = int(args[1])
    except ValueError:
        raise AssertionError("the arguments are bad")
    if any(ft_filter(lambda x: not x.isalnum() and not x.isspace(), args[0])):
        raise AssertionError("the arguments are bad")
    return args[0].split(' '), nr


def filter_words(groups: tuple[list[str], int]) -> list[str]:
    """filter the wrods based on subject rules"""
    return [x for x in groups[0] if len(x) > groups[1]]


def main():
    """main function"""
    args = sys.argv[1:]
    try:
        print(list(filter_words(validate_args(args))))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
