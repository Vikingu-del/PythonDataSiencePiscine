import sys as s
from ft_filter import ft_filter


def validate_args(args: list[str]) -> tuple[list[str], int]:
    """
    Argument validation
    """
    assert args.__len__() == 2, "the arguments are bad"
    nr = int()
    try:
        nr = int(args[1])
    except ValueError:
        raise AssertionError("the arguments are bad")
    if any(ft_filter(lambda x: not x.isalnum() and not x.isspace(), args[0])):
        raise AssertionError("the arguments are bad")
    return args[0].split(' '), nr


def filter_words(groups: tuple[list[str], int]) -> list[str]:
    """
    filter the wrods based on subject rules
    """
    return list(ft_filter(lambda x: len(x) > groups[1], groups[0]))


def main():
    """
    main function
    """
    # args = s.argv[1:]
    # try:
    #     print(list(filter_words(validate_args(args))))
    # except AssertionError as e:
    #     print(f"AssertionError: {e}")
    print(filter.__doc__)


if __name__ == "__main__":
    main()
