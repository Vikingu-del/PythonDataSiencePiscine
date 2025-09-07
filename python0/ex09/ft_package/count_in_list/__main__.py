from .count_in_list import count_in_list


def main():
    """Main entry point for count_in_list package"""
    lst = ["toto", "tata", "toto"]
    to_find = "toto"
    try:
        result = count_in_list(lst, to_find)
    except Exception as e:
        print(f"Error: {e}")
        return
    print(f"Number of {to_find} in {lst} is {result}")


if __name__ == "__main__":
    main()
