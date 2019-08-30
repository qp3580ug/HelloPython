import random
random_number = random.randint(1, 16)

incorrect = True

while incorrect == True:

    gUess = int(input("Guess a number between 1 and 15: "))

    if gUess == random_number:

        print("You have guessed the number correctly")
        incorrect = False 

    else:

        if gUess > random_number:
            print("Lower")
        elif gUess < random_number:
            print("Higher")