# Guessing Game
# Jordyn
# 16/02/2024 - Computer Programming Class

# Import random package
import random 
# Imports sys package
import sys
# Variables for W/L/T
wins, loss, total = 0, 0, 0
# replayGame function
# Replay function which takes userinput and converts the string to lowercase using .lower() if input is equal to "yes" calls guessingGame function else exit script using sys.exit()
def replayGame(): 
    replay = str(input("Do you wish to play again or see your stats? (Yes/No/Stats): ")).lower() 
    if replay == "yes": 
        guessingGame() 
    elif replay == "stats":
        calculate(wins,loss,total)
        replay = str(input("Do you wish to play again? (Yes/No): ")).lower() 
        if replay == "yes":
            guessingGame()
        else:
            print("Thanks for playing!\nExting script.")
            sys.exit()
    else: 
        print("Thanks for playing!\nExting script.")
        sys.exit()

# Function for guessingGame
# Generates random number from 0-10 using random.randint(0,10) and Sets a varible for an attempt counter
# sets "wins,loss,total" variables to global
def guessingGame(): 
    numbers = random.randint(0,10)
    print("Debug:", numbers)   # Personal debug to test for the correct number remove comment tag to implement
    attempt = 0 
    global wins,loss,total

    # Runs following code while attempts does not equal 3
    # If guess is equal to the randomly generated number +1 to attempt counter display which attempt guessed it correctly then call the replayGame function
    # if Guess is Lower or Higher than the randomly generated number +1 to attempt counter display if guessed number is higher or lower than the current generated number and display current attempts out of 3
    # When attempt counter equals to 3 end the while loop and notify user that they have used all the attempts and display the generated number then call replayGame function
    while attempt != 3: 
        guess = int(input("What will your guess be? (0-10): "))
        if guess == numbers: 
            attempt +=1 
            wins +=1
            total +=1
            print("Attempt",attempt, "guessed it correctly!")
            replayGame()
        elif guess < numbers:
            attempt +=1 
            print("Your guessed number is currently lower than the answer.\n",attempt,"/3 attempt(s)]")
        elif guess > numbers:
            attempt +=1 
            print("Your guessed number is currently higher than the answer.\n",attempt,"/3 attempt(s)]")
        else: 
            print("Invalid input!\nExiting Script.")
            sys.exit() 
    loss +=1
    total +=1
    print("You have used all your attempts, the number was", numbers) 
    replayGame() 

# Function to calculate winRate along with converting from float to normal interger which can be easily read as a percentage
def calculate(wins,loss,total):
    winRate = wins / (wins+loss)
    percentageCalc = int(winRate * 100)
    print("Here are your stats:\nWins: ",wins,"\nLosses: ",loss,"\nWin Rate: ",percentageCalc,"%\nTotal Games: ",total)

# Function for play which starts the game
# Asks for userinput in "play" variable and converts the string to lowercase using .lower() and if play equals to "no" exit script otherwise else if "play" equals to "yes" welcome the user then call the guessingGame function else invalid input call the play function to prompt input to user again
def play():
    play = str(input("Do you wish to play the guessing game? (Yes/No): ")).lower() 
    if play == "no":
        sys.exit() 
    elif play == "yes":
        print("Welcome to the guessing game, You have three attempts to guess the correct number!\nThe guessing range is from 0-10") 
        guessingGame()
    else:
        print("Invalid Input, please try again.")
        play()

# Callls play function
play()
