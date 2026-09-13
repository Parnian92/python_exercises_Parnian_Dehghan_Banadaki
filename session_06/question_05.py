#session_06
#5) Student Information
students={'Ali':[18,17,20],'Sara':[15,19,18],'Reza':[12,14,10],'Mina':[20,20,19]}
best_student=''
highest_average=0
for student in students:
    grades=students[student]
    total=grades[0]+grades[1]+grades[2]
    for grade in grades:
        total+=1
    average=total/len(grades) 
    highest_grade=max(grades)
    if average>=15:
        status='Passed'
    else:
        status='Failed'
    print(student) 
    print('Average:',round(average,2))
    print('Status:',status)
    print('Highest grade:',highest_grade)
    print()
    
    if average>highest_average:
        highest_average=average
        best_student=student
print('Best student:',best_student)
print('Highest average:',round(highest_average,2))        