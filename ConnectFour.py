# Establish Board
Board = [["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
         ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
         ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"], ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]]
numbers=[" 0","  1","  2","  3","  4","  5","  6 "]

#Display Board
def printboard():
    print(numbers)
    for i in Board:
        row = i
        print(row[:])

#Player Turns, alternate between X and O
def turns():
    global Player_1
    if Player_1==True:
        symbol="[X]"
        column=int(input("What Column Do You Want To Place A Piece at?: "))
        while column < 0 or column > 6:
            print("Please choose a number between 0 and 6")
            column = (int(input()))
        for i in reversed(Board):
            row=i
            if row[column]=="[ ]":
                row[column]="[X]"
                Player_1 = False
                return Board
                break

    if Player_1==False:
        symbol="[O]"
        column=int(input("What Column Do You Want To Place A Piece at?: "))
        while column < 0 or column > 6:
            print("Please choose a number between 0 and 6")
            column = (int(input()))
        for i in reversed(Board):
            row=i
            if row[column]=="[ ]":
                row[column]="[O]"
                Player_1=True
                return Board
                break


def horizontal():
    global win
    #Check Horizontal
    for y in Board:
        i=0
        while i<7:
            if y[i:i+4]==["[X]","[X]","[X]","[X]"] or y[i:i+4]==["[O]","[O]","[O]","[O]"]:
                win=True
                return win
                break
            else:
                i=i+1
    return win
def vertical():
    global win
    #Check Vertical
    i=0
    while i<7:
        column = []
        for y in Board:
            column.append(y[i])
        num=0
        while num < 6:
            if column[num:num + 4] == ["[X]", "[X]", "[X]", "[X]"] or column[num:num + 4] == ["[O]", "[O]", "[O]", "[O]"]:
                win = True
                return win
                break
            else:
                num = num + 1
        i=i+1
    return win
def right_dia():
    # Check / diagnols
    global win
    x = 0
    while x <= 3:
        y = 5
        while y >= 0:
            check = []
            row_1=Board[y]
            check.append(row_1[x])
            row_2=Board[y-1]
            check.append(row_2[x+1])
            row_3=Board[y-2]
            check.append(row_3[x+2])
            row_4=Board[y-3]
            check.append(row_4[x+3])
            if check[0:4] == ["[X]", "[X]", "[X]", "[X]"] or check[0:4] == ["[O]", "[O]", "[O]", "[O]"]:
                win = True
                return win
                break
            else:
                y-=1
        x+=1
def left_dia():
    #Check \ diagnols
    global win
    x = -1
    while x >= -4:
        y = 5
        while y >= 0:
            check = []
            row_1=Board[y]
            check.append(row_1[x])
            row_2=Board[y-1]
            check.append(row_2[x-1])
            row_3=Board[y-2]
            check.append(row_3[x-2])
            row_4=Board[y-3]
            check.append(row_4[x-3])
            if check[0:4] == ["[X]", "[X]", "[X]", "[X]"] or check[0:4] == ["[O]", "[O]", "[O]", "[O]"]:
                win = True
                return win
                break
            else:
                y-=1
        x-=1
Player_1=True
win=False

#Determine if there are no plays left and if the board is full
def full():
    global tie
    tie=False
    for row in Board:
        if "[ ]" in row:
            tie=False
            return tie
        else:
            tie=True
            return tie


def play():
    global win
    while win!=True:
        printboard()
        turns()
        win=vertical()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        win=horizontal()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        win = right_dia()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        win = left_dia()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        full()
        if tie == True:
            print("Its a tie!")
            printboard()
            quit()
        printboard()
        turns()
        win=vertical()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        win = horizontal()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        win = right_dia()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        win = left_dia()
        if win == True:
            print("Game Over!")
            printboard()
            quit()
        full()
        if tie==True:
            print("Its a tie!")
            printboard()
            quit()

play()