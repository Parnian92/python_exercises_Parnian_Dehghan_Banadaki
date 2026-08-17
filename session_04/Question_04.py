#session_04
#4) Sum Numbers Until Zero
total=0
while True:
    number=float(input('Enter a number:'))
    if number==0:
        break
    total=total+number
print('The sum is:',total)    
