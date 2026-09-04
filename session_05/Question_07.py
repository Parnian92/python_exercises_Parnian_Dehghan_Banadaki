#session_05
# 7) Compress Consecutive Characters
text=input('Enter a string:')
result=''
count=1
for i in range(len(text)):
    if i<len(text)-1 and text[i]==text[i+1]:
        count+=1
    else:
        result+=text[i]+str(count)
        count=1
print('compressed string:',result)       
 
        

