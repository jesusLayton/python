from random import randrange

print("+-------" * 3,"+")
for row in range(3):
    print("|       " * 3,"|")
    for col in range(3):
        print("|   " + str(board[row][col]) + "   ",end="")
    print("|")
    print("|       " * 3,"|",sep="")
    print("+-------" * 3,"+",sep="")
