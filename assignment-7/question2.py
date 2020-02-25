# =============================================================================
# question2.py
# A program to check if the input numbers are sorted.
# Date: 02/23/2020
# Author: Tarini Dash
# =============================================================================


# =============================================================================
# Modifies the input list of strings´”strList” by converting each string to a number.
# Raises an exception in case a string in the list strList does not represent a 
# valid number, prints an error message and returns False.
# Returns True if all strings in “strList” represent numbers, and False otherwise. 
# =============================================================================
def toNumbers(strList):
    try:
        for i in range(len(strList)):
            strList[i] = int(strList[i])
    except ValueError: # the input is not an integer
        print("Error! The input is not a number!")
        return False
    return True


# =============================================================================
# The input “nums” is a list of numbers.
# Use a Boolean variable (flag) and initially assume that the numbers in the list “nums” are sorted.
# Use a definite loop to sequence through the list. If you find a pair of elements, which are in
# descending order, set the flag to “False” and exit the loop. Return the flag. 
# =============================================================================
def isAscend(nums):
    checkAscending = True
    for i in range(len(nums) -1):
        if (nums[i] > nums[i+1]):
            checkAscending = False
            break
        
    return checkAscending
            
    

# =============================================================================
# The input “nums” is a list of numbers.
# Use a Boolean variable (flag) and initially assume that the numbers in the list “nums” are sorted.
# Use a definite loop to sequence through the list. If you find a pair of elements, which are in
# ascending order, set the flag to “False” and exit the loop. Return the flag.     
# =============================================================================
def isDescend(nums):
    checkDescending = True
    for i in range(len(nums) -1):
        if (nums[i] < nums[i+1]):
            checkDescending = False
            break
    
    return checkDescending
    
    
   
    
def areSame(nums):
    checkSame = True
    for i in range(len(nums) -1):
        if (nums[i] != nums[i+1]):
            checkSame = False
            break
    
    return checkSame

   
# The main function
def main():
    print("A program to check if the input numbers are sorted.")
    input_string = input("Enter numbers separated by a space: ")
    if (input_string == ""):
        print("Error! No input number.")
    else:
        list_str = input_string.split(" ")
        if(toNumbers(list_str)):
            if(len(list_str) == 1):
                print("You entered a single number.")
            else:
                if(areSame(list_str)):
                    print("The numbers are same.")
                else:
                    if(isAscend(list_str)):
                        print("The numbers are in Ascending order.")
                    else:
                        if(isDescend(list_str)):
                            print("The numbers are in Descending order.")
                        else:
                            print("The numbers are not sorted.")
    
    
    
main()