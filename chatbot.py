import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Base system prompt for step-by-step reasoning
BASE_PROMPT = """
You are a smart assistant.
Rules:
1. Always think step by step before answering.
2. Format answers with numbers or bullet points for clarity.
3. If the user asks a math calculation (like addition, multiplication, subtraction, division),
   DO NOT answer. Instead say: "I cannot solve math problems directly. Please use a calculator tool."
"""

def ask_llm(question: str) -> str:
    """Send a question to the Gemini LLM with enforced step-by-step reasoning."""
    model = genai.GenerativeModel("gemini-1.5-flash")  # updated correct model
    response = model.generate_content(BASE_PROMPT + "\nUser: " + question)

    # Ensure response is text
    if hasattr(response, "text"):
        return response.text.strip()
    else:
        return "No valid response received from Gemini."

def main():
    print("Smart Assistant (Level 1 - Gemini)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye")
            break

        try:
            answer = ask_llm(user_input)
            print(f"Assistant: {answer}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
