#TA
#4)
products=[]
answer=input('Aya mikhahid mahsool ezafe konid?(yes/no):')
answer=answer.strip().lower()
if answer=='yes':
    product=input('Esme mahsool ra vared konid:')
    products.append(product)
elif answer=='no':
    print('Mamnoon az kharid shoma.')
else:
    print('Faghat ba yes va no javab dahid.')    

