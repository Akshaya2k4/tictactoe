import random
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
cp="X"
winner=None
gr=True

#printing the game board
def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("------------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("------------")
    print(board[6]+" | "+board[7]+" | "+board[8])

#take a player input
def pI(board):
    inp=int(input("select a spot 1-9:"))
    if board[inp-1]=="-":
        board[inp-1]=cp
    else:
        print("Oops player is already at that spot")

#check for win or tie

def ch(board):
    global winner
    if(board[0]==board[1]==board[2] and board[0]!="-"):
        winner=board[0]
        return True
    elif(board[3]==board[4]==board[5] and board[3]!="-"):
        winner=board[3]
        return True
    elif(board[6]==board[7]==board[8] and board[6]!="-"):
        winner=board[6]
        return True

def cr(board):
    global winner
    if(board[0]==board[3]==board[6] and board[0]!="-"):
        winner=board[0]
        return True
    elif(board[1]==board[4]==board[7] and board[1]!="-"):
        winner=board[1]
        return True
    elif(board[2]==board[5]==board[8] and board[2]!="-"):
        winner=board[2]
        return True

def cd(board):
    global winner
    if(board[0]==board[4]==board[8] and board[0]!="-"):
        winner=board[0]
        return True
    elif(board[2]==board[4]==board[6] and board[4]!="-"):
        winner=board[3]
        return True

def checkIfWin(board):
    global g
    if(ch(board)):
        printBoard(board)
        print("The winner is (winner)!")
        g=False
    elif(cr(board)):
        printBoard(board)
        print("The winner is (winner)!")
        g=False
    elif(cd(board)):
        printBoard(board)
        print("The winner is (winner)!")
        g=False


def checkIfTie(board):
    global g
    if("-" not in board):
        printBoard(board)
        print("It is a tie!")
        g=False

        
 #switch player

def sp():
    global cp
    if(cp=="X"):
        cp="O"
    else:
        cp="X"

def computer(board):
    while(cp=="O"):
        position=random.randint(0,8)
        if(board[position]=="-"):
            board[position]="O"
            sp()
while gr:
    printBoard(board)
    pI(board)
    checkIfWin(board)
    checkIfTie(board)
    sp()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)
    
