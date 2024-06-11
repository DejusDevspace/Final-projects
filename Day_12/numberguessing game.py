from random import randint

EASY_LEVEL_TURNS = 10   #This is an example of GLOBAL VARIABLE
HARD_LEVEL_TURNS = 5  

#Make function to set difficulty
def set_difficulty(level):
    # level = input("Choose a difficulty. Type 'Easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Please choose a difficulty.") #There is a bug here to fix



#function to guess the users against the computer guess
def check_answer(user_guess, answer, turns):
    """ Check answers against guess. Returns the number of turns remaining."""
    if user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print("You guessed right.")

def game():
    #choosing a random number
    print("Welcome to Number guessing game")
    print("I am thinkng of a number between 1 to 100.")
    answer = randint(1,100)
    print(answer)
    level = input("Choose a difficulty. Type 'Easy' or 'hard': ").lower()


    turns = set_difficulty()
    
        

    #repeat the guessing functionality
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attepmts remaining to guess the number.")

        #let the user guess a number
        user_guess = int(input("Make a Guess: "))
        
        #Track the number of turns and reduce by one if it is wrong
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses. You lost")
            return # to exit the game and stop the code from running
        elif user_guess != answer:
            print("Guess Again.")


game()
