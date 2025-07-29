import random
import string

_LOWER = string.ascii_lowercase + string.digits
_UPPER = string.ascii_letters + string.digits

def _rnd_username():
    return "user" + ''.join(random.choice(_LOWER) for _ in range(6)) + str(random.randint(10, 99))

def _rnd_password():
    return ''.join(random.choice(_UPPER) for _ in range(8)) + str(random.randint(0,9))

def get_registration_data():
    email = f"{_rnd_username()}@testexample.com"
    pwd = _rnd_password()
    return {
        "email": email,
        "password": pwd,
        "confirm_password": pwd
    }

def get_registration_data_wrong_email():
    return {
        "email": ''.join(random.choice(_LOWER) for _ in range(8))
    }

def get_existing_user():
    return {
        "email": "registered_test@example.com",
        "password": "SecurePass99",
        "confirm_password": "SecurePass99"
    }

def get_create_ad_data():
    name = "Товар " + ''.join(random.choice(string.ascii_letters) for _ in range(4))
    description = f"{name}: это описание #{random.randint(100,999)}, высокое качество"
    cost = str(random.randint(500, 5000))
    return {
        "title": name,
        "description": description,
        "price": cost
    }
