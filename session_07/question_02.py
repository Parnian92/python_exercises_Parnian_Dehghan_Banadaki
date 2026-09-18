#session_07
# 2) Order Processing
def process_order(customer, *products, **options):
    discount=options.get('discount',0)
    tax=options.get('tax',0)
    shipping=options.get('shipping',0)
    prices={'Laptop':1200,'Mouse':50,'Keyboard':100}
    total_price=0
    for product in products:
        if product in prices:
            total_price+=prices[product]
    discount_amount=total_price*discount/100
    price_after_discount=total_price-discount_amount
    tax_amount=price_after_discount*tax/100
    final_price=price_after_discount+tax_amount+shipping
    result={'customer':customer,'discount':discount,'tax':tax,'shipping':shipping,\
    'final_price':final_price}
    return result
order=process_order('Ali','Laptop','Keyboard',discount=10,tax=9,shipping=200000)
print(order)        