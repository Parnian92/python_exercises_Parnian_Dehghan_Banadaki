#session_07
#3) Transaction Analysis

transactions = [("Ali", "deposit", 5000000),("Ali", "withdraw", 1000000),\
                ("Sara", "deposit", 8000000),("Ali", "withdraw", 500000),\
                ("Sara", "withdraw", 2000000),("Reza", "deposit", 10000000)]
def analyze_transactions(transactions):
    users = {}
    for transaction in transactions:
        username, transaction_type, amount = transaction
        if username not in users:
            users[username] = {"deposits": 0,"withdrawals": 0,"balance_change": 0,\
                               "transactions": 0}
        users[username]["transactions"] += 1    
        if transaction_type == "deposit":
            users[username]["deposits"] += amount
            users[username]["balance_change"] += amount
        elif transaction_type == "withdraw":
            users[username]["withdrawals"] += amount
            users[username]["balance_change"] -= amount
            
    highest_deposit_user = ""
    highest_deposit = 0
    
    highest_withdrawal_user = ""
    highest_withdrawal = 0
    
    most_active_user = ""
    most_active_transactions = 0
    
    for username in users:
        if users[username]["deposits"] > highest_deposit:
            highest_deposit = users[username]["deposits"]
            highest_deposit_user = username
            
        if users[username]["withdrawals"] > highest_withdrawal:
            highest_withdrawal = users[username]["withdrawals"]
            highest_withdrawal_user = username
            
        if users[username]["transactions"] > most_active_transactions:
            most_active_transactions = users[username]["transactions"]
            most_active_user = username
            
    result = {"users": users,"highest_deposit": {"user": highest_deposit_user,\
              "amount": highest_deposit},"highest_withdrawal": {\
              "user": highest_withdrawal_user,"amount": highest_withdrawal},\
              "most_active_user": {"user": most_active_user,\
              "transactions": most_active_transactions}}
    return result
report = analyze_transactions(transactions)
print(report)