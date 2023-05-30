#Branch and Bound
def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def is_safe(row, col, queens):
    for i in range(col):
        if queens[i] == row or queens[i] - row == i - col or queens[i] - row == col - i:
            return False
    return True

def solve_nqueens_util(col, queens, row_lookup, nd_lookup, rd_lookup):
    if col >= N:
        return True

    for row in range(N):
        if row_lookup[row] and nd_lookup[row + col] and rd_lookup[row - col]:
            queens[col] = row
            row_lookup[row] = False
            nd_lookup[row + col] = False
            rd_lookup[row - col] = False

            if solve_nqueens_util(col + 1, queens, row_lookup, nd_lookup, rd_lookup):
                return True

            queens[col] = -1
            row_lookup[row] = True
            nd_lookup[row + col] = True
            rd_lookup[row - col] = True

    return False

def solve_nqueens(N):
    queens = [-1] * N
    row_lookup = [True] * N
    nd_lookup = [True] * (2 * N - 1)
    rd_lookup = [True] * (2 * N - 1)

    if not solve_nqueens_util(0, queens, row_lookup, nd_lookup, rd_lookup):
        print("Solution does not exist")
        return False

    board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        board[queens[i]][i] = 1

    print_solution(board)
    return True

while True:
    N = int(input("Enter a Number: "))
    solve_nqueens(N)
    ch = input("Do you want to continue? (y/n): ")
    if ch != 'y':
        break

# -------------------------------------------------------------------------------

# OUTPUT:

# Enter a Number: 5
# 1 0 1 0 0
# 0 0 0 0 0
# 0 1 0 0 1
# 0 0 0 1 0
# 0 0 0 0 0
# Do you want to continue? (y/n): n

# -------------------------------------------------------------------------------

# WHAT IS N queen's BRANCH AND BOUND?
# In the N-Queens problem with branch and bound, the goal is to find an optimal placement of N queens on an N x N chessboard, where no two queens threaten each other. The branch and bound technique is used to systematically explore the solution space and efficiently search for the best solution. It involves dividing the problem into smaller subproblems (branches) and using bounds or heuristics to prune branches that cannot lead to an optimal solution. This approach helps to narrow down the search space and find the optimal solution more efficiently.

# -------------------------------------------------------------------------------

# WHAT IS NQUEEN'S PROBLEM WITH BACKTRACKING?
# The N-Queens problem with backtracking is a variation of the N-Queens problem where the backtracking algorithm is used to find all possible solutions. Backtracking involves trying different options, undoing choices that lead to conflicts, and exploring alternative possibilities until a valid solution is found or all possibilities are exhausted. It efficiently prunes the search space by eliminating branches that cannot lead to a valid solution. The goal is to place N queens on an N x N chessboard such that no two queens threaten each other (no conflicts in rows, columns, or diagonals).

# -------------------------------------------------------------------------------

## WHAT IS THE DIFFERENCE BETWEEN NQUEEN BACKTRACKING AND BRANCH AND BOUND?
# The main difference between N-Queens backtracking and branch and bound lies in their approach to finding solutions and optimizing the search process.
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
# Certainly! Here's an explanation of the code:
#
# 1. The `print_solution` function is responsible for printing the chessboard configuration. It iterates over each row and column of the board and prints the value at each position, representing whether a queen is present (1) or not (0).
#
# 2. The `is_safe` function checks whether it is safe to place a queen at a given position. It takes the current `row` and `col` coordinates and the list of `queens` representing the positions of already placed queens. It compares the current position with the positions of the previously placed queens to check for conflicts. It checks if the new queen is in the same row, same diagonal, or same anti-diagonal as any of the previous queens. If a conflict is found, the function returns `False`; otherwise, it returns `True`.
#
# 3. The `solve_nqueens_util` function is a recursive function that attempts to place queens on the board column by column. It takes the current column index `col`, the list of queen positions `queens`, and the lookup arrays `row_lookup`, `nd_lookup`, and `rd_lookup` as parameters.
#
# 4. Inside the `solve_nqueens_util` function, it first checks if all the queens have been successfully placed by comparing the current column index `col` with the board size `N`. If all queens have been placed (base case), it means a valid solution has been found, so the function returns `True`.
#
# 5. If there are still columns left to be filled, the function iterates over each row in the current column using the `range(N)` loop. For each row, it checks if it is safe to place a queen at that position by calling the `is_safe` function. If it is safe, the queen is placed at that position by updating the `queens` list with the current row index.
#
# 6. After placing the queen, the function updates the lookup arrays `row_lookup`, `nd_lookup`, and `rd_lookup` to mark the occupied rows and diagonals as unavailable (set to `False`).
#
# 7. The function then makes a recursive call to itself with the next column index (`col + 1`) to continue the placement process and explore the possibilities in the next column.
#
# 8. If the recursive call returns `True`, indicating a successful placement for the next column, the function also returns `True` to propagate the success to the previous recursive calls.
#
# 9. If the recursive call does not return `True`, it means that the current queen's position did not lead to a valid solution. In this case, the queen is removed from the current position by setting its value in the `queens` list back to `-1`. Additionally, the lookup arrays `row_lookup`, `nd_lookup`, and `rd_lookup` are restored to mark the row and diagonals as available (set to `True`).
#
# 10. The function then continues to the next row in the current column and repeats the process of placing queens and making recursive calls until a valid solution is found or all possibilities are exhausted.
#
# 11. If no valid solution is found for the initial call to `solve_nqueens_util`, the function returns `False` to indicate that a solution does not exist.
#
# 12. The `solve_nqueens` function serves as a wrapper function. It initializes the necessary data structures, such as the `queens` list to keep track of queen positions, and the lookup arrays (`row_lookup`, `nd_lookup`, and `rd_lookup`) to track available rows and diagonals.
#
# 13. The function then calls the `solve_nqueens_util` function with the initial column index 0 and the initialized data structures to start solving the N-Queens problem.
#
