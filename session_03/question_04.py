#sessio_3 Question4
#4)string length
text=input('enter a string:')
length=len(text)
if length%2==0:
    print(text[:length//2])
else:
    print(text[length//2:])

