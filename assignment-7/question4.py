# =============================================================================
# question4.py
# A Program to sum the rows of an input matrix.
# Date: 02/24/2020
# Author: Tarini Dash
# =============================================================================


# function to check n is prime. Return true if n is prime or else return false
def isPrime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for i in range(2, n//2):
      if n % i == 0:
         return False
   return True

    
# function to print prime #s    
def printPrime(lowerLimit, upperLimit):
    print()
    print("The sequence of prime numbers in the given interval:")
    for n in range(lowerLimit,upperLimit):
        if(isPrime(n)):
            print(n)
    
    
def main():
    print("The program prints prime numbers in a range.")
    lower_limit_str = input("Enter the lower limit of a range: ")
    upper_limit_str = input("Enter the upper limit of the range: ")
    try:
        lower_limit = int(lower_limit_str)
        upper_limit = int(upper_limit_str)
    except ValueError:
        print("Error! You entered a non-integer!")
        return
    
    if (lower_limit == 0):
        print("Invalid input: Lower limit should be a positive integer, greater than 1.")
    elif(upper_limit < lower_limit):
        print("Invalid input: Upper limit is less than lower limit.")
    else:
        printPrime(lower_limit,upper_limit)
    
    
main()
