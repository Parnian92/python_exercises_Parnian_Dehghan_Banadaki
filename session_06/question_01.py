#session_06
#1)Store Products

products={'laptop': 1200,'phone': 800,'tablet': 500,'headphone': 150,'mouse': 50}

# Most expensive product
most_expensive= max(products,key=products.get)
print('Most expensive:',most_expensive,products[most_expensive])

# Cheapest product
cheapest=min(products,key=products.get)
print('Cheapest:',cheapest,products[cheapest])

# Average price
total=sum(products.values())
average=total/len(products)
print('Average price:',average)

# Products with price greater than 500
print('Products over 500:')
for product in products:
    if products[product]>500:
        print(product,products[product])
        
# Total price
print('Total price:',total)        