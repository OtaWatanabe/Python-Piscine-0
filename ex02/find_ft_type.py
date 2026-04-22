def all_thing_is_obj(object: any) -> int:
    type_obj = type(object)
    if type_obj == list:
        print("List : ", type_obj)
        return 42
    if type_obj == dict:
        print("Dict : ", type_obj)
        return 42
    if type_obj == tuple:
        print("Tuple : ", type_obj)
        return 42
    if type_obj == set:
        print("Set : ", type_obj)
        return 42
    if type_obj == str:
        print(f"{object} is in the kitchen : ", type_obj)
        return 42
    print("Type not found")
    return 42