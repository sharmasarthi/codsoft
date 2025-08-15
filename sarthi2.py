# Simple Rule-Based Chatbot

print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()  # convert to lowercase for easy matching

    # Exit condition
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    # Greetings
    elif any(greet in user_input for greet in ["hi", "hello", "hey"]):
        print("Chatbot: Hello! How can I help you today?")

    # Asking name
    elif "your name" in user_input:
        print("Chatbot: I am ChatBot 1.0, your friendly assistant.")

    # Asking about well-being
    elif "how are you" in user_input:
        print("Chatbot: I'm doing great, thank you! How about you?")

    # Weather
    elif "weather" in user_input:
        print("Chatbot: I can't check the weather right now, but I hope it's nice where you are!")

    # Time query (simple static)
    elif "time" in user_input:
        print("Chatbot: I don't have a clock, but maybe it's coffee time? ☕")

    # Default response
    else:
        print("Chatbot: Sorry, I don't understand that. Can you rephrase?")
