from django.db import models
from authorization.models import User
import random

accTypes = (
    ('Deposit', 'Deposit'),
    ('Debit', 'Debit'),
)

class Account(models.Model):
    owner_id = models.ForeignKey(User, on_delete = models.CASCADE)
    account_number = models.IntegerField('AccountNumber', unique=True)
    balance = models.FloatField('Balance', default = 0)
    type = models.CharField('Type', max_length = 50, choices = accTypes)
    api_key = models.TextField('APIKey', max_length = 255)
    cvv_code = models.IntegerField('CVVCode', unique=True)
    account_status = models.TextField('Status', max_length = 1000, default = "Just new.")


    def __str__(self):
        return str(self.account_number)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

