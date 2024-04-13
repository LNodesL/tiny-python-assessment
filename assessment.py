import csv
import ctypes
import datetime

def load_questions_from_csv(csv_filename):
    """
    Load questions and answer options from a CSV file.
    Assumes the CSV file has columns: 'Question', 'Answer1', 'Answer2', 'Answer3', 'Answer4'.
    Returns a list of dictionaries, each containing question and answer options.
    """
    questions = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions.append(row)
    return questions

def present_question(question, answers):
    """
    Present a question and answer options to the user.
    Returns the user's selected answer (1, 2, 3, or 4).
    """
    print(question)
    for i, answer in enumerate(answers, start=1):
        print(f"{i}. {answer}")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    csv_filename = 'questions.csv'  # Replace with your actual CSV filename
    questions = load_questions_from_csv(csv_filename)

    user_responses = []
    for q in questions:
        answer_choice = present_question(q['Question'], [q['Answer1'], q['Answer2'], q['Answer3'], q['Answer4']])
        user_responses.append({'Question': q['Question'], 'Answer': q[f'Answer{answer_choice}']})

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"user_responses_{timestamp}.csv"

    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ['Question', 'Answer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for response in user_responses:
            writer.writerow(response)

    print(f"User responses saved to {output_filename}")

if __name__ == "__main__":
    main()
