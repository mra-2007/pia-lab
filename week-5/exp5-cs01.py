class CyberSecurityGame:
    def __init__(self):
        self.system = [' '] * 9

    def print_system(self):
        for i in range(0,9,3):
            print(self.system[i:i+3])

    def attacker_win(self):
        win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(self.system[a]==self.system[b]==self.system[c]=='A' for a,b,c in win)

    def defender_win(self):
        win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        return any(self.system[a]==self.system[b]==self.system[c]=='D' for a,b,c in win)

    def full(self):
        return ' ' not in self.system

    def actions(self):
        return [i for i,v in enumerate(self.system) if v==' ']

    def apply_action(self,pos,player):
        self.system[pos]=player

    def undo_action(self,pos):
        self.system[pos]=' '

def minimax(game,is_defender,alpha,beta):
    if game.defender_win(): return 1
    if game.attacker_win(): return -1
    if game.full(): return 0
    if is_defender:
        best = -999
        for move in game.actions():
            game.apply_action(move,'D')
            score = minimax(game,False,alpha,beta)
            game.undo_action(move)
            best = max(best,score)
            alpha = max(alpha,best)
            if beta <= alpha: break
        return best
    else:
        best = 999
        for move in game.actions():
            game.apply_action(move,'A')
            score = minimax(game,True,alpha,beta)
            game.undo_action(move)
            best = min(best,score)
            beta = min(beta,best)
            if beta <= alpha: break
        return best

def best_defense_move(game):
    best_score = -999
    move = None
    for m in game.actions():
        game.apply_action(m,'D')
        score = minimax(game,False,-999,999)
        game.undo_action(m)
        if score > best_score:
            best_score = score
            move = m
    return move

game = CyberSecurityGame()
print("Initial System State:")
game.print_system()
move = best_defense_move(game)
print("\nBest Defense Action: Secure component", move)
