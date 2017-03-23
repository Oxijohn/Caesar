# -*- coding: cp1252 -*-
from random import randrange

text = raw_input('')    
liste = text.split()

s = raw_input('')
sl = list(s)

zz1 = randrange(9)
zzs1 = str(zz1)
zz2 = randrange(9)
zzs2 = str(zz2)

if len(sl) == 1:
    sl[0:0] = zzs1
    sl[1:1] = zzs2
if len(sl) == 2:
    sl[1:1] = zzs1
else:
    pass

    
sll = 2+32
vl = []
ll = len(liste)
wn = 0
sz = 0
vln = 0
i2 = 0
i4 = 0
e32 = 1
while i2 < ll:
    zvw = liste[wn]
    # verschiebung (rechts)
    zvw2=''
    ver=int(float(sl[sz]))
    print 1
    for i in xrange (len(zvw)):
        c=zvw[i]
        x=ord(c)
        y=x+ver
        y=y-122
        if x==32:
            pass
        elif x-ver>122:
            x=97+y-1
        elif x==46:
            pass
        elif x==44:
            pass
        else:
            x=x+ver
        q=chr(x)
        zvw2=zvw2+q
    print zvw2
    wn = wn+1
    if sz==sll-32:
        sz=0
    else:
        sz=sz+1
    i2=i2+1
    vl[0:0] = zvw2
    if i2<ll:
        vl[0:0] = chr(32)
    else:
        pass
  
print vl
vt = ""
for i3 in vl:
    vt = vt+str(i3)
print vt

vl2 = vt.split()
vl2.reverse()
print vl2

e33 = len(vl2) + len(vl2) - 1

while e32 < e33:
    vl2[e32:e32] = chr(32)
    e32 = e32 + 2

vt2 = ""
for i4 in vl2:
    vt2 = vt2+str(i4)
print vt2
