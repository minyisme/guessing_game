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
while raw_guess not in new_list:
if raw_guess in new_list:
    guess = int(raw_guess)
else:
    raw_guess = raw_input("That's invalid. Guess again.")

r_number = random.randint(1,100)

print r_number

while guess != r_number:
    if guess > r_number:
        print "Guess is too high."
    elif guess < r_number:
        print "Guess is too low."
    raw_guess = raw_input("Choose a number between 1 and 100: ")
    while raw_guess not in new_list:
        raw_guess = raw_input("That's invalid. Guess again.")
    guess = int(raw_guess)



print "Congratulations! You have guessed the number."
