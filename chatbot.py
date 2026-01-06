import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,
    api_key=os.getenv('GROQ_API_KEY')
)

def chat_with_groq():
    print("Welcome to the Groq Chatbot! Type 'exit' to quit.")
    messages = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Add user message to conversation
        messages.append({"role": "user", "content": user_input})

        # Get response from Groq
        try:
            response = llm.invoke(messages)
            bot_response = response.content
            print(f"Bot: {bot_response}")

            # Add bot response to conversation
            messages.append({"role": "assistant", "content": bot_response})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_groq()