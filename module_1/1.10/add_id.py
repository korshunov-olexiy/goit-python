'''
Создайте класс IDException, который будет наследовать класс Exception.
Также, реализуйте функцию add_id(id_list, employee_id), которая добавляет
в список id_list идентификатор пользователя employee_id и возвращает
указанный обновленный список id_list.
Функция add_id будет вызывать собственное исключение IDException,
если employee_id не начинается с '01' иначе employee_id будет добавлен
в список id_list
'''
class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not str(employee_id).startswith('01'):
        raise IDException
    else:
        id_list.append(employee_id)
        return id_list


# EXAMPLE:
lst = [1,2,3,4]
print(add_id(lst, '01234'))
