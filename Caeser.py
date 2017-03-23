print'Gib den zu codierenden Text ein (keine Umlaute)'
s=raw_input('')
s1=s.lower()
print'gib die zahl ein um die die Buchstaben verschober werden sollen'
a=input('')

def codieren (s1):
    s2=''
    for i in xrange (len(s1)):
        c=s1[i]
        x=ord(c)
        y=x+a
        y=y-122
        if x==32:
            pass
        elif x+a>122:
            x=97+y-1
        elif x==46:
            pass
        elif x==44:
            pass
        else:
            x=x+a
        q=chr(x)
        s2=s2+q
    print s2
    
codieren(s1)
