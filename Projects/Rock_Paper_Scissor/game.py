import random

user_choice = input("Enter your choice: ")
user=user_choice.capitalize()
print("User went with ", user)


rps_choice = ["Rock", "Paper", "Scissor"]

comp = random.choice(rps_choice)
print("Computer went with",comp)

if user == comp:
    print("Tie!")
elif (user == "Paper" and comp == "Rock") or (user == "Rock" and comp == "Scissor") or (user == "Scissor" and comp == "Paper"):
    print("User Wins!")
elif (user == "Rock" and comp == "Paper") or (user == "Scissor" and comp == "Rock") or (user == "Paper" and comp == "Scissor"):
    print("Computer Wins!")
else:
    print("Enter a valid response!")