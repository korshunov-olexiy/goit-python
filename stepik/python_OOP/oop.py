class UserMail:
    def __init__(self, login, email):
        self.login = login  # устанавливаем имя
        self.__email = email      # устанавливаем возраст
 
    @property
    def email(self):
        pass
 
    @email.getter
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, new_email):
        if list(filter(lambda val: val in '@.', new_email)) == ['@','.']:
            self.__email = new_email
        else:
            print("Недопустимый email")
     
    @property
    def name(self):
        return self.login
         
    def display_info(self):
        print("Имя:", self.login, "\tВозраст:", self.__email)
         
         
tom = UserMail("Tom", 'balu@gmail.com')
 
tom.display_info()      # Имя: Tom  Возраст: 1
tom.email = 'balu145@gmail.co.m'         # Недопустимый возраст
print(tom.email)          # 1
tom.email = 'fuck@mail.ru'
tom.display_info()      # Имя: Tom  Возраст: 36
