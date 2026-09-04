#session_05
#5)Find the Longest Word
sentence=input('Enter a sentence:') 
words= sentence.split()
longest_word= words[0]
for word in words:
    if len(word)>len(longest_word):
        longest_word= word
print('Longest word:',longest_word)    
print('Length:',len(longest_word))    
