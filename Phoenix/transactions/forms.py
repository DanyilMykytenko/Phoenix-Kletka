from .models import Transactions
from django import forms

class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ["date", "senders_account", "receivers_account", "amount", "description", "status", "error_message"]
