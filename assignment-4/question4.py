# question4.py
# The program checks if an input string is a palindrome.
# Date: 02/05/2020
# Author: Tarini Dash
def main():
    print("The program checks if an input string is a palindrome")
    # body of the program
    input_str = input("Enter a string: ")
    if input_str == input_str[::-1]:
        print("The string is a palindrome. ")
    else:
        print("The string is not a palindrome. ")
    
main()