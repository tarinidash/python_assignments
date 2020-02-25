# =============================================================================
# question1.py
# The Program prints min, max, and count of positive and negative numbers
# Date: 02/23/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("Program prints min, max, and count of positive and negative numbers.")
    pos_count=0
    neg_count=0
    num_list = []
    input_string = input("Enter a number: ")
    
    while input_string != "":
        try:
            num = int(input_string)
            num_list.append(num) 
            if(num >= 0):
                pos_count += 1
            else:
                neg_count += 1
        except ValueError: # the input is not an integer
            input_string = input("Error! Please enter a valid number: ")
            continue
        input_string = input("Enter next number: ")
        
    num_list.sort()
    print()
    print("You entered",len(num_list),"numbers.")
    print("The smallest number is",num_list[0])
    print("The largest number is",num_list[-1])
    print("There are",pos_count ,"positive and ",neg_count,"negative number(s).")
    
    
       
main()
    