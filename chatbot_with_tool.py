import os
import google.generativeai as genai
from dotenv import load_dotenv
from calculator_tool import calculate

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

BASE_PROMPT = """
You are a smart assistant.
Rules:
1. Always explain step by step for general knowledge questions.
2. For math questions (addition or multiplication), DO NOT answer directly.
   Instead say: "Using calculator tool..." and let the calculator tool return the result.
3. If a query mixes math and non-math (multi-step), say:
   "Sorry, I cannot handle multiple tasks yet."
"""

def is_math_query(question: str) -> bool:
    """Check if query looks like a math problem"""
    keywords = ["add", "plus", "+", "sum", "multiply", "times", "x", "*"]
    return any(word in question.lower() for word in keywords)

def ask_llm(question: str) -> str:
    """Ask Gemini for non-math queries"""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(BASE_PROMPT + "\nUser: " + question)
    return response.text.strip()

def main():
    print("🤖 Smart Assistant (Level 2 - With Calculator Tool)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye")
            break

        try:
            if is_math_query(user_input):
                # Detect if it's a mixed query (math + knowledge)
                if any(word in user_input.lower() for word in ["capital", "city", "translate"]):
                    print("Assistant: Sorry, I cannot handle multiple tasks yet.\n")
                else:
                    result = calculate(user_input)
                    print(f"Assistant: Using calculator tool... Result = {result}\n")
            else:
                # General knowledge → ask LLM
                answer = ask_llm(user_input)
                print(f"Assistant: {answer}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
