# Put your code here
import random
#initializing the guess variable
guess = None
name = raw_input ("Howdy, What's your name? ")
play = True
guess_list = []

while play:
    answer = raw_input("Do you want to play a game? (yes/no): ")
    if answer == "yes":
        print "Great!"
        guess_list =[]
    else:
        print "Have it your way. Bye"
        play = False
        break
    print "%s, I'm thinking of a number between 1 and 100." % (name)
    print "Try to guess my number."
    number = random.randint(1,100)
    print number
    while guess != number:
        #This raw input is a string
        guess = raw_input("Your guess? ")
        guess_list.append(guess)
        #this is our verification that the guess is only a digit
        try:
            str.isdigit(guess)
            #this reassigns the value of guess to an Integer
            guess = int(guess)
            #this loop is setting the boundaries for acceptable guesses
            if guess < 1 or guess > 100:
                print "That number is out of range. How dare you! try again!"
                continue
            #this loop is comparing guess to number when guess isn't equal to number
            if guess > number:
                print "Your guess is too high, try again!"
            elif guess < number:
                print "Your number is too low, try again!"
            else: 
                print "Huzzah! you picked the it! The number is %s." % (number)
                print "It took you %s guesses." % (len(guess_list))
                break
        except:
            print "Whoops, input integers only! Try again."
            continue
      

