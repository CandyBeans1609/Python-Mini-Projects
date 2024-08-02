import random

name = input("Hi, welcome to the word guessing game!\nEnter your name to begin: ")
print("All the best, ", name)

words = ['apple', 'blush', 'ring', 'python', 'coding', 'cute', 'valorant']
word = random.choice(words)

print("Guess the characters: ")

guesses = ""
turns = 15

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()  # Print new line after the word representation
    
    if failed == 0:
        print("Congratulations, you win!")
        print("The word is: ", word)
        break  # Exit the game loop if the player wins
    
    guess = input("Guess a character: ").lower()  # Convert input to lowercase
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print("Wrong guess.")
        print("You have", turns, "more guesses left.")
        
        if turns == 0:
            print("Sorry, you lose. Better luck next time.")
