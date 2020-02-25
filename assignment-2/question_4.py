# question_4.py
# A program for an Interactive Calculator
# Date: 01/19/2020
# Author: Tarini Dash
def main():
    print("Welcome to the Interactive Python Calculator")
    # body of the program
    for i in range(0,100):
        output = eval(input("Enter an expression: "))
        print(output)
 
main()