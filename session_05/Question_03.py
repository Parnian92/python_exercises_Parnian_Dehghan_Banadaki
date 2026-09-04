#session_05
#3) Count Letters,Upercase,Lowercase,Digits,Spaces and Special Characters
text=input('Enter a string:')
letters=0
lowercase=0
uppercase=0
digits=0
spaces=0
special=0
for char in text:
    if 'a' <=char <='z':
        lowercase +=1
        letters +=1
    elif 'A' <= char <= 'Z':
            uppercase +=1
            letters +=1
    elif char.isdigit():
         digits +=1
    elif char==' ':
         spaces +=1          
    else:
        special +=1
print('Letters:',letters)  
print('Uppercase:',uppercase)
print('Lowercase:',lowercase) 
print('Digits:',digits)
print('Spaces:',spaces)
print('Special:',special)
     
        
         