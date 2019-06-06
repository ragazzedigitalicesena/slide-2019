import random
import sys

#1

def drawBoard(board):
    print(' 12345678')
    print(' +--------+')
    for y in range(#1):
        print('%s|' % (y+1), end='')
        for x in range(#1):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print(' 12345678')

def getNewBoard():

    board = []
    for x in range(#1):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):

    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    
    #2

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction.
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0: 
        return False
    return tilesToFlip

def isOnBoard(x, y):
    return x >= 0 and x <= #1 - 1 and y >= 0 and y <= #1 - 1

def getBoardCopy(board):
#3 - Funzione che crea e ritorna una copia di una board passata in input

def getBoardWithValidMoves(board, tile):
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    validMoves = []
    for x in range(#1):
        for y in range(#1):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    #4
    return {'X':xscore, 'O':oscore}
 
def enterPlayerTile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #5

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile

    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def isOnCorner(x, y):

    return (x == 0 or x == #1 - 1) and (y == 0 or y == #1 - 1)

def getPlayerMove(board, playerTile):
     DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        
        #6

        #7
        
    return [x, y]

def getComputerMove(board, computerTile):

    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, playerTile, computerTile):
    #8

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')

    #9
    
    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board

        elif turn == 'player':
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                print("move[0]  %s" % move[0] + "  move[1]  %s" % move[1])
                if move == 'quit':
                    print('Thanks for playing!')
                    sys.exit()
                elif move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    print("move[0]  %s" % move[0] + "  move[1]  %s" % move[1])
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'computer'

        elif turn == 'computer':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Press Enter to see the computer\'s move.')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'player'

print('Welcome to Reversegam!')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    
    #10

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break