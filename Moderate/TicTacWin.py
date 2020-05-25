#tic tac toe
#x = 'X', o='O'

def ticTacToe(moves):
    result = []
    n = len(moves)
    dictOfMoves = {i : moves[i] for i in range(0, n) }
    print(dictOfMoves)

a = ('X', 'O', 'X', 'O', 'X', 'O')
ticTacToe(a)
    

