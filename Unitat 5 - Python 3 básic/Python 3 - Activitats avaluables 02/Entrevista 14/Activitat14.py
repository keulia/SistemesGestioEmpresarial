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
# Here we check if there is another queen placed on the `board`
# that would attack the one we are trying to place at (row, col)
# from the left
def anotherQueenCanAttackOnleft(board, row, col):
  for i in range(col):
    if (board[row][i]):
      return True
  return False

# Here we check if there is another queen placed on the `board`
# that would attack the one we are trying to place at (row, col)
# from the upper diagonal
def anotherQueenCanAttackUpperLeftDiagonal(board, row, col):
  while row >= 0 and col >= 0:
    if (board[row][col]):
      return True
    row -= 1
    col -= 1
  return False

# Here we check if there is another queen placed on the `board`
# that would attack the one we are trying to place at (row, col)
# from the lower diagonal
def anotherQueenCanAttackLowerLeftDiagonal(board, row, col):
  while col >= 0 and row < len(board):
    if (board[row][col]):
      return True
    row += 1
    col -= 1


# Call the previous "checks" in conjunction. This function is not strictly necessary, but
# makes the code more readablereturn False
def canSafelyPlaceQueen(board, row, col):
  return (
    (not anotherQueenCanAttackOnleft(board, row, col)) and
    (not anotherQueenCanAttackUpperLeftDiagonal(board, row, col)) and
    (not anotherQueenCanAttackLowerLeftDiagonal(board, row, col))
  )
# Generates a flat list of col coordinates for what cols currently have queens
# This function is not strictly necessary, but makes the code more readable
def getQueenCoordinates(board):
  queens = []
  for i in board:
    for j in range(len(i)):
      if i[j] == 1:
        queens.append(j)
  return queens
# This is the main function for generating all the possible queen locations.
# It is a recursive function that has it's end condition set at "col" == len(board)
# which means that we have generated our first board and can add it to our results list
def rec_nQueens(results, board, col):
  if (col == len(board)):
    results.append(getQueenCoordinates(board))
    return results
   # for each row in our current col, check where we can place our queen
  # this is exhaustive as we will try to call canSafelyPlaceQueen() for all possible values
  for i in range(len(board)):
    if (canSafelyPlaceQueen(board, i, col)):
      board[i][col] = 1
      rec_nQueens(results, board, col + 1)
      board[i][col] = 0
  return results
# Starter function for finding all possible locations that a queen can be placed.
# It just kicks of the recursive function "rec_nQueens" by starting at col 0
# Oh and it also generets the "board"
def findAllSolutions(n):
  board = [[0 for j in range(n)] for i in range(n)]
  results = rec_nQueens([], board, 0)
  return results

# Helper function for rotation queen positions by 90 degrees.
# This is also known as a C4 rotation (https://en.wikipedia.org/wiki/Rotational_symmetry)
def rotate90Deg(list):
  rot = []
  for i in range(len(list)):
    rot.append(len(list) - 1 - list.index(i))
  return rot
# Helper function for mirroring our queen posistions.
def mirror(list):
  mir = [0 for i in list]
  for i in range(len(list)):
    mir[list[i]] = i
  return mir

# Helper function for generating ALL symmetrical permutations of a single board-solution
# This could be optimized a bit more, but the function is not that exhaustive
#
# https://en.wikipedia.org/wiki/Eight_queens_puzzle has a piece stating:
# > A fundamental solution usually has eight variants (including its original form) obtained by
# > rotating 90, 180, or 270° and then reflecting each of the four rotational variants in a mirror in a fixed position.
# > However, should a solution be equivalent to its own 90° rotation (as happens to one solution with five queens on a 5×5 board),
# > that fundamental solution will have only two variants (itself and its reflection).
# > Should a solution be equivalent to its own 180° rotation (but not to its 90° rotation),
# > it will have four variants (itself and its reflection, its 90° rotation and the reflection of that).
# > If n > 1, it is not possible for a solution to be equivalent to its own reflection because that would require two queens to be facing each other.
#
# This is just the implementation fo all the rortation/mirroring rules, where 90+90deg = 180deg and 90+90+90deg = 270deg
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

# Starter function for finding all fundamental solutions.
# It starts off by finding ALL possible solutions, and then filters the solutions into a new array
# where symmetry is not allowed
def findFundamentalSolutions(n):
    # Find ALL solutions
  solutions = findAllSolutions(n)
  fundamentalSolutions = []
  for i in range(len(solutions)):
    found = False
    # For each possible solution, generate all the possible symmetrical variants of said solution
    for symmetrical in generateSymmetricalyEqualSolutions(solutions[i]):
      # If we already have one of the symmetrical solutions in our "fundamentalSolutions", we can say it is "found"
      # and we DON't want to add it again.
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