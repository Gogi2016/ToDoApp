class Account:
    def __init__(self, account_id, created_at, is_active=True):
        self.__account_id = account_id
        self.__created_at = created_at
        self.__is_active = is_active

    def deactivate(self):
        pass

    def activate(self):
        pass

    def delete_permanently(self):
        pass