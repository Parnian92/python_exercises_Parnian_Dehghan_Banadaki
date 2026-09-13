#session_06
#3) Count characters with dictionary

text=input('Enter a string:')
characters={}
for char in text:
    if char.isalpha():
        if char in characters:
            characters[char]+=1
        else:
            characters[char]=1
print(characters)            
