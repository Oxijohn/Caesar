# -*- coding: cp1252 -*-
from random import randrange*
# 1. Eingabe der Klartextes und des gew�nschten Schl�ssels und umwandelung des String in eine
#       Liste und die Schl�ssell�nge umgewandelt

# variationen von i sind f�r die schleifen
# s = schl�ssel ss = schl�ssel in string sll = schl�ssell�nge slz = schl�ssell�nge als zeichen
# sl =schl�ssel als liste

print'Gib den zu codierenden Text ein (keine Umlaute)'
text = raw_input('')
liste = text.split()

print'Gib den Schl�ssel an (Zahl maximal 226 Zahlen lang)'

if s>226:
    print'die Zahl ist zu gro�'
else:
    s = raw_input('')
    # splitt nach jedem Zeichen
    sl = list(s)
    # bis 33 sind keine lesbaren zeichen codiert deswegen +32
    sll = len(s)+32
    slz = chr(sll)
    


# 2. herausnahme,verschiebung und wiedereinf�gung
#   der einzelnen W�rter (ein wort selbe verschiebung)
#   http://python4kids.net/how2think/kap08.htm


# zvw = zu ver�nderdes Wort zz = Zufallszahl ll = l�nge der Liste wn = wort nummer
# ver = verschiebung sz = schl�sselzahl vl = verschl�sselte liste vln = verschl�sselte listennummer
# verschl�sselter Text zz2 = Zufallszahl2 zzs =zufallszahl in string

    vl = []
    ll=len(liste)
    wn=0
    sz=0
    vln=0
    i2=0
    while i2 < ll:
        zvw = liste[wn]
        # verschiebung (links)
        zvw2=''
        ver=int(float(sl[sz]))
        for i in xrange (len(zvw)):
            c=zvw[i]
            x=ord(c)
            y=x+ver
            y=y-97
            if x==32:
                pass
              elif x-ver<97:
                x=122-y+1
            elif x==46:
                pass
            elif x==44:
                pass
            else:
                x=x-ver
            q=chr(x)
            zvw2=zvw2+q
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


# 3. und einf�gen eines Zuf�lligen Buchstabens an zuf�lliger stelle in das Wort
#   (position wird ausgegeben und teil des Schl�ssels)

# 4. zuasmmenf�hgen der Liste zum Sting und generierung des entg�ltigen Schl�ssels




# Liste zu string

stringliste = ""
for i in xrange (len(stringliste)):
    stringliste = stringliste+str(i)
print stringliste

# string zu liste

a='Gib den zu codierenden Text ein (keine Umlaute)'
print a.split()

#bis die ganze liste gezeigt ist
# len(horsemen) = l�nge der Liste

i = 0
while i < len(horsemen):
  print horsemen[i]
  i = i + 1 

# zahl zu string
str(133)
