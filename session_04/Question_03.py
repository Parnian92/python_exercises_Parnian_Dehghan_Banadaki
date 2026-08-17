#session_04
#3) Password Validation
password=input('Enter password:')
if len(password)== 8 and password[:4].isalpha() and password[4:].isdigit():
    print('Valid')
else:
    print('Invalid')
    
