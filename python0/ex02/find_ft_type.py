import typing as t

any = t.Any

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, int):
        print("Type not found")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    return 42

if __name__ == "__main__":
    pass