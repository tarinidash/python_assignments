# =============================================================================
# question2.py
# The program receives height in inches and weight in pounds, converts height to 
# meters and weight to kilograms, then calculates and returns the BMI
# Date: 02/15/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program receives height in inches and weight in pounds," 
          "converts height to meters and weight to kilograms, then calculates "
          "and returns the BMI")
    # body of the program
    height_string = input("Enter your height in inches: ")
    weight_string = input("Enter your weight in pounds: ")
    
    # check if the input string is a float, if it is skip “except”
    try:
        height = float(height_string)
        weight = float(weight_string)
        
    except ValueError: # the input is not an float
        print("Error! You entered a non-number.")
        return
    
    if (height < 0 or weight < 0):
        print("Error! You entered a negative number!")
    else:
        bmi = body_mass_index(height,weight)
        if(bmi >= 19 and bmi <=25):
            print("Your BMI is", bmi ,", you are within the healthy range!")
        elif (bmi < 19):
            print("Your BMI is", bmi ,", you are below the healthy range!")
        else:
            print("Your BMI is", bmi ,", you are above the healthy range!")
        
    

# This function receives height in inches and weight in pounds, 
# converts height to meters and weight to kilograms, then calculates and returns the BMI.             
def body_mass_index(height, weight):
    height = height * 0.0254
    weight = weight * 0.453592
    return weight/(height**2)


           
main()