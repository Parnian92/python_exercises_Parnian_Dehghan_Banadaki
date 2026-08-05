#TA
#5)
products=[]
answer=input('Aya mikhahid kharid konid?(yes/no):')
answer=answer.strip().lower()
if answer=='yes':
    name=input('Esme mahsool ra vared konid:')
    price=float(input('Gheymat mahsool ra vared konid:'))
    product={'name':name,'price':price}
    products.append(product)
    print('Mahsool ba movafaghiyat ezafe shod.')
    print('Sabad kharid:')
    for item in products:
        print(item['name'],'-',item['price'])
elif answer=='no':
     print('Mamnoon az shoma.Khodahafez!')
else:
    print('Lotfan faghat yes ya no vared konid.')        
    

