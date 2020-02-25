# question2.py
# The program spells the input number.
# Date: 02/05/2020
# Author: Tarini Dash
def main():
    print("The program spells the input number.")
    # body of the program
    num_str = input("Please input a number: ")
    print("You typed a string: " + num_str)
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 
    print_num=""
    for i in num_str:
        print_num = print_num + num_list[int(i)] + " "
        
    print("The number in words: "+print_num)
    
    
main()