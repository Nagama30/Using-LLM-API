import google.generativeai as genai
import os

# API key
genai.configure(api_key=os.environ["API_KEY"])

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Conversation history and question-answer history
conversation_summary = ""
qa_history = []  # List to store question-answer pairs

def summarize_conversation(text):
    # Summarize the conversation so far
    response = model.generate_content(f"Summarize the following conversation: {text}")
    
    # Check the structure of the response
    if response and response.candidates:
        return response.candidates[0].content.parts[0].text
    return ""

def chatbot():
    global conversation_summary, qa_history
    print("Chatbot initialized! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Append current input to the conversation history for context
        prompt = f"{conversation_summary}\nUser: {user_input}"
        
        # Generate the bot's response
        response = model.generate_content(prompt)

        # Access the bot's reply
        if response and response.candidates:
            bot_reply = response.candidates[0].content.parts[0].text
        else:
            bot_reply = "Sorry, I couldn't understand that."

        # Display the bot's response
        print("Bot:", bot_reply)

        # Store the Q&A pair in history
        qa_history.append((user_input, bot_reply))

        # Update conversation summary for context
        conversation_summary = summarize_conversation(prompt + "\nBot: " + bot_reply)

# Start the chatbot
chatbot()
