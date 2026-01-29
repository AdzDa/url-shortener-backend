import string
import random

def generate_unique_code(length: int = 4) -> str:
    characters = string.ascii_letters + string.digits
    result = []

    for i in range(length):
        result.append(random.choice(characters))

    return ''.join(result)