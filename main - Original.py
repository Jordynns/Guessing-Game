#Guessing Game
import random # import random package
import sys # imports sys package
import time # import time package

play = str(input("Do you wish to play the guessing game? (Yes/No): ")) # User dictates if game is started or not
if play == "No":
    sys.exit() # If no exit script
elif play == "Yes":
    print("Welcome to the guessing game, You have three attempts to guess the correct number!\nThe guessing range is from 0-10")

# Uses user input to determin wether to start the game or not

def guessingGame(): # Guessing Game function

    numbers = random.randint(0,10)
    guess = int(input("What will your first guess be? (0-10): ")) # User guess input
    count = 2

# ^ variables for the random number generation, guess and attempt count

    #print("Debug:", numbers)   #/// Personal debug to test for the correct number remove comment tag to implement

    if guess == numbers:
        print("Your 1st attempt guessed it correctly!") # Correct Guess
        time.sleep(1)
        replay = str(input("Do you wish to play again? (Yes/No): ")) # User input for replay
        if replay == "Yes":
            guessingGame()
        elif replay == "No":
            print("Exting script.")
            sys.exit()  # If user wants to no longer play anymore exit the script
        return
    elif guess < numbers:
        print("Your guessed number is currently lower than the answer, Guess again.\n",count, "attempt(s) remaining") # Guessed number lower than the answer
    elif guess > numbers:
        print("Your guessed number is higher than the answer.\n", count, "attempt(s) remaining.") # Guessed number higher than the answer
    else:
        print("Number out of range!")
        return

    guess = int(input("What will your second guess be? (0-10): ")) # User guess input
    count = 1

    if guess == numbers:
        print("Your 2nd attempt guessed it correctly!") # Correct Guess
        time.sleep(1)
        replay = str(input("Do you wish to play again? (Yes/No): ")) # User input for replay
        if replay == "Yes":
            guessingGame()
        elif replay == "No":
            print("Exting script.")
            sys.exit()  # If user wants to no longer play anymore exit the script
        return
    elif guess < numbers:
        print("Your guessed number is currently lower than the answer, Guess again.\n",count, "attempt(s) remaining") # Guessed number lower than the answer
    elif guess > numbers:
        print("Your guessed number is higher than the answer.\n", count, "attempt(s) remaining.") # Guessed number higher than the answer
    else:
        print("Number out of range!")
        return

    guess = int(input("What will your third and final guess be? (0-10): ")) # User guess input
    count = 0

    if guess == numbers:
        print("Your final attempt guessed it correctly!") # Correct Guess
        time.sleep(1)
        replay = str(input("Do you wish to play again? (Yes/No): "))
        if replay == "Yes":
            guessingGame()
        elif replay == "No":
            print("Exting script.")
            sys.exit() # If user wants to no longer play anymore exit the script
        else:
            return
    elif guess < numbers:
        print("Your guessed number was lower than the answer, You have ran out of attempts.\nThe answer was: ",numbers) # Guessed number lower than the answer - Gives answer
    elif guess > numbers:
        print("Your guessed number was higher than the answer, You have ran out of attempts.\nThe answer was: ",numbers) # Guessed number higher than the answer - Gives answer
    else:
        print("Number out of range!")
        return

    if count == 0: # If the count equals 0 ask if you wish to play again
        print("Ran out of attempts!")
        time.sleep(1)
        replay = str(input("Do you wish to play again? (Yes/No): "))
        if replay == "Yes":
            guessingGame() 
        elif replay == "No":
            print("Exting script.")
            sys.exit() # If user wants to no longer play anymore exit the script
        else:
            return

guessingGame() # Calls game function
