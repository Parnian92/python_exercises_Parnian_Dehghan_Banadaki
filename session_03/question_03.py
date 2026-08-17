#sessio_3 Question3
#3)numbers from 1 to 10
total=0
for i in range(1,11):
    if i%2==1:
        result=i*5
        print(i,'*5=',result)
    else:
        result=i+5
        print(i,'+5',result)
    total+=result
print('sum=',total)
    
    