# =============================================================================
# question4.py
# The program prompts the user for a player who wins a point and returns “A” if 
# player A wins a point and returns “B” if player B wins a point
# Date: 02/16/2020
# Author: Tarini Dash
# =============================================================================
def main():
    print("The program keeps score in a game.")
    # body of the program
    winner = game()
    print("The Winner is ",winner)


# =============================================================================
# Initializes the scores of both players to 0.
# Calls point() to determine the player who wins a point.
# Increments the score of the player who wins a point.
# Prints the scores of both players.
# Game is over and the winner is:
# • A player who has at least 3 points and wins by at least 2 points or
# • A player who first scores 7 points.
# Returns ”A” if player A wins the game or ”B” if player B wins the game.    
# =============================================================================
def game():
    score_a = 0
    score_b = 0
    for i in range(10):
        score_recieved = point()
        if(score_recieved == "A"):
            score_a = score_a +1
        elif(score_recieved == "B"):
            score_b = score_b +1
        print("A score: ",score_a)    
        print("B score: ",score_b)
        if(score_a > 2 and (score_a - score_b > 1)):
            return "A"
        elif(score_b > 2 and (score_b - score_a > 1)):
            return "B"
    
    
# =============================================================================
# Prompts the user for the player who wins a point. User enters “A” or “a” for 
# player A, and “B” or “b” for player B.
# Checks input and prints a message in case of invalid input and returns string “E.”
# Returns “A” if player A wins a point or ”B” if player B wins a point
# =============================================================================
def point():
    user_input = input("Who wins a point, player A or B?: ")
    if(user_input != "A" and user_input != "a" and user_input != "B" and user_input != "b"):
        print("E")
    else:
        if(user_input == "A" or user_input == "a"):
            return "A"
        elif(user_input == "B" or user_input == "b"):
            return "B"
        
        
main()