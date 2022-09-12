from .models import Transactions
#from django.contrib.auth.models import User
from home.models import Account

def makeTransaction(sender, receiver, money):
    if not sender or not receiver:
        error_message = "Didn't find that account number:("
        return {error_message}
    sendersAccount = Account.objects.get(account_number=sender)
    receiversAccount = Account.objects.get(account_number=receiver)

    if not sendersAccount or not receiversAccount:
        error_message = "Didn't find that account number:("
        return {error_message}

    if sendersAccount[0].balance >= money:
        sendersAccount[0].balance = sendersAccount[0].balance - money
        sendersAccount.save()

        receiversAccount[0].balance = receiversAccount[0].balance + money
        receiversAccount.save()

        affectedAccounts = {sendersAccount, receiversAccount}
        return affectedAccounts
    else:
        errorMessage = "Not enough money:("
        return errorMessage

