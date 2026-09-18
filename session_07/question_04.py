#session_07
#4) Fraud Detection

transactions = [("Ali", "deposit", 50000000, 10),("Ali", "withdraw", 2000000, 11),\
("Ali", "withdraw", 3000000, 12),("Ali", "withdraw", 4000000, 13),\
("Ali", "withdraw", 5000000, 14),("Ali", "withdraw", 6000000, 15),\
("Sara", "deposit", 50000000, 20),("Sara", "withdraw", 60000000, 21),\
("Reza", "deposit", 150000000, 30)]

def check_large_transaction(transaction):
    amount = transaction[2]
    if amount > 100000000:
        return True
    return False

def check_repeated_withdrawals(withdrawal_count):
    if withdrawal_count > 3:
        return True
    return False

def check_balance(balance, amount):
    if amount > balance:
        return True
    return False

def generate_fraud_report(transactions):

    suspicious_transactions = []
    all_transactions = []
    balances = {}
    withdrawal_count = {}

    for transaction in transactions:
        all_transactions.append(transaction)

        username = transaction[0]
        transaction_type = transaction[1]
        amount = transaction[2]

        if username not in balances:
            balances[username] = 0
            withdrawal_count[username] = 0

        large_transaction = check_large_transaction(transaction)

        if transaction_type == "deposit":
            if large_transaction:
                suspicious_transactions.append(transaction)

            balances[username] += amount
            withdrawal_count[username] = 0
        elif transaction_type == "withdraw":
            withdrawal_count[username] += 1

            repeated_withdrawals = check_repeated_withdrawals(withdrawal_count[username])
            balance_problem = check_balance(balances[username],amount)

            if large_transaction or repeated_withdrawals or balance_problem:
                suspicious_transactions.append(transaction)
            balances[username] -= amount

    report = {"all_transactions": all_transactions,\
          "suspicious_transactions": suspicious_transactions}
    return report

def detect_fraud(transactions):
    fraud_report = generate_fraud_report(transactions)
    return fraud_report
fraud_report = detect_fraud(transactions)
print("All Transactions:")

for transaction in fraud_report["all_transactions"]:
    print(transaction)
print()
print("Suspicious Transactions:")
for transaction in fraud_report["suspicious_transactions"]:
    print(transaction)
