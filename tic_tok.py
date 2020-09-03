import sys
import random
def Tik_tac():
    def board():
        print(row[0:3])
        print(row[3:6])
        print(row[6:])
        sys.exit()
    go=0
    game=1
    count=0
    row=[" "," "," "," "," "," "," "," "," "]
    while game==1:
        while go!=1:
            try:
                move=int(input("Which position do you want to put an x in?"))
            except Exception as e:
                print("Enter Right input!")
            try:
                if row[move-1]==" ":
                    row[move-1]="x"
                    go=1
                    count+=1
                else:
                    print("That space has been taken")
            except Exception as e:
                print("Enter Postion in range of 1 to 9 Only!")
            if row[0]=="x" and row[1]=="x" and row[2]=="x":
                print("X wins!")
                board()
            elif row[3]=="x" and row[4]=="x" and row[5]=="x":
                print("X wins!")
                board()
            elif row[6]=="x" and row[7]=="x" and row[8]=="x":
                print("X wins!")
                board()
            elif row[0]=="x" and row[3]=="x" and row[6]=="x":
                print("X wins!")
                board()
            
            elif row[1]=="x" and row[4]=="x" and row[7]=="x":
                print("X wins!")
                board()
            elif row[2]=="x" and row[5]=="x" and row[8]=="x":
                print("X wins!")
                board()
            elif row[0]=="x" and row[4]=="x" and row[8]=="x":
                print("X wins!")
                board()
            elif row[2]=="x" and row[4]=="x" and row[6]=="x":
                print("X wins!")
                board()
            
            
        print(row[0:3])
        print(row[3:6])
        print(row[6:])
        go=0
        if count==9:
            print("Game Over,It's a draw")
            sys.exit()
        while go!=1:
            move= random.randint(1,9)
            print("The CPU has Choose postion:")

            if row[move-1]==" ":
                row[move-1]="o"
                go=1
                count+=1
            else:
                print("That space has been taken")
            if row[0]=="o" and row[1]=="o" and row[2]=="o":
                print("O wins!")
                board()
            elif row[3]=="o" and row[4]=="o" and row[5]=="o":
                print("O wins!")
                board()
            elif row[6]=="o" and row[7]=="o" and row[8]=="o":
                print("O wins!")
                board()
            elif row[0]=="o" and row[3]=="o" and row[6]=="o":
                print("O wins!")
                board()
            elif row[1]=="o" and row[4]=="o" and row[7]=="o":
                print("O wins!")
                board()
            elif row[2]=="o" and row[5]=="o" and row[8]=="o":
                print("O wins!")
                board()
            elif row[0]=="o" and row[4]=="o" and row[8]=="o":
                print("O wins!")
                board()
            elif row[2]=="o" and row[4]=="o" and row[6]=="o":
                print("O wins!")
                board()
        print(row[0:3])
        print(row[3:6])
        print(row[6:])
        go=0
        if count==9:
            print("Game Over,It's a draw")
            sys.exit()
