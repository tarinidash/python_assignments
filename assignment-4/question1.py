# question1.py
# The program prints a string in a reverse order.
# Date: 02/05/2020
# Author: Tarini Dash
def main():
    print("The program prints a string in a reverse order.")
    # body of the program
    orig_str = input("Please enter a string: ")
    print("You typed a string: " + orig_str)
    print("The string in the reverse order: " + orig_str[::-1])
    
main()