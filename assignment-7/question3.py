# =============================================================================
# question3.py
# A Program to sum the rows of an input matrix.
# Date: 02/24/2020
# Author: Tarini Dash
# =============================================================================


# =============================================================================
# Prompts the user for positive integer m and n. Builds and returns a nested list 
# mx with m elements. Each element is a sub-list, which represents a row of the matrix 
# with n elements. Prompts the user to enter integers and inserts them into the list mx. 
# Let the program crash in case of invalid input.
# =============================================================================
def inMatrix():
    rows_string = input("Enter the number of rows: ")
    columns_string = input("Enter the number of columns: ")
    try:
        rows = int(rows_string)
        columns = int(columns_string)
    except ValueError:
        print("Error! You entered a non-integer!")
        return
    
    mx = []
    for r in range(rows):
        row = []
        for c in range(columns):
            msg_string = "Enter next element of row "+ str(r) + ": "
            data = int(input(msg_string))
            row.append(data)
        mx.append(row)
        
    print()
    printMx(mx)
    print()
    sumRows(mx)
    

# =============================================================================
# Input mx is a nested list that represents m x n matrix (a matrix with m rows and n columns).
# Prints each row in a separate line, with no square brackets. You will need two nested loops, 
# one that slices the rows, and the other one that prints elements of a row in the same line. 
# Use “\t” to justify the elements of the matrix.Use syntax mx[i][j] to extract element j from row i .
# =============================================================================
def printMx(mx):
    print("Input matrix:")
    for r in range(len(mx)):
        for j in mx[r]:
            print(j, end="\t")
        print()
        

# =============================================================================
# Input mx is a nested list that represents m x n matrix (a matrix 
# with m rows and n columns).The function sums the rows of the matrix mx 
# and puts the results into a list sums with m elements. You will need two nested 
# loops, one that iterates the rows, and the other one that sums the integers in the row. 
# Append the sums to the list sums and return the list. 
# =============================================================================
def sumRows(mx):
    for row in range(len(mx)):
        sum = 0
        for j in mx[row]:
            sum = sum + j
        print("Sum of numbers in row",row,"is",sum)
    

# The main function
def main():
    print("Program to sum the rows of an input matrix.")
    inMatrix()
    

main()