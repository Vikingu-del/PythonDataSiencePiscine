import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes as parameters a 2D array, prints its shape
and returns a truncated version of the array based
on the provided start and end arguments."""
    if not isinstance(family, list):
        print(f"{family} is not a list instance but is a {type(family)}")
        return None
    if not isinstance(start, int) or not isinstance(end, int):
        print(f"start or end are not int instances \
              but start: {type(start)} and end: {type(end)}")
        return None
    try:
        # arr = np.array(family, dtype=float) only numeric types
        arr = np.array(family)
    except Exception as e:
        print(f"Error: {e}")
        return None
    if arr.ndim != 2:
        print("Array should be 2 dimensional")
        return None
    print(f"My shape is : {arr.shape}")
    new = arr[start:end]
    print(f"My new shape is : {new.shape}")
    return new.tolist()


def main():
    """Main entrypoint of slice_me"""
    print("-----------------------Every think ok---------------------------")
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("---------------------inhomogeneous array------------------------")
    family = [[1.80, 78.4], [2.15], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("-----------------non numeric elements in array------------------")
    family = [[1.80, "78.4"], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

    print("-----------non numeric elements in the slicing edges------------")
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, "0", 2))
    print(slice_me(family, 1, -2))

    print("-------------------Family is not a list-------------------------")
    family = "Erik"
    print(slice_me(family, "0", 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
    print(f"slice_me.__doc__: {slice_me.__doc__}")
    print(f"main.__doc__: {main.__doc__}")
