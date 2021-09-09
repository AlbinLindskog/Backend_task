from django.db import models


class Account(models.Model):
    """
    Represents an account created in Bindit.
    """

    bindit_id = models.PositiveIntegerField()
    name = models.CharField(max_length=128)


class Transfer(models.Model):
    """
    Represents a transfer created to Bindit.
    """

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    bindit_id = models.PositiveIntegerField()
    amount = models.CharField(max_length=128)
