# =============================================================================
# question1.py
# The program receives a score and uses decision structure to calculate
# and return the corresponding letter grade.
# Date: 02/15/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program receives a score and uses decision structure to calculate and return the corresponding letter grades.")
    # body of the program
    input_string = input("Enter your total score: ")
    
    # check if the input string is a float, if it is skip “except”
    try:
        num = float(input_string)
    except ValueError: # the input is not an float
        print("Error! You entered a non-integer!")
        return
    
    if (num < 0 or num > 100):
        print("Error! The total score must be between 0 and 100.")
    else:
         grade = letter_grade(num)
         print("Your letter grade is",grade)
        
    

# This function  receives a score and uses decision structure to calculate
# and return the corresponding letter grade.            
def letter_grade(score):
    if (score >= 93 and score <=100):
        return "A"
    elif (score >= 90 and score <= 92.99):
        return "A-"
    elif (score >= 86 and score <= 89.99):
        return "B+"
    elif (score >= 83 and score <= 85.99):
        return "B"
    elif (score >= 80 and score <= 82.99):
        return "B-"
    elif (score >= 76 and score <= 79.99):
        return "C+"
    elif (score >= 73 and score <= 75.99):
        return "C"
    elif (score >= 70 and score <= 72.99):
        return "C-"
    elif (score >= 66 and score <= 69.99):
        return "D+"
    elif (score >= 60 and score <= 65.99):
        return "D"      
    else:
        return "F"
        


           
main()