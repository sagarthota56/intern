quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Madrid", "C) Berlin"],
        "correct_answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus"],
        "correct_answer": "B"
    },
    {
        "question": "What is the units of speed?",
        "options" : ["A)meter", "B) second", "C) Meter per second"],
        "correct_answer": "C"
        
    },
]
def get_user_answer(options):
    while True:
        print("\n".join(options))
        user_input = input("Enter your answer (A/B/C): ").strip().upper()
        if user_input in ["A", "B", "C"]:
            return user_input
        else:
            print("Invalid input. Please choose A, B, or C.")

def calculate_score(user_answers):
    correct_count = sum(user_answers[q] == q_data["correct_answer"] for q, q_data in enumerate(quiz_data))
    return correct_count
def provide_feedback(user_answers):
    for q, q_data in enumerate(quiz_data):
        if user_answers[q] == q_data["correct_answer"]:
            print(f"Question {q + 1}: Correct!")
        else:
            print(f"Question {q + 1}: Incorrect. Correct answer: {q_data['correct_answer']}")
def main():
    user_answers = {}
    for q, q_data in enumerate(quiz_data):
        print(f"\nQuestion {q + 1}: {q_data['question']}")
        user_answers[q] = get_user_answer(q_data["options"])

    score = calculate_score(user_answers)
    print(f"\nYour final score: {score}/{len(quiz_data)}")
    provide_feedback(user_answers)

if __name__ == "__main__":
    main()