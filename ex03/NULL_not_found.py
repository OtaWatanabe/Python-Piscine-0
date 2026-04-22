def NULL_not_found(object: any) -> int:
    type_obj = type(object)

    if object is None:
        print(f"Nothing: {object} {type_obj}")
        return 0
    if type_obj is bool and object is False:
        print(f"Fake: {object} {type_obj}")
        return 0
    if type_obj is int and object == 0:
        print(f"Zero: {object} {type_obj}")
        return 0
    if type_obj is float and object != object:
        print(f"Cheese: {object} {type_obj}")
        return 0
    if type_obj is str and object == "":
        print(f"Empty: {object} {type_obj}")
        return 0
    if type_obj is dict and len(object) == 0:
        print(f"Dict: {object} {type_obj}")
        return 0
    if type_obj is list and len(object) == 0:
        print(f"List: {object} {type_obj}")
        return 0
    if type_obj is set and len(object) == 0:
        print(f"Set: {object} {type_obj}")
        return 0
    if type_obj is tuple and len(object) == 0:
        print(f"Tuple: {object} {type_obj}")
        return 0

    print("Type not Found")
    return 1