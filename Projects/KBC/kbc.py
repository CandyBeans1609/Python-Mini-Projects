import random

# Sample questions
questions = [
    {
        "question": "What is the capital of India?",
        "choices": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "choices": ["A) Rabindranath Tagore", "B) Bankim Chandra Chatterjee", "C) Sarojini Naidu", "D) Mahatma Gandhi"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Silver"],
        "answer": "B"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["A) Gold", "B) Iron", "C) Diamond", "D) Quartz"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Gas Giant?",
        "choices": ["A) Mars", "B) Earth", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "question": "What is the largest desert in the world?",
        "choices": ["A) Sahara", "B) Arabian", "C) Gobi", "D) Antarctic"],
        "answer": "D"
    },
    {
        "question": "Which chemical element has the atomic number 1?",
        "choices": ["A) Helium", "B) Hydrogen", "C) Lithium", "D) Carbon"],
        "answer": "B"
    }
]

def ask_question(q):
    print(q["question"])
    for choice in q["choices"]:
        print(choice)
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    return user_answer == q["answer"]

def kbc_game():
    total_prize_money = 0
    shuffled_questions = random.sample(questions, len(questions))
    for i, question in enumerate(shuffled_questions):
        question_prize = 10**(i+1)
        print(f"\nQuestion {i+1} for {question_prize} rupees")
        if ask_question(question):
            total_prize_money += question_prize
            print(f"Sahi Jawab!!! Aapko prapt hue hai {question_prize} rupees.")
            print(f"Prapt Dhanrashi: {total_prize_money} rupees.")
        else:
            print("Galat Jawab! :( You've lost the game.")
            break
    print(f"Total prize money: {total_prize_money} rupees")

if __name__ == "__main__":
    kbc_game()
