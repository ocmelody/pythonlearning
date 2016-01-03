import random
import os

theString = "Hello! What is your name?"
print theString
os.system("say %s" %(theString))

theName = raw_input()
theString="O.K. " + theName + ", Lets do simple addition or subtraction!"
os.system("say %s" %(theString))
theString = "Good Luck " + theName
os.system("say %s" %(theString))

for x in range(0,10):
    #the computer generate a random number between 1 and 20
    repeat = True
    while repeat:
        repeat  = False
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 10)
        operation = random.randint(1,2)
        if (operation == 2) and (number1 < number2):
            repeat = True
        else:
            repeat = False


    if operation == 1:
        number = number1 + number2
        print(str(number1) + "+" + str(number2) + "=")
        theString = str(number1) + " plus " + str(number2) + " equal "
    else:
        number = number1 - number2
        print(str(number1) + "-" + str(number2) + "=")
        theString = str(number1) + " minus " + str(number2) + " equal "

    os.system("say %s" %(theString))

    i = 0
    while i < 3:
        i = i + 1

        theString = theName + " can you answer the problem "
        print theString
        os.system("say %s" %(theString))
        guess = input()
        #convert the string to an integer
        guess = int(guess)
        if guess == number:
            theString = "Great job " + theName + " ! You did the number in " + str(i) + " tries!"
            print theString
            os.system("say %s" %(theString))

            theString = "genius! "
            print theString
            os.system("say %s" %(theString))
            break
        else:
            theString = "try again."
            print theString
            os.system("say %s" %(theString))


    if i == 6 and guess != number:
        print("You need work on this game!  I think you better try again!")
        theString = theName + "You are so stupid!"
        os.system("say %s" % (theString))

