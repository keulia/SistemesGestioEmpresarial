"""
Sudoku exercise - thinking
--En el 2, creamos nosotros manualmente el sudoku o el programa debe crear el sudoku?
create a method with each type of value from 1 to 9
in case a value is there it will add an int one=1
if every value is bigger than 1 then program says "Wrong"
else "Correct!"
"""


# Check Row
def checkRow(sudoku, rowIndex):
    numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False,'8': False, '9': False}
    for i in range(9):
        numbers[sudoku[rowIndex][i]] = True;
    #print(numbers)
    for key in numbers.keys():
        if(numbers[key] == False):
            return False;
    
    return True;

# Check Columns
def checkColumn(sudoku, columnIndex):
    numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False,'8': False, '9': False}
    for i in range(9):
        numbers[sudoku[i][columnIndex]] = True;
    #print(numbers)
    for key in numbers.keys():
        if(numbers[key] == False):
            return False;
    
    return True;

# Check Square
def checkSquare(sudoku, rowIndex, columnIndex):
    numbers = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False,'8': False, '9': False}
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
    

isSudokuValid = True;
for i in range(9):
    if( not checkRow(sudoku, i) or not checkColumn(sudoku,i)): 
        isSudokuValid = False;
        break;
if(isSudokuValid):
    for i in range(0,7,3):
        for j in range(0,7,3):
            if(not checkSquare(sudoku, i,j)):
                isSudokuValid = False;
                break;
if(isSudokuValid):
    print("Sudoku is Valid")
else:
    print("Sudoku is invalid")