import json
from difflib import get_close_matches as get_close_matches

def load_database():
    with open('#\\database.json','r') as file: #write your path
        return json.load(file)


def write_to_database(data):
    with open('#\\database.json','w') as file: #write your path
        json.dump(data, file, indent=2)


def find_close_match(question, questions):
    matched = get_close_matches(question, questions, n=1, cutoff=0.6)
    return matched[0] if matched else None


def find_answer(question, database):
    for question_answers in database["questions"]:
        if question_answers["question"] == question:
            return question_answers["answer"]
    return None


def chat_bot():
    database = load_database()

    while True:
        question = input("You: ")
        if question == 'exit':
            print("Successfully logged out.")
            break

        matched_result = find_close_match(question, [question_answers["question"] for question_answers in database["questions"]])

        if matched_result:
            found_answer = find_answer(matched_result, database)
            print(f"Bot: {found_answer}")
        else:
            print("Bot: I don't know how to answer that. Can you teach me?")
            new_answer = input("You can write to teach or type [skip]: ")

            if new_answer != 'skip':
                database["questions"].append({
                    "question": question,
                    "answer": new_answer
                })
                write_to_database(database)
                print("Bot: Thank you, I've learned something new thanks to you.")


if __name__ == '__main__':
    chat_bot()
