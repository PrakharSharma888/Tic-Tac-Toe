str = ["-","-","-","-","-","-","-","-","-"]
player1 = True
print("Enter Name of Player 1")
play1 = input()
print("Enter Name of Player 2")
play2 = input()
player = play1
def display():
    print(str[0],"|",str[1],"|",str[2])
    print(str[3],"|",str[4],"|",str[5])
    print(str[6], "|", str[7], "|",str[8])

draw = False
even = 0
winner = None
def playgame():
    global player
    global move
    global chancep1
    global chancep2
    global checking
    if even == 0:
        display()
    winner_rows()
    tie()
    if draw == True:
        print("Game Tied! No one wins")
    else:
        if winner == play1 or winner == play2:
            end()
        else:
            print(player+"'s chance")
            print("Select your position")
            move = int(input())
            move -= 1
            check()
            if player == play1:
                chancep1 = True
                chancep2 = False
                chance()
            else:
                chancep1 = False
                chancep2 = True
                chance()

def chance():
    global even
    global checking
    if chancep1 == True:
        if checking == False:
            str[move] = str[move]
        else:
            str[move]="X"
        i=0
        while i<9:
            print(str[i], "|", str[i+1], "|", str[i+2])
            i += 3
            print(str[i], "|", str[i+1], "|", str[i+2])
            i += 3
            print(str[i], "|", str[i+1], "|", str[i+2])
            i += 3

        if checking == False:
            playgame()
        else:
            even += 1
            change_player()

    elif chancep2 == True:
        if checking == False:
            str[move] = str[move]
        else:
            str[move]="0"
        i = 0
        while i < 9:
            print(str[i], "|", str[i + 1], "|", str[i + 2])
            i += 3
            print(str[i], "|", str[i + 1], "|", str[i + 2])
            i += 3
            print(str[i], "|", str[i + 1], "|", str[i + 2])
            i += 3

        if checking == False:
            playgame()
        else:
            even += 1
            change_player()
def change_player():
    global player1
    global player2
    global player
    global even
    if even % 2==0:
        player1 = True
        player2 = False
        player = play1
        playgame()
    else:
        player2 = True
        player1 = False
        player = play2
        playgame()


def check():
    global move
    global checking
    if str[move] == 'X' or str[move] == '0':
        print("Invalid move")
        checking = False
    else:
        checking = True

def winner_rows():
    i=0
    global winner
    while i<9:
        if str[i]==str[i+1]==str[i+2] != '-':
            if str[i]=='X':
                winner = play1
            else:
                winner = play2
        elif str[i+3]==str[i+4]==str[i+5] != '-':
            if str[i+3]=='X':
                winner = play1
            else:
                winner = play2
        elif str[i+6]==str[i+7]==str[i+8] != '-':
            if str[i+6]=='X':
                winner = play1
            else:
                winner = play2
        i = 9
    winner_col()

def winner_col():
    i = 0
    global winner
    while i<9:
        if str[i]==str[i+3]==str[i+6] != '-':
            if str[i]=='X':
                winner = play1
            else:
                winner = play2
        if str[i+1]==str[i+4]==str[i+7] != '-':
            if str[i+1]=='X':
                winner = play1
            else:
                winner = play2
        if str[i+2]==str[i+5]==str[i+8] != '-':
            if str[i+2]=='X':
                winner = play1
            else:
                winner = play2
        i = 9
    winner_diagonal()

def winner_diagonal():
    i = 0
    global winner
    while i < 9:
        if str[i] == str[i + 4] == str[i + 8] != '-':
            if str[i] == 'X':
                winner = play1
            else:
                winner = play2
        if str[i + 2] == str[i + 4] == str[i + 6] != '-':
            if str[i + 2] == 'X':
                winner = play1
            else:
                winner = play2
        i = 9
    return winner

def tie():
    global draw
    if "-" not in str:
        draw = True

def end():
    if winner == play1:
        print(play1,"is the winner")
    elif winner == play2:
        print(play2,"is the winner")

playgame()#stating point
