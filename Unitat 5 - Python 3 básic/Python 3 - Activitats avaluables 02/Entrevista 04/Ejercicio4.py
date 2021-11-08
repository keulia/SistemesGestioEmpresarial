n = input("Please enter the number of rows: ")
mine = []
for i in range(int(n)):
    mine.append(list(map(lambda x: int(x),input().split(" "))))
print(mine)
def countMines(mine,rowIndex,columnIndex):
    numberOfMines = 0
    rowIndexUnderflow = False;
    rowIndexOverflow  = False;
    columnIndexUnderflow = False;
    columnIndexOverflow  = False;
    
    if(rowIndex == 0):
        rowIndexUnderflow = True;        
    if(columnIndex == 0):
        columnIndexUnderflow = True;
    if(rowIndex == len(mine) - 1):
        rowIndexOverflow = True;
    if(columnIndex == len(mine[0]) - 1):
        columnIndexOverflow = True;

    if(rowIndexUnderflow):
        if(columnIndexUnderflow):

        if(columnIndexOverflow):
                
     if(mine[rowIndex][columnIndex-1] == -1):
            numberOfMines+=1;

    if(rowIndexOverflow):
        if(columnIndexUnderflow):

        if(columnIndexOverflow):





        if(mine[rowIndex][columnIndex-1] == -1):
            numberOfMines+=1;
        if(mine[rowIndex][columnIndex+1] == -1):
            numberOfMines+=1;
        if(mine[rowIndex+1][columnIndex-1] == -1):
            numberOfMines+=1;
        if(mine[rowIndex+1][columnIndex] == -1):
            numberOfMines+=1;
        if(mine[rowIndex+1][columnIndex+1] == -1):
            numberOfMines+=1;
    if(mine[rowIndex-1][columnIndex-1] == -1):
        numberOfMines+=1;
    if(mine[rowIndex-1][columnIndex] == -1):
        numberOfMines+=1;
    if(mine[rowIndex-1][columnIndex+1] == -1):
        numberOfMines+=1;
   
    return numberOfMines

print(countMines(mine, 1,1));