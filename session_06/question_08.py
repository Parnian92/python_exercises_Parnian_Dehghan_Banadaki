#session_06
#8) Group Users by Programming Language
users=[('Ali',25,'Python'),('Sara',30,'Java'),('Reza',22,'Python'),('Mina',28,'C++'),\
('John',35,'Python'),('David',30,'Java')]
language_users={}
#Group users by language
for user in users:
    name=user[0]
    language=user[2]
    if language in language_users:
        language_users[language].append(name)
    else:
        language_users[language]=[name]
print('Users by language:')
print(language_users)
#Average age of each language
for language in language_users:
    total_age=0
    count=0
    for user in users:
        if user[2]==language:
            total_age+=user[1]
            count+=1
    if count>0:
        average_age=total_age/count        
    print(language,'Average age:',average_age)        
#Oldest user of each language
for language in language_users:
    oldest_name=''
    oldest_age=0
    for user in users:
        if user[2]==language:
            if user[1]>oldest_age:
               oldest_age=user[1]
               oldest_name=user[0]
    print(language,'oldest user:',oldest_name)       
#language with the most users
most_users=0 
most_used_language='' 
for language in language_users:
    if len(language_users[language])>most_users:
       most_users=len(language_users[language]) 
       most_used_language=language
print('Language with the most users:',most_used_language)  
#All programming languages
print('Programming language:')
for language in language_users:
    print(language)     