#Tic Tac Toe

board = [' ' for x in range (10)]

def insertLetter (letter, pos):
    board [pos] = letter 

def spaceIsFree (pos):
    return board[pos] == ' '

def printBoard(board):
    print('  |  |') 
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print ('  |  |')
    print('-----------')
    print('  |  |')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print ('  |  |')
    print('-----------')
    print('  |  |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('  |  |')


    def isWinner(bo, le):
        return (bo[7] == le and bo [8] == le and bo [9] == le) (bo [4] == le and bo [5] == le and bo [6] == le) (bo [1] == le and bo [2] == le and bo [3] == le) (bo [1] == le and bo [4] == le and bo [7] == le) (bo [2] == le and bo [5] == le and bo [8] == le) (bo [3] == le and bo [6] == le and bo [9] == le) (bo [1] == le and bo [5] == le and bo [9] == le) (bo [3] == le and bo [5] == le and bo [7] == le)

        def playerMove():
            run = True
            while run:
                move = input ('Select a position to place an \'X\'(1-9): ')
                try:
                    Move = int (move)
                    if move > 0 and move < 10:
                        if spaceIsFree (move):
                            run = False
                            insertLetter ('x', move)

#Feedback for the user
                        else:
                            print ('Sorry, this space is full!')
                    else:
                        print ('Please type a number within the range!')

                except:
                    print ('Please type a number!')



def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
