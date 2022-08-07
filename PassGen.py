import random

large = list('ABCDEFGHIJKLNOPQRSTUVWXYZ')
small = list('abcdefghijklmnopqrstuvwxyz')
num = list('1234567890')
spec = list('!@#$%^&*[]}{::?/')

lsn = large + small + num
snsp = small + num + spec
nsl = num + small + large
lssp = large + small + spec
lnsp = large + num + spec

char = small + large + num + spec

def passw(lenn):
    if lenn <= 4:
        return 'Choose a length more than 4!'
        pass
    else:
            

        temp = ''

        temp += random.choice(char)

        for i in range(4):
            if temp[-1] in large:
                temp += random.choice(snsp)
            elif temp[-1] in small:
                temp += random.choice(lnsp)
            elif temp[-1] in num:
                temp += random.choice(lssp)
            elif temp[-1] in spec:
                temp += random.choice(nsl)

        for i in range(lenn - 5):
            if temp[-1] in large:
                temp += random.choice(snsp)
            elif temp[-1] in small:
                temp += random.choice(lnsp)
            elif temp[-1] in num:
                temp += random.choice(lssp)
            elif temp[-1] in spec:
                temp += random.choice(nsl)

        return temp



while True:
    lenn = int(input("enter the length of your pw: "))
    print(passw(lenn))
