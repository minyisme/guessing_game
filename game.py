# Put your code here
import random

print "Hi there!"
raw_input("What is your name?")

guess = int(raw_input("Choose a number between 1 and 100: "))

r_number = random.randint(1,100)

while guess != r_number:
    if guess > r_number:
        print "Guess is too high."
    elif guess < r_number:
        print "Guess is too low."
    else:
        print "Your guess is invalid."
    guess = int(raw_input ("Guess again."))

print "Congratulations! You have guessed the number."
