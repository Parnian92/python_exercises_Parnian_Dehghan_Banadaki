#session_06
#9) Product Inventory Analysis
products={'P01':('Laptop',1200,5),'P02':('Phone',800,0),'P03':('Tablet',500,12),'P04':\
('Mouse',50,25),'P05':('Keyboard',100,0)}
total_warehouse_value=0 
highest_value=0 
highest_product=''
print('Available products:')  
for product_id in products:
    product=products[product_id]
    name=product[0]
    price=product[1]
    stock=product[2]
    if stock>0:
        print(name)
print('Out of stock products:')
for product_id in products:
    product=products[product_id]
    name=product[0]
    price=product[1]
    stock=product[2]      
    if stock==0:
        print(name)
print('Inventory value:')        
for product_id in products:
    product=products[product_id]
    name=product[0]
    price=product[1]
    stock=product[2] 
    value=price*stock
    print(name,'->',value)
    total_warehouse_value+=value
    if value>highest_value:
        highest_value=value
        highest_product=name
print('Product with the highest inventory value:',highest_product)
print('Highest inventory value:',highest_value)
print('Total warehouse value:',total_warehouse_value)        
    
    