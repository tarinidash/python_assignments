# =============================================================================
# question3.py
# The program determines a valid date in a leap year.
# Date: 02/15/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program determines a valid date in a leap year.")
    # body of the program
    calendar_list = in_date()
    
    try:
        year = int(calendar_list[-1])
        
    except ValueError: # the input is not an float
        print("Error! You entered a non-number.")
        return
    
    if (year < 1 or year > 2019):
        print("Error!",year,"is not a positive integer between 1 and 2019.")
    else:
        if (not is_leap_year(year)):
            print("Error!",year,"is not a leap Year")
        else:
            month = calendar_list[0]
            if (not is_month(month)):
                print("Error!",month,"month is invalid")
            else:
                day = calendar_list[1]
                if (not is_day(month,day)):
                    print("Error! You entered an invalid day in",month)
                else:
                    print("You entered a valid date in a leap year!")
                
            
# =============================================================================
# Prompts the user for month, day, and year, creates and returns a list [month, day, year].
# month is a string, but day and year are integers. For example: [“September”, 27, 2019].    
# =============================================================================

def in_date():
    calendar_list = []
    input_month = input("Please enter a month: ")
    input_day = input("Enter a day: ")
    input_year = input("Enter a year: ")
    # append to above list
    calendar_list.append(input_month)
    calendar_list.append(input_day)
    calendar_list.append(input_year)
    return calendar_list
    


# =============================================================================
# Input month is a string.
# Returns True if month is a valid month name, and False otherwise
# =============================================================================
def is_month(month):
    month_lst = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']
    if month.lower() in month_lst:
        return True
    else:
        return False
    

# =============================================================================
#     
# Input month is a string that represents a month, day is an integer that represents 
# a day in the month.
# Returns True if the day is a valid day, and False otherwise. day is valid if it
# is in the range of the days in the month.     
# =============================================================================
def is_day(month, day):
    month = month.lower()
    day = int(day)
    if(month == "january" or month == "march" or month == "may" or month == "july" 
       or month == "august" or month == "october" or month == "december"):
        if(day < 1 or day > 31):
            return False
        else:
            return True
    elif(month == "april" or month == "june" or month == "september" or month == "november"):
        if(day < 0 or day > 30):
            print(month)
            print(day)
            return False
        else:
            return True
    else:
        if(day < 0 or day > 29):
            return False
        else:
            return True
        

# =============================================================================
# Input year is a positive integer.
# Returns True if the year is a leap year, and False otherwise    
# =============================================================================

def is_leap_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
   
    
    
main()