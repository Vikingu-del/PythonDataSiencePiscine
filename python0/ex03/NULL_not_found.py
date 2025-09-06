import math as m
import typing as t

any = t.Any

def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)):
        print(f"Nothing = {object} {type(object)}")
    elif isinstance(object, float) and m.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, int) and not isinstance(object, bool) and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    elif object == '':
        print(f"Empty: {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0

if __name__ == "__main__":
    pass