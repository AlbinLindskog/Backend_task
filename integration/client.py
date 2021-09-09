class BinditException(Exception):
    pass


class BinditClient:

    def create_account(self, name):
        """
        Creates an account in Bindit.

        :arg string name: Name of account to open.
        :returns dict:
        :raises BinditException: If the account could not be created.

        :Example:
            >>> BinditClient.create_account('gerbil')
            {'id': 45, 'name': 'gerbil'}
        """
        pass

    def update_account(self, id, name):
        """
        Updates an account in Bindit.

        :arg id int: ID of account to update
        :arg string name: New name of account
        :returns dict:
        :raises BinditException: If the account could not be updated.

        :Example:
            >>> BinditClient.update_account(45, 'mouse')
            {'id': 45, 'name': 'mouse'}
        """
        pass

    def delete_account(self, id):
        """
        Deletes an account in Bindit.

        :arg id int: ID of account to delete.
        :returns None:
        :raises BinditException: If the account could not be created.

        :Example:
            >>> BinditClient.delete_account(45)
        """
        pass

    def create_transfer(self, amount, account):
        """
        Creates a transfer in Bindit.

        :arg int amount: Amount to transfer.
        :arg int account: ID of account to transfer to.
        :returns dict:
        :raises BinditException: If the transfer could not be created.

        :Example:
            >>> BinditClient.create_transfer(12, 45)
            {'id': 67, 'amount': 12, 'account': 45}
        """
        pass

    def update_transfer(self, id, amount, account):
        """
        Updates a transfer in Bindit.

        :arg id int: ID of transfer to update.
        :arg int amount: New amount to transfer.
        :arg int account: ID of new account to transfer to.
        :returns dict:
        :raises BinditException: If the transfer could not be updated.

        :Example:
            >>> BinditClient.create_transfer(67, 22, 45)
            {'id': 67, 'amount': 22, 'account': 45}
        """
        pass

    def delete_transfer(self, id):
        """
        Deletes a transfer in Bindit.

        :arg id int: ID of transfer to delete.
        :returns None:
        :raises BinditException: If the transfer could not be deleted.

        :Example:
            >>> BinditClient.delete_transfer(67)
        """
        pass
