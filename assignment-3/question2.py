# question3_2.py
# A program to calculating the length of a ladder
# Date: 01/26/2020
# Author: Tarini Dash
import math
def main():
    print("The program calculates the length of a ladder.")
    # body of the program
    height = eval(input("Enter the height in feet: "))
    angle = eval(input("Enter the angle in degrees: "))
    length = height/math.sin((math.pi/180)*angle)
    print("The length of the ladder is ", round(length,2) , " feet")
 
main()