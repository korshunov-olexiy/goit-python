from random import randint


def get_random_password():
    pwd_str = "()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    return ''.join(list(map(lambda p: chr(randint(40, 126)), pwd_str))[:8])


'''
1. Длина строки пароля восемь символов.
2. Содержит хотя бы одну букву в верхнем регистре.
3. Содержит хотя бы одну букву в нижнем регистре.
4. Содержит хотя бы одну цифру.
'''
def is_valid_password(password):
    if len(password) != 8: return False
    elif not any(p.isupper() for p in password): return False
    elif not any(p.islower() for p in password): return False
    elif not any(p.isdigit() for p in password): return False
    else: return True


def get_password():
    pwd = get_random_password()
    while not is_valid_password(pwd):
        pwd = get_random_password()
    return pwd


print( get_password() )
