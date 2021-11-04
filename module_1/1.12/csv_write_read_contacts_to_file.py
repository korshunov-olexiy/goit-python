'''Разработайте две функции для сериализации и
десериализации списка контактов, с помощью
пакета csv и хранения полученных данных.
Первая функция write_contacts_to_file принимает два параметра:
filename имя файла, contacts список контактов.
Вторая функция read_contacts_from_file читает, выполняет
преобразование данных и возвращает указанный список contacts
из файла filename, сохраненного ранее функцией write_contacts_to_file.
Примечание: При чтении csv файла, мы получаем свойство словаря
favorite в виде строки, т.е. например favorite='False'. Необходимо
его привести к логическому выражению обратно, чтобы стало favorite=False.
'''

import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fn:
        flg = 1
        for contact in contacts:
            writer = csv.DictWriter(fn, fieldnames=contact.keys())
            if flg:
                writer.writeheader()
                flg = 0
            writer.writerow({key:val for key,val in contact.items()})


def read_contacts_from_file(filename):
    reader_dict = []
    with open(filename, 'r', newline='') as fn:
        reader = csv.DictReader(fn)
        for row in reader:
            row['favorite'] = eval(row['favorite'])
            reader_dict.append(row)
    return reader_dict

contacts = [{'name': 'Allen Raymond',
            'email': 'nulla.ante@vestibul.co.uk',
            'phone': '(992) 914-3792',
            'favorite': False},
            {'name': 'Chaim Lewis',
            'email': 'dui.in@egetlacus.ca',
            'phone': '(294) 840-6685',
            'favorite': False}]


write_contacts_to_file('contacts.csv', contacts)
print(read_contacts_from_file('contacts.csv'))
