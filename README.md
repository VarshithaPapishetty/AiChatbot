# Level 1 — LLM-Only Smart Assistant (Prompt Engineering Focus)

This is **Level 1** of the Python Software Engineer Assignment (LLM + Agentic Thinking).  
It implements a **command-line chatbot** that interacts with a Large Language Model (LLM) and enforces **step-by-step reasoning** using prompt engineering.  

The assistant **refuses to solve math problems** and suggests using a calculator tool instead.

---

## 🚀 Features
- Takes user input from the command line.
- Uses **Gemini LLM (`gemini-1.5-flash`)** for answers.
- Always gives **step-by-step reasoning**.
- Refuses math calculations.

---

## 🛠️ Setup & Installation

1. Clone the repository or copy the project files.
2. Install dependencies:
   ```bash
   pip install google-generativeai python-dotenv
3. Create a .env file in the project folder and add your Gemini API key:
    GEMINI_API_KEY=your_api_key_here
4. Run the chatbot:
    python chatbot.py