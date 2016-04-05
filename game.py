# Put your code here
import random
#initializing the guess variable
guess =  None
name = raw_input ("Howdy, What's your name? ")
print "%s, I'm thinking of a number between 1 and 100." % (name)
print "Try to guess my number."
number = random.randint(1,100)
while guess != number:
    #This raw input is a string
    guess = raw_input("Your guess? ")
    #this is our verification that the guess is only a digit
    if str.isdigit(guess):
        #this reassigns the value of guess to an Integer
        guess = int(guess)
        #this loop is comparing guess to number when guess isn't equal to number
        if guess > number:
            print "Your guess is too high, try again!"
        elif guess < number:
            print "Your number is too low, try again!"
        else: 
            print "Huzzah! you picked the it! The number is %s." % (number)
    else:
        print "Whoops, input integers only! Try again."
        continue       

