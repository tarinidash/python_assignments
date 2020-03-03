# =============================================================================
# question5.py
# The Program that prompts the user for a player who wins a point and returns “A” if player A wins, 
# “B” if player B wins, and ”Q” if the user quits the g
# Date: 02/23/2020
# Author: Tarini Dash
# =============================================================================

# The game function
def game():
    scoreA = 0
    scoreB = 0
    listA = []
    listB = []
    result = point()
    while (result):
        if(result == "Q"):
            print("You quit the game.")
            break
        elif(result == "A"):
            scoreA = scoreA + 1
        elif(result == "B"):
            scoreB = scoreB + 1
        elif(result == "E"):
            print("Invalid input. Please enter A, B or Q (to quit).")
          
        f_scoreA,f_scoreB = display(scoreA,scoreB)
        if(len(listA) > 0 and f_scoreA == "Adv" and listA[-1] == "Adv"):
            print()
            print("Player A wins the game")
            break
        if(len(listB) > 0 and f_scoreB == "Adv" and listB[-1] == "Adv"):
            print()
            print("Player B wins the game")
            break
        listA.append(f_scoreA)
        listB.append(f_scoreB)
        result = point()
        
        
    
# the point function
def point():
    user_string = input("Who wins a point, player A or player B? ")
    if(user_string == "A" or user_string == "a"):
        return "A"
    elif(user_string == "B" or user_string == "b"):
        return "B"
    elif(user_string == "Q" or user_string == "q"):
        return "Q"
    else:
        return "E"
   
 
# The display function    
def display(scoreA,scoreB):
    f_scoreA = 0
    f_scoreB = 0
    if(scoreA == 0):
        f_scoreA = 0
    elif(scoreA == 1):
        f_scoreA = 15
    elif(scoreA == 2):
        f_scoreA = 30
    elif(scoreA == 3):
        f_scoreA = 40
    if(scoreB == 0):
        f_scoreB = 0
    elif(scoreB == 1):
        f_scoreB = 15
    elif(scoreB == 2):
        f_scoreB = 30
    elif(scoreB == 3):
        f_scoreB = 40
    
    
    if(scoreA < 4 and scoreB < 4):
        print("Score of Player A:",f_scoreA)
        print("Score of Player B:",f_scoreB)
    else:
        if(scoreA > scoreB):
            f_scoreA = "Adv"
            f_scoreB = ""
        elif(scoreA < scoreB):
            f_scoreA = ""
            f_scoreB = "Adv"
        else:
            f_scoreA = "40"
            f_scoreB = "40"
        
        print("Score of Player A:",f_scoreA)
        print("Score of Player B:",f_scoreB)
        

    return f_scoreA, f_scoreB
    
    
# The main function    
def main():
    print("The program keeps a score and prints winner in a tennis game.")
    game()
    
    
    
main()
    