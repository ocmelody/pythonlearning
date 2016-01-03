import random
import os

theString = "Hello! What is your name?"
print theString
os.system("say %s" %(theString))

theName = raw_input()
theString="O.K. " + theName + ", I am thinking of a number between 1 and 20."
os.system("say %s" %(theString))

#the computer generate a random number between 1 and 20
number = random.randint(1, 20)

theString = "Good Luck " + theName
os.system("say %s" %(theString))

i = 0
while i < 6:
    i = i + 1

    theString = " can you guess the number that I have?" + theName
    print theString
    os.system("say %s" %(theString))
    guess = input()
    #convert the string to an integer
    guess = int(guess)
    if guess == number:
        theString = "Great job " + theName + " ! You guessed the number in " + str(i) + " guesses!"
        print theString
        os.system("say %s" %(theString))

        theString="bye! You did great!"
        print theString
        os.system("say %s" %(theString))

        theString = "genius! " + theName
        print theString
        os.system("say %s" %(theString))
        break
    else:
        if guess < number:
            theString = "Your Guess is too small, try again."
            print theString
            os.system("say %s" %(theString))
        else:
            theString = "Your guess is too big, try again."
            print theString
            os.system("say %s" %(theString))


if i == 6 and guess != number:
    print("You need work on this game!  I think you better try again!")
    theString = theName + "You are so stupid!"
    os.system("say %s" % (theString))
