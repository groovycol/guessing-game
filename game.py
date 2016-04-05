# Put your code here
import random

number=None

name = raw_input ("Howdy, What's your name? ")
print "%s, I'm thinking of a number between 1 and 100." % (name)
print "Try to guess my number."
number = random.randint(1,100)
guess = raw_input("Your guess? ")

