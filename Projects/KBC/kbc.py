import random

q1 = ["How many days does February have?", "What does not grow on tree according to a popular Hindi saying?", "Which city is known as Pink City in India?"]

while True:
    question = random.choice(q1)
    correct_ans = None

    if question == q1[0]:
        print(f"{question}\n1. 30 days \n2. 28 days \n3. 31 days \n4. 27 days")
        correct_ans = 2
    elif question == q1[1]:
        print(f"{question}\n1. Money \n2. Flowers \n3. Leaves \n4. Fruits")
        correct_ans = 1
    elif question == q1[2]:
        print(f"{question}\n1. Pune \n2. Bangalore \n3. Jaipur \n4. Kochi")
        correct_ans = 3

    choice = int(input("Select your choice: "))

    if choice == correct_ans:
        print("Sahi jawab!!!!")
        break
    else:
        print("Galat jawab :( Try again.")
