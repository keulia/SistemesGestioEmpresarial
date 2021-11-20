"""
*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
|￣￣￣￣￣￣￣￣￣￣￣|
    Exercise 4
|＿＿＿＿＿＿＿＿＿＿＿|
⠀⠀⠀⠀⠀⠀(\__/) ||
⠀⠀⠀⠀⠀⠀(•ㅅ•) ||
⠀⠀⠀⠀⠀⠀/ 　 づ

Author: Cassandra Sowa Candela ♡ ´･ᴗ･ `♡
2ºDAM
November 2021

⠀                                                 ⠀∩∩
                                                ♡(｡･x･)♡  

   ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄                                                                     ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄ 
   █▒▒░░░░░░░░░▒▒█                                                                     █▒▒░░░░░░░░░▒▒█
    █░░█░░░░░█░░█                                                                       █░░█░░░░░█░░█
 ▄▄  █░░░▀█▀░░░█  ▄▄                                                                 ▄▄  █░░░▀█▀░░░█  ▄▄
█░░█ ▀▄░░░░░░░▄▀ █░░█                                                               █░░█ ▀▄░░░░░░░▄▀ █░░█

*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡


Fill the mines
INPUT: 
0  0  0 0 0
0 -1 -1 0 0
0  0  0 0 0

OUTPUT:
1  2  2 1 0
1 -1 -1 1 0 
1  2  2 1 0

"""


n = input("Please enter the number of rows: ") # We are asking the user 
mine = []
for i in range(int(n)):
    mine.append(list(map(lambda x: int(x),input().split(" ")))) # We will add the numbers the user will type into "mine". with map we will change the typed numbers from a string into an int and with "split" we will split by the space
rowSize = int(n) # The amount of rows we have
columnSize = len(mine[0]) # how many numbers do we have per line

# We will print the mine
def printMine(mine): 
    print("\n Printing Mine")
    for i in range(rowSize):
        print (mine[i])

printMine(mine)


# We will counnt the mines next to a 0
def countMines(i, j):
    numberOfMines = 0
    hasTop = False # Line above 
    hasBottom =  False # Underneath line
    hasLeft = False
    hasRight = False

    if i > 0: # If i is higher than 0 it means it's the 2nd row or higher so it DOES have a top
        hasTop = True
    if i < rowSize - 1: # If i is smaller than the row size - 1 it means it has a bottom
        hasBottom = True   
    if j > 0: # if j is bigger than 0 it means there's a number on its left side
        hasLeft = True
    if j < columnSize - 1: # if j is smaller than columnSize -1 it means there's a number on its right side
        hasRight = True    

# Checking diagonally 
    if hasTop:
        if mine[i-1][j] == -1:
            numberOfMines+=1
        if hasLeft:
            if mine[i-1][j-1] == -1:
                numberOfMines+=1
        if hasRight:
            if mine[i-1][j+1] == -1:
                numberOfMines+=1
    if hasBottom:
        if mine[i+1][j] == -1:
            numberOfMines+=1
        if hasLeft:
            if mine[i+1][j-1] == -1:
                numberOfMines+=1
        if hasRight:
            if mine[i+1][j+1] == -1:
                numberOfMines+=1        
    # Checking on the sides 
    if hasLeft:
        if mine[i][j-1] == -1:
            numberOfMines+=1  
    if hasRight:
        if mine[i][j+1] == -1:
            numberOfMines+=1  
    return numberOfMines

# We are changing the 0 with numbers depending on how many mines there are next to it
for i in range(int(n)):
    for j in range(len(mine[i])):
        if mine[i][j] == 0:
            mine[i][j] = countMines(i ,j)         

printMine(mine)

"""
*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡*✲ﾟ*｡⋆♡
⠀⠀⠀⠀°. ♡
⠀⠀⠀⠀. °
⠀⠀＿♡
⊂⊂ ・）
⠀/　 |
⊂＿__u

*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
"""