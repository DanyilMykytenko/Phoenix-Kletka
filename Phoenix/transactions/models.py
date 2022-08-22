from django.db import models
from home.models import Account

class Transactions(models.Model):
    date = models.DateTimeField('Date')
    senders_account = models.ForeignKey(Account, related_name = "Sender", on_delete = models.DO_NOTHING)
    receivers_account = models.ForeignKey(Account, related_name = "Receiver", on_delete = models.DO_NOTHING)
    amount = models.FloatField('Amount')
    description = models.CharField('Description', max_length = 255)
    status = models.BooleanField('Status')
    error_message = models.TextField('ErrorMessage', max_length = 1000)

    def __str__(self):
        return f"{self.amount} : {self.senders_account} : {self.receivers_account}"

    class Meta:
        verbose_name = 'Transactions'
        verbose_name_plural = 'Transactions'