class BinditException(Exception):
    pass


class BinditClient:

    def create_account(self, name):
        pass

    def update_account(self, id, name):
        pass

    def delete_account(self, id):
        pass

    def create_transfer(self, amount, account):
        pass

    def update_transfer(self, id, amount, account):
        pass

    def delete_transfer(self, amount, account):
        pass
