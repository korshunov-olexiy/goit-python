class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({
            'id': Contacts.current_id,
            'name': name,
            'phone': phone,
            'email': email,
            'favorite': favorite})
        Contacts.current_id += 1


# EXAMPLE:
cnt = Contacts()
cnt.add_contacts('vasya1', 9249249249, 'vasya1@gamil.com', 'petya1')
cnt.add_contacts('vasya2', 9249249249, 'vasya2@gamil.com', 'petya2')
cnt.add_contacts('vasya3', 9249249249, 'vasya3@gamil.com', 'petya3')
cnt.add_contacts('vasya4', 9249249249, 'vasya4@gamil.com', 'petya4')

print(cnt.list_contacts())
