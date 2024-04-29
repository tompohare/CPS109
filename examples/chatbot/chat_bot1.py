from difflib import get_close_matches

def get_best_match(user_question, knowledge):
    """Compares the user question to find similiar questions in knowledge base"""
    questions = list(knowledge.keys())
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    else:
        return None

def chatbot(knowledge):
    """Chatbot"""
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
            print('Bot: I don\'t understand... Could you try rephrasing that?')

def main():
    knowledge: dict = {'hello': 'Hey there!',
                       'how are you?': 'I am good, thanks!',
                       'do you know what the time is?': 'Not at all',
                       'what time is it?': 'No clue!',
                       'what can you do?': 'I can answer questions',
                       'ok': 'Great!'}
    chatbot(knowledge)

if __name__ == "__main__":
    main()
