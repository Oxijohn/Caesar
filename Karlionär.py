# -*- coding: cp1252 -*-
from random import randrange*
# 1. Eingabe der Klartextes und des gewünschten Schlüssels und umwandelung des String in eine
#       Liste und die Schlüssellänge umgewandelt

# variationen von i sind für die schleifen
# s = schlüssel ss = schlüssel in string sll = schlüssellänge slz = schlüssellänge als zeichen
# sl =schlüssel als liste

print'Gib den zu codierenden Text ein (keine Umlaute)'
text = raw_input('')
liste = text.split()

print'Gib den Schlüssel an (Zahl maximal 226 Zahlen lang)'

if s>226:
    print'die Zahl ist zu groß'
else:
    s = raw_input('')
    # splitt nach jedem Zeichen
    sl = list(s)
    # bis 33 sind keine lesbaren zeichen codiert deswegen +32
    sll = len(s)+32
    slz = chr(sll)
    


# 2. herausnahme,verschiebung und wiedereinfügung
#   der einzelnen Wörter (ein wort selbe verschiebung)
#   http://python4kids.net/how2think/kap08.htm


# zvw = zu veränderdes Wort zz = Zufallszahl ll = länge der Liste wn = wort nummer
# ver = verschiebung sz = schlüsselzahl vl = verschlüsselte liste vln = verschlüsselte listennummer
# verschlüsselter Text zz2 = Zufallszahl2 zzs =zufallszahl in string

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


# 3. und einfügen eines Zufälligen Buchstabens an zufälliger stelle in das Wort
#   (position wird ausgegeben und teil des Schlüssels)

# 4. zuasmmenfühgen der Liste zum Sting und generierung des entgültigen Schlüssels




# Liste zu string

stringliste = ""
for i in xrange (len(stringliste)):
    stringliste = stringliste+str(i)
print stringliste

# string zu liste

a='Gib den zu codierenden Text ein (keine Umlaute)'
print a.split()

#bis die ganze liste gezeigt ist
# len(horsemen) = länge der Liste

i = 0
while i < len(horsemen):
  print horsemen[i]
  i = i + 1 

# zahl zu string
str(133)
