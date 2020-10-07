import random

def Print(board):
    for i in (7,4,1):
        print("\n{}\t{}\t{}\n".format(board[i],board[i+1],board[i+2]))
        
def player1(board):
    choice=int(input("Enter your move, player 1:"))
    while board[choice]!=None:
        choice=int(input("Enter an valid move please: "))
    board[choice]='X'
    Print(board)

def player2(board,p):
    if(p==2):
        choice=int(input("Enter your move, player 2:"))
        while board[choice]!=None:
            choice=int(input("Enter an valid move please: "))
    elif(p==1):
        print("Computers Move:")
        choice=random.randrange(1,10)
        while board[choice]!=None:
            choice=random.randrange(1,10)
    board[choice]='O'
    Print(board)

def play(p):
    if(p!=1 and p!=2):
        print("Invalid number of players")
        return;
    boxes=list(range(1,10))
    turns=1
    board={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
    while(turns<=9):
        if turns%2==1:
            player1(board)
        if turns%2==0:
            player2(board,p)
        if win(board)==True:
            break
        turns+=1
    if turns==10:
        print("Its a draw!")

def win(board):
    comb=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3)]
    for a,b,c in comb:
        if(board[a]=='X' and board[b]=='X' and board[c]=='X'):
            print("Player 1 wins!")
            return True
        if(board[a]=='O' and board[b]=='O' and board[c]=='O'):
            print("Player 2 wins!")
            return True
    return False

p=int(input("Welcome to tic tac toe. Please enter the number of players to play (one or two):"))
play(p)