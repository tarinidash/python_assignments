# question3_1.py
# A program to  prints the numbers divisible by 3
# Date: 01/26/2020
# Author: Tarini Dash
def main():
    print("The program prints the numbers divisible by 3.")
    # body of the program
    num = eval(input("Enter a positive integer: "))
    for i in range(1,num+1):
        if (i % 3 == 0):
            {
                print(i)
            }
            
main()