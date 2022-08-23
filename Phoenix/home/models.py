from django.db import models
from authorization.models import User
import random

accTypes = (
    ('Deposit', 'Deposit'),
    ('Debit', 'Debit'),
)

# class generator():
#     def __int__(self):
#         self.defaultAccountNumber = self.generateAccountNumber()
#
#     def getAccountByNumber(self, number):
#         account_number = Account.objects.get(account_number=number)
#         if not account_number:
#             return True
#         else:
#             return False
#
#     def generateAccountNumber(self):
#         rnd = 0
#         while True:
#             rnd = random.randint(1000, 9999)
#             if Account.getAccountByNumber(rnd) == True:
#                 return rnd
#             else:
#                 continue

class Account(models.Model):
    owner_id = models.ForeignKey(User, on_delete = models.CASCADE)
    account_number = models.IntegerField('AccountNumber', default = random.randint(1000,9999), unique=True)
    #account_number = models.IntegerField('AccountNumber', default = generator().defaultAccountNumber, unique=True)
    balance = models.FloatField('Balance', default = 0)
    type = models.CharField('Type', max_length = 50, choices = accTypes)
    api_key = models.TextField('APIKey', max_length = 255)
    cvv_code = models.IntegerField('CVVCode', default = random.randint(100,999), unique=True)
    account_status = models.TextField('Status', max_length = 1000, default = "Just new.")


    def __str__(self):
        return str(self.account_number)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

