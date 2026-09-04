#session_05
# 8) Text Report
text=input('Enter a text:')
words= text.split()
letters=0
digits=0
spaces=0
uppercase=0
lowercase=0
#count characters
for char in text:
    if char.isalpha():
        letters+=1
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowercase+=1
    elif char.isdigit():
        digits+=1
    elif char==' ':
        spaces+=1
# Most repeated character        
most_repeated_character=''
max_character_count=0
for char in text:       
    if char !=' ':
        count=text.count(char)
        if count> max_character_count:
            max_character_count=count
            most_repeated_character=char
# Most repeated word
most_repeated_word=''
max_word_count=0
for word in words:
    count=words.count(word)
    if count>max_word_count:
        max_word_count=count
        most_repeated_word=word
# Longest word
longest_word=words[0]
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
# Shortest word
shortest_word= words[0]
for word in words:
    if len(word)<len(shortest_word):
        shortest_word=word  
print('Total characters:',len(text))
print('Total words:',len(words))
print('Total letters:',letters)     
print('Total digits:',digits)
print('Total spaces:',spaces)
print('Total uppercase:',uppercase)
print('Total lowercase:',lowercase)
print('Longest word:',longest_word)
print('Shortest word:',shortest_word)
print('Most repeated character:',most_repeated_character)
print('Most repeated word:',most_repeated_word)   
            
       


