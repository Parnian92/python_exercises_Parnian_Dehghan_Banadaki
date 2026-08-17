#sessio_3 Question5
#5)simple calculator 
num1=float(input('enter first number:'))
num2=float(input('enter second number:'))
op=input('enter operator(+-*/):')
if op=='+':
    print('result:',num1+num2)
elif op=='-':
    print('result:',num1-num2)
elif op=='*':
    print('result:',num1*num2)
elif op=='/':
    if num2!=0:
      print('result:',num1/num2)
    else:
        print('division by zero is not allowed!')
else:
   print('invalid operator.')        
    