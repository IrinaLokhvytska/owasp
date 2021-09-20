import pickle


def insecure_deserialization():
    f = open("examples/insecure_deserialization/pickle_example/demo.pickle", "rb")
    user_input = pickle.load(f)
    return user_input


print(insecure_deserialization())
