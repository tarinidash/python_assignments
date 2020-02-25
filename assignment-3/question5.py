# question5.py
# A program calculates and prints the ratio of the sum of even numbers to the sum of all the numbers in the range
# Date: 01/26/2020
# Author: Tarini Dash
def main():
    print("The program calculates the sum of numbers entered by the user.")
    # body of the program
    start = eval(input("Enter start number of a range: "))
    end = eval(input("Enter ending number of a range: "))
    sum_even=0
    sum_all=0
    for i in range(start,end+1):
        sum_all = sum_all+i
        if(i % 2 == 0):
            sum_even = sum_even+i
            
    print("Ratio of sum of even numbers to sum of all numbers in the range is",round((sum_even/sum_all),3))
            
main()