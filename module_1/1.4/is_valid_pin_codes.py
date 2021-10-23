''' Проверяет валидность переданной строки пин-кодов

1. нет дубликатов
2. хранятся в виде строк
3. длина одного пина = 4
4. содержат только цифры
'''
def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0:
        return False
    elif len(set(pin_codes)) != len(pin_codes):
        return False
    elif set(filter(lambda p: type(p) != str or len(p) != 4 or not p.isdigit(), pin_codes)):
        return False
    else:
        return True


pins = ['1234', '1301', '9034', '0011']
print( is_valid_pin_codes(pins) )
