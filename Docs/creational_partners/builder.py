class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

class UserBuilder:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None

    def set_name(self, name):
        self.name = name
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_password(self, password):
        self.password = password
        return self

    def build(self):
        return User(self.name, self.email, self.password)
