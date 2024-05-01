"""
A chatbot to interact with the user, provides answers to questions, and
learns answers to new questions.

The chatbot does the following:
1. Load the knowledge base from a JSON file.
2. Continuously prompt the user for questions.
3. Find the closest matching question in the knowledge base.
4. If a match is found, return the answer. Otherwise, ask the user to teach the chatbot the answer.
5. If the user provides a new answer, add it to the knowledge base and save the updated knowledge base to the JSON file.
6. Exit the chatbot when the user types 'quit'.
"""
import json
from difflib import get_close_matches

def load_knowledge_base(kb_path):
    """Load the knowledge base from a JSON file and return as a Python dictionary"""
    with open(kb_path, 'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(kb_path, knowledge):
    """Save the knowledge base dictionary to a JSON file"""
    with open(kb_path, 'w') as file:
        json.dump(knowledge, file, indent=2)
    return

def get_best_match(user_question, knowledge):
    """Compares the user question to find similar questions in knowledge base.
        returns the first match from matches list if found, otherwise returns None
    """
    questions = list(knowledge.keys())
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    else:
        return None

def chatbot():
    """Chatbot"""
    knowledge = load_knowledge_base('knowledge_base.json')

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            break
        # Find the best match, otherwise returns nothing
        best_match = get_best_match(user_input, knowledge)
        answer = knowledge.get(best_match)
        if answer:
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t understand. Could you teach me?')
            new_answer = input('Type the answer or "skip" to skip: ')
            if new_answer.lower() != 'skip':
                knowledge[user_input] = new_answer
                save_knowledge_base('knowledge_base.json', knowledge)
                print('Thank you! I\'ve learned something new.')

if __name__ == "__main__":
    chatbot()
