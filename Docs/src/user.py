class User:
    def __init__(self, user_id, name, email, password):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.account = None
        self.notifications = []

    def register(self):
        pass

    def login(self):
        pass

    def reset_password(self):
        pass

    def delete_account(self):
        pass