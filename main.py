#The guess game

import random
randNo=random.randint(1,100)


userGuess=None
guesses=0

while (userGuess !=randNo):
    userGuess=int(input("Enter your Guess :"))

    if(userGuess==randNo):
        print("You guessed it right !")
    else:
        if (userGuess>randNo):
            print("You guessed it wrong.Enter a smaller No !")
        else:
            print("You guessed it wrong.Enter a larger No !")

    guesses+=1

print(f"You guessed the number in {guesses} guesses")

with open("topscore.txt","r") as f:
    topscore=int(f.read())

if guesses<topscore:
    print("You have just broken the top score...")
    with open("topscore.txt","w") as f:
        f.write(str(guesses))
