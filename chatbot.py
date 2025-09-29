
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set OPENAI_API_KEY in .env")


client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = "You are a helpful, friendly AI chatbot."

def chat_with_gpt(messages):
    """
    Send conversation to GPT and return the assistant's reply.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content.strip()

def main():
    print("AI Chatbot (type 'exit' to quit)\n")
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        
        messages.append({"role": "user", "content": user_input})

        
        try:
            reply = chat_with_gpt(messages)
        except Exception as e:
            print("Error calling OpenAI API:", str(e))
            break

     
        messages.append({"role": "assistant", "content": reply})

        print("Chatbot:", reply)
        print("-" * 40)

if __name__ == "__main__":
    main()
