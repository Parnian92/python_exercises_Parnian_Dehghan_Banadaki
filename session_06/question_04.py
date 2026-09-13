#session_06
#4) Employee Information

employees={'E01':{'name':'Ali','age':28,'salary':3000},'E02':{'name':'Sara','age':32,\
'salary':4500},'E03':{'name':'Reza','age':25,'salary':2800}}                                                                  

#Employee with the highest salary
highest_salary=0 
highest_employee=''
for employee in employees:
    if employees[employee]['salary']>highest_salary:
       highest_salary=employees[employee]['salary']
       highest_employee=employees[employee]['name']
print('Highest salary:',highest_employee, highest_salary)       

#Average salary
total_salary=0
for employee in employees:
    total_salary+=employees[employee]['salary']
    
average_salary=total_salary/len(employees)
print('Average salary:',average_salary)

#Employees with salary greater than 3000

print('employees with salary greater than 3000:') 
for employee in employees:
    if employees[employee]['salary']>3000:
        print(employees[employee]['name'])

#Employee with the lowest salary
lowest_salary=100000
lowest_employee=''
for employee in employees:
    if employees[employee]['salary']<lowest_salary:
        lowest_salary=employees[employee]['salary']
        lowest_employee=employees[employee]['name']
print('Lowest salary employee:',lowest_employee)        