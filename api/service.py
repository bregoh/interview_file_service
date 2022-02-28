import random
import string


def generate_link(count):
    random_values = random.choices(string.ascii_lowercase + string.digits, k=count)
    return "".join(random_values)


def generate_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)

    password = [random.choice(characters) for i in range(9)]
    random.shuffle(password)
    return "".join(password)
