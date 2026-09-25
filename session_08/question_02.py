#session_08
#2) Text.logs

def count_successful_logins():
    file=open('txt.logs','r')
    count=0
    for line in file:
        data=line.strip().split(',')
        username=data[0]
        operation=data[1]
        status=int(data[2])
        
        if operation=='LOGIN' and status==200:
            count+=1
    file.close()
    return count

def count_failed_logins():
    file=open('txt.logs','r')
    count=0 
    for line in file:
        data=line.strip().split(',')
        username=data[0]
        operation=data[1]
        status=int(data[2])           
        
        if operation=='LOGIN' and status==403:
            count+=1
    file.close() 
    return count

def find_suspicious_users():
    file=open('txt.logs','r')
    users=[]
    failed_counts=[]
    for line in file:
        data=line.strip().split(',')
        username=data[0]
        operation=data[1]
        status=int(data[2])
        if operation=='LOGIN' and status==403:
            if username not in users:
                users.append(username)
                failed_counts.append(1)
            else:
               index=users.index(username)
               failed_counts[index]+=1
    file.close()
    suspicious_users=[]
    for i in range(len(users)):
        if failed_counts[i]>=3:
            suspicious_users.append(users[i])   
    return suspicious_users

def generate_report():
    successful_logins=count_successful_logins()
    failed_logins=count_failed_logins()
    suspicious_users=find_suspicious_users()
    file=open('txt.logs','r')
    users=[]
    operation_counts=[]
    for line in file:
        data=line.strip().split(',') 
        username=data[0] 
        if username not in users:
            users.append(username)
            operation_counts.append(1)
        else:
            index=users.index(username)
            operation_counts[index]+=1
    file.close()
    print('Final Report')
    print('--------------------------------------------')    
    print('Successful logins:',successful_logins)    
    print('Failed logins:',failed_logins)   
    print('Suspicious users:')
    if len(suspicious_users)==0:
        print('None')
    else:
        for user in suspicious_users:
            print(user)
    print('Operations per user:')   
    for i in range(len(users)):
        print(users[i],':',operation_counts[i])  
#Run the report
generate_report()        
            



















         