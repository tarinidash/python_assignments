# question_2.py
# The program converts US mileage to EU mileage.
# Date: 01/19/2020
# Author: Tarini Dash
def main():
    print("The program converts mileage to liters per 100 km.")
    # body of the program
    us_mileage = eval(input("Please enter mileage (miles per gallon): "))
    print("Vehicle economy is", us_mileage ,"miles per gallon.")
    eu_mileage = 3.785 *100/(us_mileage *1.6)
    print("Vehicle consumption is", eu_mileage ,"liters per 100 km.")
 
main()