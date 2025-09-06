import sys


def check_input(object: list[str]) -> str:
    """
    Checks and validates the arguments
    """
    na = object.__len__()
    assert na <= 1, 'There are more than 1 argument'
    if na == 0:
        lines = []
        try:
            while (True):
                if na == 0:
                    word = input("What is the text to count?")
                else:
                    word = input()
                na += 1
                lines.append(word)
        except EOFError:
            return "\n".join(lines)
    else:
        return object[0]


def process_input(string: str) -> None:
    """
    proccess a string input and counts how many
    characters, upper letters, lower letters, punctuation marks, spaces
    and digits has
    """
    print(f"The text contains {string.__len__()} characters:")
    print(f"{[x for x in string if x.isupper()].__len__()} upper letters")
    print(f"{[x for x in string if x.islower()].__len__()} lower letters")
    punct = [x for x in string if x in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
    print(f"{punct.__len__()} punctuation marks")
    print(f"{[x for x in string if x.isspace()].__len__()} spaces")
    print(f"{[x for x in string if x.isdigit()].__len__()} digits")


def main():
    """
    This program parses the arguments validates and process them
    """
    args = sys.argv[1:]
    try:
        string = check_input(args)
        process_input(string)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
    # print(process_input.__doc__)
    # print(check_input.__doc__)
    # print(main.__doc__)
