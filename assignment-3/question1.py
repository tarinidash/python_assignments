# question3_1.py
# A program to calculating the wind chill index
# Date: 01/26/2020
# Author: Tarini Dash
import math
def main():
    print("The program calculates the wind chill index given a temperature and wind speed.")
    # body of the program
    temperature = eval(input("Enter the temperature in degrees Fahrenheit: "))
    wind_speed = eval(input("Enter wind speed in miles per hour: "))
    wind_chill_index = 35.74 + 0.6215 * temperature - 35.75 * math.pow(wind_speed, 0.16) +  0.4275* temperature * math.pow(wind_speed, 0.16)
    print("The wind chill index is ", round(wind_chill_index,1))
 
main()