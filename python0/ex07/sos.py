import sys as s

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/ "
}


def validate_input(args: list[str]) -> None:
    """Validates the input"""
    assert len(args) == 1, "the arguments are bad"
    word = args[0].upper()
    assert all(char in NESTED_MORSE for char in word), "the arguments are bad"


def main():
    """A Function which translates alphanumeric and space into morse code"""
    args = s.argv[1:]
    try:
        validate_input(args)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    word = args[0].upper()
    print("".join([NESTED_MORSE[char] for char in word]))


if __name__ == "__main__":
    main()
