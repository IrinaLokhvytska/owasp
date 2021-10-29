import hmac
import hashlib
import time


salt = "69OZjhT0"
password = "SomePassword1@"
pepper = "8340436b240a262ce67810b75635784382f2e77571b6f2b7ce29247219c38d"
pw_hash = "a0b74989108c5be8e8ff01178589da71a24828d97f1b0210fc6ed1dcf7e0cac7"


def is_correct_password(password, salt, pw_hash):
    start_time = time.time()
    message = password + salt
    h = hmac.new(bytes(pepper, "UTF-8"), bytes(message, "UTF-8"), hashlib.sha256)
    is_correct = pw_hash == h.hexdigest()
    time_taken = (time.time() - start_time) * 3600
    return is_correct, time_taken


def is_correct_password_digest(password, salt, pw_hash):
    start_time = time.time()
    message = password + salt
    h = hmac.new(bytes(pepper, "UTF-8"), bytes(message, "UTF-8"), hashlib.sha256)
    is_correct = hmac.compare_digest(pw_hash, h.hexdigest())
    time_taken = (time.time() - start_time) * 3600
    return is_correct, time_taken


test_passwords = [
    "abc123",
    "blahblah",
    "root",
    "admin",
    "somepassword",
    "Sop",
    "Some",
    "SomeP",
    "qwerty",
    "1234",
    "SomePassword",
    "SomePassword1",
    "SomePassword1@",
]
for password in test_passwords:
    print((password, is_correct_password(password, salt, pw_hash)))
    print((password, is_correct_password_digest(password, salt, pw_hash)))
    print("------------------------------------------")
