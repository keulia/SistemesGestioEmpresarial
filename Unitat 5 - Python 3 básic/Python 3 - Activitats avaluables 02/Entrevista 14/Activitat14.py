"""
*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧ʕᵔᴥᵔ♥ʔ*˖⁺*˖⁺♡˖°♥°˖✧
|￣￣￣￣￣￣￣￣￣￣￣|
    Exercise 14
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
def anotherQueenCanAttackOnleft(board, row, col):
  for i in range(col):
    if (board[row][i]):
      return True
  return False

def anotherQueenCanAttackUpperLeftDiagonal(board, row, col):
  while row >= 0 and col >= 0:
    if (board[row][col]):
      return True
    row -= 1
    col -= 1
  return False

def anotherQueenCanAttackLowerLeftDiagonal(board, row, col):
  while col >= 0 and row < len(board):
    if (board[row][col]):
      return True
    row += 1
    col -= 1
  return False

def canSafelyPlaceQueen(board, row, col):
  return (
    (not anotherQueenCanAttackOnleft(board, row, col)) and
    (not anotherQueenCanAttackUpperLeftDiagonal(board, row, col)) and
    (not anotherQueenCanAttackLowerLeftDiagonal(board, row, col))
  )

def getQueenCoordinates(board):
  queens = []
  for i in board:
    for j in range(len(i)):
      if i[j] == 1:
        queens.append(j)
  return queens

def rec_nQueens(results, board, col):
  if (col == len(board)):
    results.append(getQueenCoordinates(board))
    return results
  
  for i in range(len(board)):
    if (canSafelyPlaceQueen(board, i, col)):
      board[i][col] = 1
      rec_nQueens(results, board, col + 1)
      board[i][col] = 0
  return results

def findAllSolutions(n):
  board = [[0 for j in range(n)] for i in range(n)]
  results = rec_nQueens([], board, 0)
  return results

def rotate90Deg(list):
  rot = []
  for i in range(len(list)):
    rot.append(len(list) - 1 - list.index(i))
  return rot

def mirror(list):
  mir = [0 for i in list]
  for i in range(len(list)):
    mir[list[i]] = i
  return mir

def generateSymmetricalyEqualSolutions(solution):
  sym = []
  sym.append(solution)
  sym.append(mirror(solution))
  sym.append(rotate90Deg(solution))
  sym.append(mirror(rotate90Deg(solution)))
  sym.append(rotate90Deg(rotate90Deg(solution)))
  sym.append(mirror(rotate90Deg(rotate90Deg(solution))))
  sym.append(rotate90Deg(rotate90Deg(rotate90Deg(solution))))
  sym.append(mirror(rotate90Deg(rotate90Deg(rotate90Deg(solution)))))
  return sym;

def findFundamentalSolutions(n):
  solutions = findAllSolutions(n)
  fundamentalSolutions = []
  for i in range(len(solutions)):
    found = False
    for symmetrical in generateSymmetricalyEqualSolutions(solutions[i]):
      if symmetrical in fundamentalSolutions:
        found = True
        break
    if not found:
      fundamentalSolutions.append(solutions[i])
  return fundamentalSolutions

for i in range(4, 11):
  print("Amount of fundamental solutions for {0} queens on a {0}X{0} board is {1}".format(i, len(findFundamentalSolutions(i))))


# SOUT:
# Amount of fundamental solutions for 4 queens on a 4X4 board is 1
# Amount of fundamental solutions for 5 queens on a 5X5 board is 2
# Amount of fundamental solutions for 6 queens on a 6X6 board is 1
# Amount of fundamental solutions for 7 queens on a 7X7 board is 6
# Amount of fundamental solutions for 8 queens on a 8X8 board is 12
# Amount of fundamental solutions for 9 queens on a 9X9 board is 46
# Amount of fundamental solutions for 10 queens on a 10X10 board is 92

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