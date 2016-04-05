# Put your code here
import random

print "Hi there!"
name = raw_input("What is your name?")

print "Hi %s!" %(name)

raw_guess = raw_input("Choose a number between 1 and 100: ")

valid_guesses = range(1,101)

new_list = []

for number in valid_guesses:
    new_list.append(str(number))

#issues here
# while raw_guess not in new_list:
#     raw_guess = raw_input("That's invalid. Guess again.")

# guess = raw_guess

r_number = random.randint(1,100)

print r_number

def validate_guess(raw_guess):
    while raw_guess not in new_list:
        raw_guess = raw_input("That's invalid. Guess again.")
    guess = int(raw_guess)
    return guess

final_guess = validate_guess(raw_guess)
while final_guess != r_number:
    if final_guess > r_number:
        print "Guess is too high."
    elif final_guess < r_number:
        print "Guess is too low."
    raw_guess = raw_input("Choose a number between 1 and 100: ")
    while raw_guess not in new_list:
        raw_guess = raw_input("That's invalid. Guess again.")
    final_guess = int(raw_guess)



print "Congratulations! You have guessed the number."


