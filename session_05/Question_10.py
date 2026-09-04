#session_05
# 10) Find Common Words Between Two Sentences
sentence1=input('Sentence1:').lower()
sentence2=input('Sentence2:').lower()
for char in'.,!?:;':
    sentence1=sentence1.replace(char,'')
    sentence2=sentence2.replace(char,'')
words1=sentence1.lower().split() 
words2=sentence2.lower().split()
common_words=[]
for word1 in words1:
    for word2 in words2:
        if word1==word2: 
            if word1 not in common_words:
                common_words.append(word1)
print('Common words:')
for word in common_words:
     print(word)        


