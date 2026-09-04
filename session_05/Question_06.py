#session_05
# 6) Find Special Words and Count Them
text=input('Enter a text:').lower()
target_words=['hack','fraud','scam','password','atack']
words=text.split()
for target in target_words:
    count=words.count(target)
    if count>0:
        print(target,'->',count)