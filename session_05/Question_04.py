#session_05
# 4) Most Repeated Word
sentence=input('Enter a sentence:')
words= sentence.lower().split()
most_repeated=''
max_count=0
for word in words:
    count= words.count(word)
    if count > max_count:
        max_count= count
        most_repeated= word
print(most_repeated,'->',max_count)        
        
