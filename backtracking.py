def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(row, col, nd, rd, rowLookup, ndLookup, rdLookup):
    if (ndLookup[nd[row][col]] or rdLookup[rd[row][col]] or rowLookup[row]):
        return False
    return True

def solveNQueensUtil(board, col, nd, rd, rowLookup, ndLookup, rdLookup):
    if (col >= N):
        return True
    for i in range(N):
        if (isSafe(i, col, nd, rd, rowLookup, ndLookup, rdLookup)):
            board[i][col] = 1
            rowLookup[i] = True
            ndLookup[nd[i][col]] = True
            rdLookup[rd[i][col]] = True
            if (solveNQueensUtil(board, col + 1, nd, rd, rowLookup, ndLookup, rdLookup)):
                return True
            board[i][col] = 0
            rowLookup[i] = False
            ndLookup[nd[i][col]] = False
            rdLookup[rd[i][col]] = False
    return False

def solveNQueens(N):
    board = [[0 for i in range(N)] for j in range(N)]
    nd = [[0 for i in range(N)] for j in range(N)]
    rd = [[0 for i in range(N)] for j in range(N)]
    rowLookup = [False] * N
    x = 2 * N - 1
    ndLookup = [False] * x
    rdLookup = [False] * x
    for r in range(N):
        for c in range(N):
            nd[r][c] = r + c
            rd[r][c] = r - c + N - 1
    if (solveNQueensUtil(board, 0, nd, rd, rowLookup, ndLookup, rdLookup) == False):
        print("Solution does not exist")
        return False

    printSolution(board)
    return True

while True:
    N = int(input("Enter a Number: "))
    solveNQueens(N)
    ch = input("Do you want to continue? (y/n): ")
    if ch != 'y':
        break

#-----------------------------------------------------------------------------

# OUTPUT:
# Enter a Number: 5
# 1 0 0 0 0
# 0 0 0 1 0
# 0 1 0 0 0
# 0 0 0 0 1
# 0 0 1 0 0
# Do you want to continue? (y/n): N


# -------------------------------------------------------------------------------

# WHAT IS N queen's BRANCH AND BOUND?
# In the N-Queens problem with branch and bound, the goal is to find an optimal placement of N queens on an N x N chessboard, where no two queens threaten each other. The branch and bound technique is used to systematically explore the solution space and efficiently search for the best solution. It involves dividing the problem into smaller subproblems (branches) and using bounds or heuristics to prune branches that cannot lead to an optimal solution. This approach helps to narrow down the search space and find the optimal solution more efficiently.

# -------------------------------------------------------------------------------

# WHAT IS NQUEEN'S PROBLEM WITH BACKTRACKING?
# The N-Queens problem with backtracking is a variation of the N-Queens problem where the backtracking algorithm is used to find all possible solutions. Backtracking involves trying different options, undoing choices that lead to conflicts, and exploring alternative possibilities until a valid solution is found or all possibilities are exhausted. It efficiently prunes the search space by eliminating branches that cannot lead to a valid solution. The goal is to place N queens on an N x N chessboard such that no two queens threaten each other (no conflicts in rows, columns, or diagonals).

# -------------------------------------------------------------------------------

## WHAT IS THE DIFFERENCE BETWEEN NQUEEN BACKTRACKING AND BRANCH AND BOUND?
# ANS) The main difference between N-Queens backtracking and branch and bound lies in their approach to finding solutions and optimizing the search process.
#
# Backtracking:
#
# Backtracking is a general algorithmic technique used to explore all possible solutions by incrementally building a solution and undoing choices when they lead to a dead end.
# In N-Queens backtracking, the algorithm systematically tries different positions for each queen and backtracks when it encounters conflicts or reaches an invalid state.
# Backtracking explores the entire search space, considering all possible solutions, and finds a valid solution without any specific optimization strategy.
# It may have a high time complexity due to the exhaustive exploration of all possible combinations.

# Branch and Bound:
#
# Branch and bound is an algorithmic technique used for optimization problems, where the goal is to find the best solution among all possible solutions.
# Branch and bound intelligently explores the solution space by breaking it down into smaller subspaces (branches) and uses bounds or heuristics to prune branches that are guaranteed to be worse than the current best solution.
# In N-Queens branch and bound, the algorithm still tries different positions for each queen, but it uses bounds or heuristics to eliminate branches that cannot lead to an optimal solution, thus reducing the search space.
# Branch and bound aims to find an optimal solution efficiently by avoiding unnecessary exploration of the entire search space.
# In summary, backtracking focuses on finding any valid solution by exhaustively exploring all possibilities and backtracking when necessary, while branch and bound aims to find the best solution by intelligently pruning branches that cannot yield an optimal solution, resulting in a more efficient search process.

# -------------------------------------------------------------------------------

# EXPLAINATION:
# Here's a detailed explanation of the code:
#
# The printSolution function iterates over the chessboard and prints each cell's value, which represents whether a queen is placed in that position or not.
#
# The isSafe function checks if it is safe to place a queen at a given position on the chessboard. It takes the current row, column, and lookup arrays for diagonal and reverse diagonal checks. It returns True if the position is safe (i.e., no other queens can attack it) and False otherwise.
#
# The solveNQueensUtil function is the main recursive function that tries to place queens on the chessboard. It takes the chessboard, the current column, lookup arrays, and the diagonal and reverse diagonal matrices.
#
# The base case is when the current column exceeds or is equal to the total number of columns (i.e., col >= N). In this case, it means all queens have been successfully placed on the board, so it returns True to indicate a solution has been found.
#
# It iterates over each row in the current column (for i in range(N)).
#
# For each row, it checks if it is safe to place a queen at that position using the isSafe function. If it is safe, the code proceeds with the following steps; otherwise, it continues to the next iteration.
#
# If it is safe to place a queen at the current position, the code updates the chessboard, lookup arrays, and diagonal matrices accordingly.
#
# It then makes a recursive call to solveNQueensUtil with the updated parameters, incrementing the column by 1. If the recursive call returns True, it means a solution has been found, so the code returns True.
#
# If the recursive call does not return True, it means a solution has not been found yet. In this case, the code backtracks by undoing the changes made to the chessboard, lookup arrays, and diagonal matrices (setting them back to their previous state).
#
# If all the rows have been explored in the current column without finding a solution, the code returns False.
#
# The solveNQueens function is the entry point of the program. It initializes the chessboard, lookup arrays, and diagonal matrices. It also sets up the nd (normal diagonal) and rd (reverse diagonal) matrices to store the respective diagonals for each cell.
#
# It prompts the user to enter the value of N, which represents the size of the chessboard and the number of queens to be placed.
#
# It calls the solveNQueensUtil function with the initial parameters to find a solution. If a solution is found, it prints the chessboard configuration using the printSolution function. If a solution does not exist, it prints a message indicating that no solution was found.
#
# After each iteration, it asks the user if they want to continue solving the N-Queens problem with a different N value. If the user enters 'y', the loop continues; otherwise, it breaks, and the program ends.