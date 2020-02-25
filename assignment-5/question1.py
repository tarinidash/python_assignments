# =============================================================================
# question1.py
# The program calculates the sum of first n numbers and sum of their cubes.
# Date: 02/09/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program calculates the sum of first n numbers and sum of their cubes.")
    # body of the program
    input_num= int(input("Please enter a positive integer: "))
    if (input_num < 1):
        print("You entered a number, which is not a positive integer.")
    else:
        sum_n(input_num)
        sum_cubes(input_num)
    


def sum_n(n):
    sum_total = 0
    for i in range(1,n+1):
        sum_total = sum_total + i
    print("The sum of first",n," positive integers is",sum_total)
    
    

def sum_cubes(n):
    sum_cube_total=0
    for i in range(1,n+1):
        sum_cube_total = sum_cube_total + i*i*i
    print("The sum of cubes of first",n,"positive integers is",sum_cube_total)
    


main()