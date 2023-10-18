from random import choices, randint
from string import ascii_letters, punctuation, digits

CHARSET = [*ascii_letters, *punctuation, *digits]

def generate_pwd_choices(len: int) -> str:
    return ''.join(choices(population=CHARSET, k=len))

def generate_pwd_recursive(longueur: int, temp_pwd: str = ""):
    if len(temp_pwd) < longueur:
        return generate_pwd_recursive(longueur, temp_pwd + generate_random_char())
    else:
        return temp_pwd

def generate_pwd_loop(longueur: int) -> str:
    pwd = ""
    for _ in range(longueur):
        pwd += generate_random_char()
    return pwd

def generate_random_char() -> str:
    return CHARSET[randint(0, len(CHARSET) - 1)]

#print(generate_pwd_choices(10))
print(generate_pwd_recursive(10))
#print(generate_pwd_loop(10))