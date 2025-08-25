import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env + configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def translate_to_german(text: str) -> str:
    """
    Uses Gemini to translate English text into German.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Translate the following English text into German (just give the translation, no explanation): '{text}'"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Translation error: {e}"
