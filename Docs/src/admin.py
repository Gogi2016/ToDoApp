from src.user import User

class Admin(User):
    def __init__(self, user_id, name, email, password, admin_id, permissions):
        super().__init__(user_id, name, email, password)
        self.__admin_id = admin_id
        self.__permissions = permissions

    def manage_users(self):
        pass

    def delete_account(self):
        pass
