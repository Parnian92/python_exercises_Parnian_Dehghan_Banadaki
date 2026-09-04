#session_05
#2) Remove Repeated Characters
text=input('Enter:')
result=''
for char in text:
    if char not in result:
        result+=char
print('Result:',result)        
        
