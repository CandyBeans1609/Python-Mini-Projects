import random

name=input("Hieee Welcome to word guessing game!! \nEnter your name to begin: ")
print("All the best ",name)
words=['apple','blush','ring','python','coding','cute','valorant']
word=random.choice(words)

print("Guess the characters: ")

guesses=""
turns=15
while turns>0:
    failed=0
    for char in word:
        if char in guesses:    
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You win")
        print("The word is: ",word)
    
    print()
    guess=input("Guess a character: ")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("Wrog")
        print("You have", +turns, "more guesses")

        if turns==0:
            print("You Loose :( Better Luck next time")
