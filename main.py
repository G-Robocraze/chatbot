import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hello|hi|hey",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"how are you|how's it going",
        ["I'm just a bot, but I'm doing fine. How can I help you?", "I'm good, thank you. How can I assist you?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Take care!", "See you later!"]
    ],
    # Add more pattern-response pairs here
]

def simple_chatbot():
    print("Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    chatbot = Chat(pairs, reflections)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    simple_chatbot()