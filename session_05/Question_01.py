#session_05
#1)Password Validation
password=input('Enter your password:')
errors=[]
if len(password)<8:
    errors.append('Pasword must contain at least 8 characters')
upper= False
lower= False
digit= False
special= False
for char in password:
    if char.isalpha():
       if char>= 'A' and char <= 'Z':
          upper=True
       else:
          lower=True
    elif char.isdigit():
        digit=True
    elif not char.isalnum():
        special=True
if upper==False:
   errors.append('Password must contain at least one uppercase letter')        
if lower==False:
   errors.append('Password must contain at least one lowercase letter ') 
if digit==False:
   errors.append('Password must contain at least one digit')   
if special==False:
    errors.append('Password must contain at least a special character')
if len(errors)==0:
   print('Password is valid')   
else:
    print('Password is invalid')
    for error in errors:
        print('-', error)
    
