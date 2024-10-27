questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A) Madrid", "B) Rome", "C) Paris", "D) Berlin"],
        "answer": "C"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
        "answer": "C"
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["A) O2", "B) H", "C) CO2", "D) H2O"],
        "answer": "D"
    },
    {
        "prompt": "Which year did the Titanic sink?",
        "options": ["A) 1912", "B) 1905", "C) 1898", "D) 1921"],
        "answer": "A"
    },
    {
        "prompt": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Great White Shark"],
        "answer": "B"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A) Pablo Picasso", "B) Vincent van Gogh", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "prompt": "Which country is known as the Land of the Rising Sun?",
        "options": ["A) China", "B) Japan", "C) Thailand", "D) India"],
        "answer": "B"
    },
    {
        "prompt": "What is the square root of 64?",
        "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
        "answer": "C"
    },
    {
        "prompt": "What is the longest river in the world?",
        "options": ["A) Amazon River", "B) Nile River", "C) Yangtze River", "D) Mississippi River"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0  
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").strip().upper() 
        if answer == question["answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")  

    print(f"You got {score} out of {len(questions)} questions correct.")  

run_quiz(questions)
