# Put your code here
import random

def number_game():
    print "Hi there!"
    name = raw_input("What is your name?")

    print "Hi %s!" % (name)

    raw_guess = raw_input("Choose a number between 1 and 100: ")

    # creates list of valid guesses
    valid_guesses = range(1,101)
    new_list = []

    for number in valid_guesses:
        new_list.append(str(number))

    r_number = random.randint(1,100)

    print r_number

    # function validates if guess is a valid number between 1 and 100
    def validate_guess(raw_guess):
        while raw_guess not in new_list:
            raw_guess = raw_input("That's invalid. Guess again.")
        guess = int(raw_guess)
        return guess


    # checks if guess is the random number
    final_guess = validate_guess(raw_guess)
    total_guess = 1
    while final_guess != r_number:    
        if final_guess > r_number:
            print "Guess is too high."
        elif final_guess < r_number:
            print "Guess is too low."
        raw_guess = raw_input("Choose a number between 1 and 100: ")
        while raw_guess not in new_list:
            raw_guess = raw_input("That's invalid. Guess again.")
        final_guess = int(raw_guess)
        total_guess += 1

    print "Congratulations! You have guessed the number. It took you %i guesses." % (total_guess)

number_game()
play_again = int(raw_input("Would you like to play again? Press 1 for yes and 2 for no"))
while play_again == 1:
    number_game()
    play_again = int(raw_input("Would you like to play again? Press 1 for yes and 2 for no"))

print "Goodbye!"