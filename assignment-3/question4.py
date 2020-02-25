# question4.py
# A program to calculate the sum of numbers entered by the user.
# Date: 01/26/2020
# Author: Tarini Dash
def main():
    print("The program calculates the sum of numbers entered by the user.")
    # body of the program
    count = eval(input("How many numbers do you want to sum up? "))
    num=0
    for i in range(count):
        num = num + eval(input("Enter next number: "))
            
    if(count == 1):
        print("The sum of", count ,"number is",num)
    else:
        print("The sum of", count , "numbers are",num)
            
main()
