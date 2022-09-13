from .models import Account
from random import Random
import copy
import secrets

class accountNumberGenerator:

    mastercardPrefixList = [
            ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

    def completed_number(self, prefix, length):
        ccnumber = prefix

        # generate digits
        while len(ccnumber) < (length - 1):
            digit = str(generator.choice(range(0, 10)))
            ccnumber.append(digit)

        # Calculate sum
        sum = 0
        pos = 0

        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()

        while pos < length - 1:
            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9
            sum += odd
            if pos != (length - 2):
                sum += int(reversedCCnumber[pos + 1])
            pos += 2

        # Calculate check digit
        checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
        ccnumber.append(str(checkdigit))
        return ''.join(ccnumber)

    def credit_card_number(self, rnd, prefixList, length):
        result = []
        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(self.completed_number(ccnumber, length))
        return result

    def checkForExistingAccount(self, accountNumber):
        existingAccount = Account.objects.get(accountNumber=accountNumber)
        if existingAccount:
            return True
        else:
            return False

    def generateAccountNumber(self):
        generator = Random()
        generator.seed()
        accountNumber = self.credit_card_number(generator, self.mastercardPrefixList, 16)
        if not self.checkForExistingAccount(accountNumber):
            return accountNumber
        else:
            return self.generateAccountNumber()

class accountCVVGenerator:
    def checkForExistingCode(self, cvv_code):
        existingAccount = Account.objects.get(cvv_code = cvv_code)
        if existingAccount:
            return True
        else:
            return False

    def generateCVVCode(self):
        code = ''
        for i in range(3):
            code = code + str(randint(0, 9))
        if not self.checkForExistingCode(code):
            return code
        else:
            return self.generateCVVCode()

class accountAPIKeyGenerator():
    def checkForExistingKey(self, key):
        existingAccount = Account.objects.get(api_key = key)
        if existingAccount:
            return True
        else:
            return False

    def generateAPIKey(self):
        if not self.checkForExistingKey():
            return secrets.token_urlsafe(16)
        else:
            return self.generateAPIKey()