#session_08
#4) Unique Values

def get_values():
    values=[]
    number=int(input('Enter the number of values:'))
    for i in range(number):
        value=input('Enter value'+str(i+1)+':')
        values.append(value)
    return values
 
def add_unique(value,unique_values):
    if value.strip()=='':
        print('Empty value is not allowed.')
        return False
    value_lower=value.lower()
    for i in range(len(unique_values)):
        if unique_values[i].lower()==value_lower:
            print('Duplicate value. first entered at position',i+1)
            return False
    unique_values.append(value)
    print('New value added ->',value)
    return True

def process_values(values):
    unique_values=[]
    unique_count=0 
    duplicated_count=0
    first_positions=[]
    for i in range(len(values)):
        value=values[i]
        result=add_unique(value,unique_values)
        if result==True:
            unique_count+=1
            first_positions.append(i+1)
        else:
            if value.strip() !='':
                duplicated_count+=1
    return unique_values, unique_count, duplicated_count, first_positions

def show_report(unique_values, unique_count, duplicated_count, first_positions):
    print()
    print('Final Report')
    print('---------------------------------------')         
    print('Unique values:',unique_values)
    print('Number of duplicate values:',duplicated_count)
    print('Number of unique values:',unique_count)
    print('First positions:')
    for i in range(len(unique_values)):
        print(unique_values[i], '->', first_positions[i])
# Main program
values=get_values()
unique_values, unique_count, duplicated_count, first_positions= process_values(values)  
show_report(unique_values, unique_count, duplicated_count, first_positions)      
            
    