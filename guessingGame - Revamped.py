# Guessing Game
# Jordyn
# 16/02/2024 - Computer Programming Class
import random # import random package
import sys # imports sys package

def replayGame(): # replayGame function
    replay = str(input("Do you wish to play again? (Yes/No): ")).lower() # User input for replay (Converts string to lowercase)
    if replay == "yes": # User input is yes then restart the game
        guessingGame() # Calls guessingGame function
    elif replay == "no": # User input no and wants to no longer play anymore, exit the script
        print("Thanks for playing!\nExting script.") # Print to log exiting script
        sys.exit() # Exit/Kill script
    
def guessingGame(): # Function for guessingGame
    numbers = random.randint(0,10) # Generates random number for user to guess
    print("Debug:", numbers)   # Personal debug to test for the correct number remove comment tag to implement
    attempt = 0 # Attempt counter variable

    while attempt != 3: # Runs following code while attempts does not equal 3
        guess = int(input("What will your guess be? (0-10): ")) # User input guess
        if guess == numbers: # If User inputed guess matches randomly generated number print and ask if they wish to replay
            attempt += 1 # Adds + 1 to the attempt count variable 
            print("Attempt",attempt, "guessed it correctly!") # Print correct guess to log
            replayGame() # Calls replayGame function
        elif guess < numbers: # If user input is lower than the random generated number 
            attempt += 1 # Adds + 1 to the attempt count variable
            print("Your guessed number is currently lower than the answer.\n",attempt,"/3 attempt(s)]")# Print guessed number lower than the answer
        elif guess > numbers: # If user input is higher than the random generated number
            attempt += 1 # Adds + 1 to the attempt count variable
            print("Your guessed number is currently higher than the answer.\n",attempt,"/3 attempt(s)]") # Print guessed number higher than the answer
        else: # If invalid number exit script
            print("Invalid input!\nExiting Script.")
            sys.exit() # Print invalid number and exiting script
    if attempt == 3: # If attempt equals  3 run following code
        print("You have used all your attempts, the number was", numbers,) # Print attempts all used and print the correct number
        replayGame() # Calls replayGame function

play = str(input("Do you wish to play the guessing game? (Yes/No): ")).lower() # User input for replay (Converts string to lowercase)
if play == "no": # User input no and wants to no longer play anymore, exit the script
    sys.exit() # Exit/Kill the script
elif play == "yes": # User input is yes sleep for 1000ms then restart the game
    print("Welcome to the guessing game, You have three attempts to guess the correct number!\nThe guessing range is from 0-10") # Print welcome to the game log
    guessingGame() # Calls guessingGame function
