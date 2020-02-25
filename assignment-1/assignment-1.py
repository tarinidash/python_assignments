# -*- coding: utf-8 -*-
"""
file : assignmnet-1.py
comments: Very first assignment delivery
author: Tarini Dash(UID # - 2000701485)
date: 2020/01/13
"""

"""
function name: hello
comments: 
"""
def hello():
    print("Hello!")
    print("This is fun!")
    
hello();

"""
assignment_number: 2.1
function_name: calculateAreaOfCircle
comments: calculate the area of a circle
"""
def calculateAreaOfCircle(radius):
    print ("assignment 2.1 - circleArea(",radius,")")
    print (3.14*radius*radius)
    

calculateAreaOfCircle(2);


"""
assignment_number: 2.2
function_name: kilometersToMiles
comments: convert km to miles
"""
def kilometersToMiles(distance):
    print ("assignment 2.2 - kilometersToMiles(",distance,")")
    print (distance*0.62)
    
    
kilometersToMiles(600);


"""
assignment_number: 2.3
function_name: squareArea
comments: calculate area of a square
"""
def squareArea(side):
    print ("assignment 2.3 - squareArea(",side,")")
    print (side*side)
    
    
squareArea(12);


"""
assignment_number: 3.1
function_name: firstFiveSquares()
comments: prints the squares of the first five positive integers
"""
def firstFiveSquares():
    print ("assignment 3.1 - firstFiveSquares()")
    for i in range(1,6):
        print(i*i)
    
    
firstFiveSquares();


"""
assignment_number: 3.2
function_name: firstTenReverse
comments: print first 10 positive even integers in reverse order
"""
def firstTenReverse():
    print ("assignment 3.2 - firstTenReverse()")
    for i in range(9,-1,-1):
        print((i+1)*2)
    
  
firstTenReverse();
