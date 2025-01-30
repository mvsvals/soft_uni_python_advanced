# MoneyNotEnoughError - "Insufficient funds for the requested transaction"
#
# · PINCodeError - "Invalid PIN code"
#
# · UnderageTransactionError - "You must be 18 years or older to perform online transactions"
#
# · MoneyIsNegativeError - "The amount of money cannot be a negative number"

class MoneyNotEnoughError(Exception):
    pass

class PINCodeError(Exception):
    pass

class UnderageTransactionError(Exception):
    pass

class MoneyIsNegativeError(Exception):
    pass

pin, balance, age = [int(x) for x in input().split(', ')]

LEGAL_AGE = 18

while True:
    line = input().split('#')
    if line[0] == 'End':
        break
    if  line[0] == 'Send Money':
        money, pin_code = int(line[1]), int(line[2])
        if balance < money:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")
        if pin_code != pin:
            raise PINCodeError('Invalid PIN code')
        if age < LEGAL_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")
        print(f'Successfully sent {money:.2f} to a friend')
        print(f'There is {balance:.2f} money left in the bank account')
    elif line[0] == 'Receive Money':
        money = int(line[1])
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")
        into_balance = money * 0.5
        balance += into_balance
        print(f'{into_balance:.2f} money went straight into the bank account')

