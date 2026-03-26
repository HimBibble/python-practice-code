
#CONVERT STRING TO UPPERCASE
#textToConvert = "lowercase text"

#outputString = textToConvert.upper()

#print("outputString")


#ADD TWO NUMBERS

#num1 = int(input("Please enter the first number to add."))



#num2 = int(input("Please enter the first number to add."))


#total = num1 + num2

#print(total)

#GET NUMBERS FROM USER AND ADD
'''
keepAdding = "y"
total = 0
#Loop until user doesn't need to add more
while keepAdding == "y":
    numToAdd = int(input("Please enter the number you'd like to add."))
    #increment total
    total = total + numToAdd
    keepAdding = input("Would you like to add another number? y/n")
    if keepAdding == "n":
        break
 
print(total)
'''

#ASK USER FOR MAXIMUM NUMBER AND GENERATE RANDOM BETWEEN 0 AND INPUT
'''
import random
quitGame = "y"
#Loop for game
while quitGame != "n":
    #declare variables
    maxRange = int(input("Please enter the maximum value to guess."))

    numberToGuess = random.randint(0, maxRange)
    #get user input
    userGuess = int(input("Please enter your guess."))
    #evaluate user input
    if userGuess == numberToGuess:
        print("Good job you got it!")
        quitGame = input("Would you like to play again? y/n")
    else:
        quitGame = input("Not quite, would you like to play again? y/n")
    if quitGame == "n":
        continue
'''

#PRINT 10 TIMES LEFT AND RIGHT THING

amountLeft = 0
amountRight = 0

#Go through 10 numbers 
for i in range (10):
    #evaluate if number is even
    numToEvaluate = random.randint(0, 100)
    #add one to right value
    if numToEvaluate % 2 == 0
        print ("right")
        amountRight += 1
    #add one to left value
    else:
        print("left")
        amountLeft += 1
        
print("Right", amountRight, "Left", amountLeft)
