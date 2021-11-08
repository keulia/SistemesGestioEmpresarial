"""
*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
|￣￣￣￣￣￣￣￣￣￣￣|
    Exercise 2
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
"""
# We create a dictionary with the values of the keys being set to False. Every time a number appears the value of the number will
# get changed to True

# If we find a value that is "False" then we will return False.

# Check Row
def checkRow(sudoku, rowIndex):
    # Dictionary with the numbers
    numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False,'8': False, '9': False}
    # Changing the values to True in case we find the number
    for i in range(9):
        numbers[sudoku[rowIndex][i]] = True;
    # If we have a value False it will return False
    for key in numbers.keys():
        if(numbers[key] == False):
            return False;
    # If every value is True it will return True
    return True;

# Check Columns - We do the same as we did in Check Row
def checkColumn(sudoku, columnIndex):
    numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False,'8': False, '9': False}
    for i in range(9):
        numbers[sudoku[i][columnIndex]] = True;
    #print(numbers)
    for key in numbers.keys():
        if(numbers[key] == False):
            return False;
    
    return True;

# Check Square - We follow a similar logic as we did earlier 
def checkSquare(sudoku, rowIndex, columnIndex):
    numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False,'8': False, '9': False}
    # We create 2 loops to check information inside a square so we can check 0,0 - 0,1 - 0,2 - 1,0 - 1,1 - 1,2 etc...
    for i in range(columnIndex, columnIndex + 3):
        for j in range(rowIndex, rowIndex + 3):
            numbers[sudoku[j][i]] = True
    for key in numbers.keys():
        if(not numbers[key]): # Same thing as "if(numbers[key] == False)"
            return False;
    
    return True;

# Reading the sudoku file
my_file_handler=open("E:\\escritorio\\Estudios\\2GS\\Sistemes de gestió empresarial\\p2\\Sudoku.in")

# Creating the sudoku array
sudoku = []
# Loop to go through each sudoku line
for i in range(9):          
    sudoku.append(my_file_handler.readline().strip().split(" ")) # With strip we are removing "\n" and with "split" we are splitting them after a spacebar
    

isSudokuValid = True; # We define it to True
for i in range(9):
    if( not checkRow(sudoku, i) or not checkColumn(sudoku,i)): 
        isSudokuValid = False; # If we find a False return we will change the value of isSudokuValid to False
        break;
if(isSudokuValid):
    # In case checkRow and checkColumn both work, we will check the squares
    for i in range(0,7,3): #since our square goes from 1 to 9, the values it will start from will be "0 - 3 - 6" that's why we add 3 after each loop
        for j in range(0,7,3):
            if(not checkSquare(sudoku, i,j)):
                isSudokuValid = False;
                break;
if(isSudokuValid):
    print("Sudoku is Valid")
else:
    print("Sudoku is invalid")
    
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