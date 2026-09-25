#session_08
#1) Text.users

def add_user():
    username=input('Enter username:')
    user_id=input('Enter user ID:')
    status=input('Enter status (active/blocked):')
    file=open('txt.users','r')
    for line in file:
        data=line.strip().split(',')
        if data[0]==username:
            file.close()
            print('User already exists.')
            return
    file.close()
    
    file=open('txt.users','a')
    file.write('\n'+username+','+user_id+','+status)
    file.close()       
    print('User added successfully.')
    
def find_user():
    username=input('Enter username to find:')
    file=open('txt.users','r')
    for line in file:
        data=line.strip().split(',')
        if data[0]==username:
            print('Username:',data[0])
            print('ID:',data[1])
            print('Status',data[2])
            file.close()
            return
    file.close()
    print('User not found.')      
    
def delete_user():
    username=input('Enter username to delete:')
    file=open('txt.users','r')
    lines=file.readlines()
    file.close()
    found=False
    new_lines=[]
    for line in lines:
        data=line.strip().split(',')
        if data[0]==username:
            found=True
        else: 
            new_lines.append(line)
    file=open('txt.users','w')
    for line in new_lines:
        file.write(line) 
    file.close() 
    if found:
        print('User deleted successfully.')
    else:
        print('User not found.')
        
def generate_report():
    file=open('txt.users','r')
    active_users=0 
    blocked_users=0  
    for line in file:
        data=line.strip().split(',')
        if data[2]=='active':
            active_users+=1
        elif data[2]=='blocked':
            blocked_users+=1
    file.close()
    print('Active users:',active_users)
    print('Blocked users:',blocked_users)
#Test the functions
add_user()
find_user() 
delete_user() 
generate_report()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        