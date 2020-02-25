# =============================================================================
#  question3.py
#  The Program to calculate the number of combinations of n objects, taken r objects at a time.
#  Date: 02/09/2020
#  Author: Tarini Dash
# =============================================================================
def main():
    print("The Program to calculate the number of combinations of n objects, taken r objects at a time.")
    # body of the program
    n_num = int(input("Please enter a positive integer : "))
    r_num = int(input("Please enter a positive integer : "))
    if (n_num > 0 and r_num > 0):
        if(n_num < r_num):
            print("Error! Number n is less than r!")
        else:
            print(factorial(n_num)/(factorial(r_num) * factorial(n_num - r_num)))
    else:
        print("You entered a number, which is not a positive integer.")
        
    
        
def factorial(n):
    sum = 1;
    for i in range(1,n+1):
        sum = sum * i   
    return sum
        
        

main()