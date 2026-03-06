class T:
    def __init__(s): s.b=[' ']*9
    def p(s):
        for i in range(0,9,3): print(s.b[i],'|',s.b[i+1],'|',s.b[i+2])
        print()
    def w(s,p):
        W=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(s.b[a]==s.b[b]==s.b[c]==p for a,b,c in W)
    def m(s): return [i for i,v in enumerate(s.b) if v==' ']

def ab(g,maxi,a,b):
    if g.w('O'): return 1
    if g.w('X'): return -1
    if not g.m(): return 0
    if maxi:
        v=-9
        for i in g.m():
            g.b[i]='O'
            v=max(v,ab(g,0,a,b))
            g.b[i]=' '; a=max(a,v)
            if b<=a: break
        return v
    else:
        v=9
        for i in g.m():
            g.b[i]='X'
            v=min(v,ab(g,1,a,b))
            g.b[i]=' '; b=min(b,v)
            if b<=a: break
        return v

def best(g,p):
    best=-9 if p=='O' else 9; mv=None
    for i in g.m():
        g.b[i]=p
        v=ab(g,p=='X',-9,9)
        g.b[i]=' '
        if (p=='O' and v>best) or (p=='X' and v<best):
            best=v; mv=i
    return mv

g=T(); p='X'
print("Game Start\n")

while True:
    m=best(g,p)
    g.b[m]=p
    print(p,"moves to",m)
    g.p()
    if g.w(p): print(p,"wins!"); break
    if not g.m(): print("Draw!"); break
    p='O' if p=='X' else 'X'
