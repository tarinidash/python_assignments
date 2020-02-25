# question3.py
# The program computes the value of a string.
# Date: 02/05/2020
# Author: Tarini Dash
def main():
    print("The program computes the value of a string.")
    # body of the program
    input_str = input("Enter any name in lower case: ")
    input_str = input_str.lower()
    char_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0;
    for i in input_str:
        count = count + char_list.index(i)+1
    
    print("The numeric value of the name is " ,count)
    
main()