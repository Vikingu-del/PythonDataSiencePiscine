import numpy as np

# BMI body mass index BMI = mass(kg)/height(m2) = mass(lb)/height(in2) * 703


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """Takes a list of weights and heights with the same length and calculate
    the bmi for each parameter inside this lists by using numpy ndarrays"""
    len_height = len(height)
    len_weight = len(weight)
    if len_height != len_weight:
        print("Length of height and weight should be the same")
        return None
    if height is None or weight is None or len_weight == 0 or len_height == 0:
        print("Height or Weight can not be empty")
        return None
    if not all(list(isinstance(
        x,
        (int, float)) for x in height)) or not all(list(isinstance(
                x,
                (int, float)
            ) for x in weight)):
        print("Weight or height have other datatypes from floats & ints")
        return None
    return (np.array(weight) / np.array(height) ** 2).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Takes a list of floats or ints and returns a list of bools
    where true if an element of the list is above limit"""
    if bmi is None:
        print("BMI can not be empty")
        return None
    if not all(list(isinstance(x, (int, float)) for x in bmi)):
        print("BMI list has other datatypes from floats & ints")
        return None
    if not isinstance(limit, int):
        print("limit should be an integer data type")
    return (np.array(bmi) > limit).tolist()


def main():
    """Entrypoint function of give_bmi module"""
    print("------------Empty weight and height--------------")
    weight = []
    height = []
    bmi = give_bmi(height, weight)
    print("hello")
    print(apply_limit(bmi, 10))

    print("\n-----------Diff len of weight and height---------")
    weight = [1]
    height = [1, 2]
    bmi = give_bmi(height, weight)
    print("hello")
    print(apply_limit(bmi, 10))

    print("\nDiff types than list of ints or floats for weight")
    weight = ["erik", 1, 2]
    height = [1, 2, 3]
    bmi = give_bmi(height, weight)
    print("hello")
    print(apply_limit(bmi, 10))

    print("\nDiff types than list of ints or floats for apply limit")
    print(apply_limit(weight, 10))

    print("\n---------------Correct behaviour----------------")
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
