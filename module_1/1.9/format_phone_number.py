'''
Декоратор должен добавлять для коротких номеров префикс +38,
а для полного международного номера (из 12 символом) только знак +.
Реализуйте декоратор format_phone_number для функции sanitize_phone_number
с необходимым функционалом.
'''
def format_phone_number(func):
    def inner(phone):
        new_phone = func(phone)
        if len(new_phone) < 12:
            new_phone = '+38' + str(new_phone)
        elif len(new_phone) == 12:
            new_phone = '+' + str(new_phone)
        return new_phone
    return inner


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number(' +38(050)123-32-34'))
