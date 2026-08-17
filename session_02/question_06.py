#6) barnameyi benevisid ke mablagh kharid az karbar begirad. agar balaye 1 million tooman bud 15% takhfif, beyne 500000 ta 1 million 10% takhfif va kamtar az an bedoon takhfif emal shavad. mablagh nahayi chap shavad.
price=int(input('enter the price:'))    
if price>1000000:
    final_price=price*0.85
    print('final price:',final_price,'tooman')
elif price>500000:
    final_price=price*0.9
    print('final price:',final_price,'tooman')
else:
    final_price=price
    print('final price:',final_price,'tooman')
