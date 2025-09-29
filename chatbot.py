import google.generativeai as genai
from dotenv import load_dotenv
import os

# Explicitly point to the .env file in the new directory
dotenv_path = os.path.join("E:/python/Chat Bot", ".env")
load_dotenv(dotenv_path)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set GEMINI_API_KEY in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()

SYSTEM_PROMPT = "You are a helpful, friendly AI chatbot."

def chat_with_gemini(user_input):
    """
    Send user input to Gemini and return the assistant's reply.
    """
    response = chat.send_message(user_input)
    return response.text.strip()

def main():
    print("AI Chatbot (type 'exit' to quit)\n")
    print("Chatbot:", SYSTEM_PROMPT)
    print("-" * 40)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        try:
            reply = chat_with_gemini(user_input)
        except Exception as e:
            print("Error calling Gemini API:", str(e))
            break

        print("Chatbot:", reply)
        print("-" * 40)

if __name__ == "__main__":
    main()
