eng = "AaBCcEeHKMOoPpTXxy"
ru = "АаВСсЕеНКМОоРрТХху"

a, b, c = [input() for _ in range(3)]

if a in eng and b in eng and c in eng:
    print('en')
elif a in ru and b in ru and c in ru:
    print('ru')
else:
    print('mix')
