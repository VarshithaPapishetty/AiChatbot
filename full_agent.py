import os
import google.generativeai as genai
from dotenv import load_dotenv
from calculator_tool import calculate
from translator_tool import translate_to_german
import re

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

BASE_PROMPT = """
You are a smart agent assistant.
Rules:
1. Break multi-step queries into clear steps.
2. Use tools when required:
   - Calculator tool for addition/multiplication.
   - Translator tool for English → German.
3. If no tool is needed, use LLM reasoning.
4. Always present the output step-by-step.
"""

def ask_llm(question: str) -> str:
    """Ask Gemini for general knowledge queries."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(BASE_PROMPT + "\nUser: " + question)
    return response.text.strip()

def smart_split(query: str):
    """
    Split query into sub-queries intelligently.
    Keeps math phrases like 'multiply 5 and 6' or 'add 10 and 20' together.
    Cleans punctuation (like commas) so they don't become sub-queries.
    """
    query = query.lower().strip()
    query = query.replace("then", "and")

    parts = []

    # 1. Capture math patterns
    math_patterns = re.findall(r"(add\s+\d+\s+and\s+\d+|multiply\s+\d+\s+and\s+\d+)", query)
    for m in math_patterns:
        parts.append(m.strip())

    # 2. Remove matched math patterns from query completely
    cleaned_query = query
    for m in math_patterns:
        cleaned_query = cleaned_query.replace(m, "")

    # 3. Split remaining by 'and'
    leftovers = [seg.strip(" .,") for seg in cleaned_query.split("and") if seg.strip()]

    for seg in leftovers:
        if seg:  # skip empty
            parts.append(seg)

    # 4. Deduplicate + clean
    parts = [p.strip(" .,") for p in parts if p and p not in [",", "."]]
    parts = list(dict.fromkeys(parts))  # remove duplicates, preserve order

    print(f"🔍 Sub-queries detected: {parts}")
    return parts

def process_query(user_input: str) -> str:
    results = []
    sub_queries = smart_split(user_input)

    for sub_query in sub_queries:
        # Translation
        if "translate" in sub_query:
            try:
                if "'" in sub_query:
                    text_to_translate = sub_query.split("'")[1]
                    translated = translate_to_german(text_to_translate)
                    results.append(f"Translation: '{text_to_translate}' → {translated}")
                else:
                    results.append("Translation failed (missing quotes).")
            except Exception as e:
                results.append(f"Translation failed: {e}")

        # Math
        elif any(word in sub_query for word in ["add", "plus", "+", "sum", "multiply", "times", "x", "*"]):
            result = calculate(sub_query)
            results.append(f"Math Result: {result}")

        # Knowledge
        elif "capital" in sub_query or "distance" in sub_query:
            answer = ask_llm(sub_query)
            results.append(f"General Knowledge: {answer}")

        # Default → LLM
        else:
            answer = ask_llm(sub_query)
            results.append(f"General Knowledge: {answer}")

    return "\n".join(results)

def main():
    print("Smart Agent (Level 3 - Multi-Step)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye")
            break

        try:
            response = process_query(user_input)
            print(f"Assistant:\n{response}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
