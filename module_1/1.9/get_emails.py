'''
Разработайте функцию get_emails, которая получает в параметре список list_contacts
и возвращает список который содержит электронные адреса всех контактов из списка list_contacts.
Используйте при этом функцию map
'''
def get_emails(list_contacts):
    return list(map(lambda item: item['email'], list_contacts))


# EXAMPE:
data = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk',
'phone': '(992) 914-3792', 'favorite': False},
{'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca',
'phone': '(294) 840-6685', 'favorite': False},
{'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net',
'phone': '(542) 451-7038', 'favorite': False},
{'name': 'Wylie Pope', 'email': 'est@utquamvel.net',
'phone': '(692) 802-2949', 'favorite': False},
{'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com',
'phone': '(501) 472-5218', 'favorite': False}]

print(get_emails(data))
