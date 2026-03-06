class T:
    def __init__(s): s.b=[' ']*9

    def p(s):
        for i in range(0,9,3): print(s.b[i],'|',s.b[i+1],'|',s.b[i+2])
        print()

    def w(s,p):
        W=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(s.b[a]==s.b[b]==s.b[c]==p for a,b,c in W)

    def m(s): return [i for i,v in enumerate(s.b) if v==' ']


def minimax(g,maxi):
    if g.w('O'): return 1
    if g.w('X'): return -1
    if not g.m(): return 0
    best=-9 if maxi else 9
    for i in g.m():
        g.b[i]='O' if maxi else 'X'
        v=minimax(g,not maxi)
        g.b[i]=' '
        best=max(best,v) if maxi else min(best,v)
    return best


def best(g,p):
    best=-9 if p=='O' else 9; move=None
    for i in g.m():
        g.b[i]=p
        v=minimax(g,p=='X')
        g.b[i]=' '
        if (p=='O' and v>best) or (p=='X' and v<best):
            best=v; move=i
    return move


g=T(); p='X'
print("Game Start\n")

while True:
    mv=best(g,p)
    g.b[mv]=p
    print(p,"moves to",mv)
    g.p()

    if g.w(p): print(p,"wins!"); break
    if not g.m(): print("Draw!"); break
    p='O' if p=='X' else 'X'
