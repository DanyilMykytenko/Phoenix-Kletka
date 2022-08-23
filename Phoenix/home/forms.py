from .models import Account
from django import forms

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ["owner_id", "account_number", "balance", "type", "api_key", "cvv_code", "account_status"]