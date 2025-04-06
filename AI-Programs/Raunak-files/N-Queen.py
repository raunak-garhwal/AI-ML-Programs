# Function to print the matrix with solution number
def printMatrix(matrix, solution_number):
    print(f"\nSolution {solution_number}:")
    for row in matrix:
        print(" ".join(row))
    
# Function to check if placing a queen at (row, col) is safe
def isSafe(matrix, row, col):
    # Check this column on the upper side
    for i in range(row):
        if matrix[i][col] == 'Q':
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if matrix[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on the right side
    i, j = row, col
    while i >= 0 and j < n:
        if matrix[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

# Function to solve the N-Queen problem using backtracking
def solveNQueen(matrix, row, solution_count):
    # If all queens are placed successfully, print the solution
    if row == n:
        solution_count[0] += 1
        printMatrix(matrix, solution_count[0])
        return True

    # Try placing the queen in each column of the current row
    res = False
    for col in range(n):
        if isSafe(matrix, row, col):
            matrix[row][col] = 'Q'  # Place queen
            # Recur to place the rest of the queens
            res = solveNQueen(matrix, row + 1, solution_count) or res
            matrix[row][col] = '*'  # Backtrack if placing the queen doesn't lead to a solution

    return res

# Driver code
print("\n<---N-Queen Problem--->")
n = int(input("\nEnter the value of n : "))

matrix = [['*' for _ in range(n)] for _ in range(n)]
solution_count = [0]  # To keep track of the number of solutions

# Check if a solution exists
if not solveNQueen(matrix, 0, solution_count):
    print("\nNo solution exists for the given value of n.")
else:
    print(f"\nTotal solutions: {solution_count[0]}")

# No of Solutions :-
#  n --> solutions
#  4 --> 2
#  5 --> 10
#  6 --> 4
#  7 --> 40
#  8 --> 92
#  9 --> 352
# 10 --> 724