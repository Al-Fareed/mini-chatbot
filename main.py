import csv
from nltk.chat.util import Chat, reflections

def load_patterns_from_csv(file_path):
    patterns = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            pattern = row['pattern']
            response = eval(row['response'])  
            patterns.append((pattern, response))
    return patterns

patterns = load_patterns_from_csv('dataset.csv')

chatbot = Chat(patterns, reflections)

def start_chat():
    print("Hello! I'm your chatbot assistant.What can I do for you?")
    print("Type 'bye' to exit the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chal Goodbye! Have a great day!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Assistant:", response)

if __name__ == "__main__":
    start_chat()
