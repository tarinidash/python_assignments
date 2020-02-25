# question3_2.py
# A program prints the count of numbers divisible by 7.
# Date: 01/26/2020
# Author: Tarini Dash
def main():
    print("The program prints the count of numbers divisible by 7.")
    # body of the program
    num = eval(input("Enter a positive integer: "))
    count=0
    for i in range(1,num+1):
        if (i % 7 == 0):
            count = count+1
    
    if(count == 1): 
        print("There is", count , "number between 1 and",num,"that are divisible by 7.")
    else:
        print("There are", count , "numbers between 1 and",num,"that are divisible by 7.")
    
            
main()