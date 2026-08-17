#sessio_3 Question2
#2)high jump record
record=0
for i in range(10):
    jump=float(input('enter jump height:'))
    if jump>record:
        record=jump
        print('new record:',record)
    else:
        print('less than the current record.')
