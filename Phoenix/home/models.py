from django.db import models
from authorization.models import User
import secrets
import random

accTypes = (
    ('Deposit', 'Deposit'),
    ('Debit', 'Debit'),
)


# class Generator:
#     def checkAccountByNumber(self, number):
#         account_number = Account.objects.get(account_number=number)
#         if not account_number:
#             return True
#         else:
#             return False
#
#     def generateAccountNumber(self):
#         while True:
#             rnd = random.randint(1000, 9999)
#             if self.getAccountByNumber(rnd):
#                 return rnd
#             else:
#                 continue
#
#     def checkAPIKey(self, key):
#         api_key = Account.objects.get(api_key=key)
#         if not api_key:
#             return True
#         else:
#             return False
#
#     def generateAPIKey(self):
#         while True:
#             api_key = secrets.token_hex(16)
#             if self.checkAPIKey(api_key):
#                 return api_key
#             else:
#                 continue
#
#     def generateAccount(self):
#         account = Account(
#             account_number=self.generateAccountNumber(),
#             api_key=self.generateAPIKey()
#         )
#         account.save()


class Account(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.IntegerField('AccountNumber')
    balance = models.FloatField('Balance', default=0)
    type = models.CharField('Type', max_length=50, choices=accTypes)
    api_key = models.TextField('APIKey', default=secrets.token_hex(16), max_length=255)
    cvv_code = models.IntegerField('CVVCode', default=random.randint(100, 999))
    account_status = models.TextField('Status', max_length=1000, default="Just new.")

    def __str__(self):
        return str(self.account_number)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
