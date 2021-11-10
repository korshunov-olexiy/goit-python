class UserMail:
    def __init__(self,login, __email):
        self.login = login
        self.__email = __email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new_email):
        if list(filter(lambda val: val in '@.', str(new_email))) == ['@','.']:
           self.__email = new_email
        else:
            print("Ошибочная почта")


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
