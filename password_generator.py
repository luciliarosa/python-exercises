#Simple program to generate secure password

import random

def password_generator():
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    special = '!@#$%¨&*()_'
    numbers = '1234567890'

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(special),
        random.choice(numbers)
    ]

    mix_caracteres = uppercase + lowercase + numbers + special
    password.extend(random.choices(mix_caracteres, k=8))
    random.shuffle(password)
    return ''.join(password)

print(f'Password generated: {password_generator()}')
    