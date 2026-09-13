#session_06
#2) Product Inventory
 
inventory={'apple':20,'banana':5,'orange':0,'milk':12,'bread':0}
available=[]
out_of_stock=[]
for product in inventory:
    if inventory[product]>0:
        available.append(product)
    else:
        out_of_stock.append(product)
print('Available:')
for product in available:
    print(product) 
print('Out of stock:')    
for products in out_of_stock:
    print(product)
    
print('Number of available products:',len(available))   
print('Number of out of stock products:',len(out_of_stock)) 
        

