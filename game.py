# Put your code here
import random

number = None
guess =  None
name = raw_input ("Howdy, What's your name? ")
print "%s, I'm thinking of a number between 1 and 100." % (name)
print "Try to guess my number."
number = random.randint(1,100)

while guess != number:
    print number
    type (number)
    guess = int(raw_input("Your guess? "))
    if guess > number:
        print "Your guess is too high, try again!"
    elif guess < number:
        print "Your number is too low, try again!"
    else: 
        print "Huzzah! you picked the it! The number is %s." % (number)        

