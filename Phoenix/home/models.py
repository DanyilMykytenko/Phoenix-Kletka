from django.db import models
from authorization.models import User

class Account(models.Model):
    owner_id = models.ForeignKey(User, on_delete = models.CASCADE)
    account_number = models.IntegerField('AccountNumber')
    balance = models.FloatField('Balance')
    type = models.CharField('Type', max_length = 50)
    api_key = models.TextField('APIKey', max_length = 255)
    cvv_code = models.IntegerField('CVVCode')
    account_status = models.TextField('Status', max_length = 1000)

    def __str__(self):
        return self.account_number

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
