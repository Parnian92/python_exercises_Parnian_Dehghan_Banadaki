#session_05
# 9) Login System-Maximum 3 Attempts
correct_username='admin'
correct_password='1234'
max_attempt=3
for attempt in range(max_attempt):
    username=input('Enter username:')
    password=input('Enter password:')
    if username==correct_username and password==correct_password:
        print('Login successful')
        break
    else:
        attempts_remaining=max_attempt-attempt-1
        print('Wrong username or password')
        print('Attempts remaining:',attempts_remaining)
else:
    print('Account locked')        

