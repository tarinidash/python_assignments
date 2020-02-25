# question_3.py
# The program converts Celsius temperature into Fahrenheit
# Date: 01/19/2020
# Author: Tarini Dash
def main():
    print("Conversion table from Celsius to Fahrenheit")
    # body of the program
    print("Celsius Fahrenheit")
    print("-------------------")
    for i in range(0,110,10):
        print(i,"\t",i*9/5+32)
 
main()