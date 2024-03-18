"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]:
        return X

    if terminal(board):
        return 0

    vazio = 0

    for row in board:
        for element in row:
            if element == EMPTY:
                vazio +=1

    if (vazio // 2 == 0):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    if terminal(board):
        return 0

    actions = set()

    #nao sei se esta certo 
    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    state = copy.deepcopy(board)

    jogador = player(board)

    if jogador == 0:
        raise NameError("Jogada inválida")

    state[action[0]][action[1]] = jogador

    return state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    tabuleiro = board

    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != EMPTY:
            return linha[0]

    # Verifica as colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != EMPTY:
            return tabuleiro[0][coluna]

    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != EMPTY:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != EMPTY:
        return tabuleiro[0][2]

    # Se não houver vencedor, retorna None
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #Se há um vencedor, jogo acabou
    if (winner(board) != None):
        return True
    

    for linha in board:
        for celula in linha:
            if celula == EMPTY:
                #Jogo nao acabou, ainda tem pelo menos uma celular vazia
                return False

    #Jogo acabou empatdo
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if (terminal(board)):
        return None

    jogador = player(board)

    if (jogador == X):
        value, move =  MaxValue(board)
    else:
        value, move = MinValue(board)
    
    return move


def MaxValue(state):

    if terminal(state):
        return utility(state)

    v = (-1) * math.inf

    move = None

    for action in actions(state):
        aux, action = MinValue( result(state, action) )

        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move


    return v, move

def MinValue(state):

    if (terminal(state)):
        return utility(state)

    v = math.inf

    for action in actions(state):
        aux, action = MaxValue( result(state, action) )

        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    
    return v, move

