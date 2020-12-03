# Import the shuffle function from random module
from random import shuffle

def shuffle_list(my_list):
    '''
    In this function we are going to use the shuffle function to shuffle the list randomly
    '''
    shuffle(my_list) # Shuffeling the list
    return my_list

def player_guess():
    '''
    Here we will set the player guess and store it in a variable and return it at the end
    of the function
    '''
    while True:
        # Used try and except for exception handling
        try:
            guess = int(input("To guess the ball please select a number (0, 1 or 2) :-\n"))
            if guess > 2:
                print("your number is out of bound")
            else:
                return guess
        except:
            print("Please input the given options")        

def final_result(my_list,guess):
    '''
    In this function we will take the shuffeled list and the player guess
    so that we can check and print the result
    '''
    if my_list[guess] == 'O':
        print("Congratulations!\nYou got cup with a ball")
        print(my_list)

    else:
        print("Sorry!\nYou got the wrong cup")
        print(f"The ball is in {my_list}")                

if __name__ == "__main__":

    print("Welcome to Three Cup Monte!")
    
    # Used while True to continue the cycle
    while True:
        play = input("If you want to play press 's' or to quit press 'q' :-\n")
        if play == 's':
            cup_n_ball_list = [' ','O',' ']

            shuff_result = shuffle_list(cup_n_ball_list)

            guess_result = player_guess()

            final_result(shuff_result,guess_result)

        # If pressed 'q' the game will end
        elif play == 'q':
            print("Thank you for playing")
            break

        else:
            print("Please input the given options")        


