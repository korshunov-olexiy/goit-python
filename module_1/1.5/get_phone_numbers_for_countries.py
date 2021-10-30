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


def get_phone_numbers_for_countries(list_phones):
    
    def country_code(number, codes):
        for c in codes.items():
            if number.startswith(c[1]): return c[0]
        return 'UA'
    
    countries_codes = {'UA': '380', 'TW': '886', 'SG': '65', 'JP': '81'}
    countries_phones = {k:[] for k in countries_codes.keys()}
    print(countries_phones, end='\n\n')
    list_phones = [sanitize_phone_number(l) for l in list_phones]
    print(list_phones, end='\n\n')
    for l in list_phones:
        countries_phones[country_code(l, countries_codes)].append(l)
    return countries_phones

lst = [' +70  ()9612  34534  )', '+38(067)3215678','+ 380967689876   ', ' +8156743567    ', ' +65(45) 643789  ', '    +813453531241244325', '+ 8(86)42334454567  ']

print( get_phone_numbers_for_countries(lst) )
