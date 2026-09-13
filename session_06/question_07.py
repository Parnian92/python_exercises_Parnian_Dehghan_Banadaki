#session_06
#7) Group orders
orders=[('Ali','Laptop'),('Sara','Phone'),('Ali','Phone'),('Reza','Laptop'),('Sara','Laptop')\
,('Ali','Tablet'),('Reza','Phone')]

customer_orders={}
for order in orders:
    customer=order[0]
    product=order[1]
    if customer in customer_orders:
        customer_orders[customer].append(product)
    else:
        customer_orders[customer]=[product]
print(customer_orders)        