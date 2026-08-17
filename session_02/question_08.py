#8) saati beyne 0 ta 23 az karbar begirid va baze zamani rooz(sobh,zohr,asr,shab) ra tayin namayid.hamchenin agar adad kharej az baze motabar bud, payame khata chap namayad.
hour=int(input('enter the time(0-23):' ))
if 0<=hour<6:
    print('night')
elif 6<=hour<12:
    print('morning')
elif 12<=hour<17:
    print('noon')
elif 17<=hour<21:
    print('evining')
elif 21<=hour<=23:
    print('night')
else:
    print('the time is out of range')
