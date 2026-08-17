#5) barnameyi benevisid masafat tey shode bar hasb km begirad.agar masafat kamtar az 2km bud keraye sabet 20000 toman bashad. dar gheyre in surat be ezaye har km ezafe, 5000 toman keraye ezafe shavad. keraye nahayi ra chap namayid.
distance=float(input('enter distance(km):'))
if distance<2:
    fare=20000
    print('final fare:',fare,'tooman')
else:
    fare=20000+(distance-2)*5000
    print('final fare:',fare,'tooman')
