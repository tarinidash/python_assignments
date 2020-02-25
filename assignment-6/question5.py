# =============================================================================
# question5.py
# The program checks passwords.
# Date: 02/16/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program checks passwords.")
    # body of the program
    input_password = input("Please enter a password: ")
    password_check(input_password)


# Tried with accumulator other than boolean
def password_check(password):
    special = "$#@"
    if(len(password) < 4):
        print("Error: The password has less than 4 characters!")
    else:
        if(len(password) > 8):
            print("Error: Maximum length of the password should be less than 8 characters!")
        else:
            if(not password[0].isalpha()):
                print("First character has to be a letter!")
            else:
                count = 0
                for ch in password:
                    if(ch.isdigit()):
                        count = count+1
                        break;
                if(count == 0):
                    print("At least 1 number between [0-9]")
                else:
                    count_special = 0
                    for chs in password:
                        if(chs in special):
                            count_special = count_special+1
                            break;
                    if(count_special == 0):
                        print("At least 1 character from [$#@]")
                    else:
                        print("You entered a valid password.")
        
    
        
main()