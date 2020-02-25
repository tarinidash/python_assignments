# =============================================================================
# question2.py
# The program to print letter X in n lines using character.
# Date: 02/09/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program to print letter X in n lines using character.")
    # body of the program
    odd_num = int(input("Please enter a positive odd integer : "))
    seq_char= input("Please enter a character : ")
    if (odd_num > 0 and odd_num % 2 != 0):
        print_X(odd_num,seq_char)
    else:
        print("You entered a number, which is not a positive odd integer.")

# print for n*n matrix. print c and space and after every row print new line.
def print_X(n, c):
    a=0
    b=n-1
    for row in range(n):
        for col in range(n):
            if(row==a and col==b):
                print(c,end="")
                a = a+1
                b = b-1
            elif(row == col):
                print(c,end="")
            else:
                print(end = " ")
        print()

main()

