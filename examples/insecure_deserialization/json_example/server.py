import json


def insecure_deserialization():
    with open("examples/insecure_deserialization/json_example/demo.json", "r") as write_file:
        user_input = json.load(write_file)
    return user_input


print(insecure_deserialization())
