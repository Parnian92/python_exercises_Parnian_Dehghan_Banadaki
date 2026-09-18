#session_07
#5) Log Analysis
def analyze_logs(logs):
    successful_logins = 0
    failed_logins = 0
    user_operations = {}
    user_errors = {}

    for log in logs:
        username, operation, status = log
        if username not in user_operations:
            user_operations[username] = 0
        user_operations[username] += 1

        if operation == "LOGIN":
            if status == 200:
                successful_logins += 1
            elif status == 403:
                failed_logins += 1
                if username not in user_errors:
                    user_errors[username] = 0
                user_errors[username] += 1

    suspicious_users = []
    for username in user_errors:
        if user_errors[username] >= 3:
            suspicious_users.append(username)
    report = {"successful_logins": successful_logins,"failed_logins": failed_logins,\
              "suspicious_users": suspicious_users,"user_operations": user_operations}
    return report

logs = [("Ali", "LOGIN", 200),("Ali", "DOWNLOAD", 200),("Sara", "LOGIN", 403),\
        ("Reza", "LOGIN", 200),("Sara", "LOGIN", 403),("Sara", "LOGIN", 403)]

report = analyze_logs(logs)
print("Final Report:")
print(report)
