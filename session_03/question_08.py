#session 3 Question8
#8)bank withdrawal
balance=float(input('Enter account balanve:'))
withdraw=float(input('Enter withdrawal ammount:'))
if withdraw <=0:
    print('Error')
elif withdraw <=balance:
    balance=balance-withdraw
    print('Withdrawal successful.')
    print('New balance:',balance)
else:
    print('Insufficient balance.')    
