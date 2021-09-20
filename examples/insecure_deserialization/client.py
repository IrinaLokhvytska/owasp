import os
import pickle


def serialize_exploit(user_input):
    f = open("examples/insecure_deserialization/demo.pickle", "wb")
    pickle.dump(user_input, f)


user_input = {"test": "some safe input"}
serialize_exploit(user_input)
#serialize_exploit(os.remove("examples/insecure_deserialization/important_client_information.csv"))
