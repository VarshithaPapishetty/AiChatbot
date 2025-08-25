## Python Software Engineer Assignment: LLM + Agentic Thinking

This repository contains solutions for **Level 1, Level 2, and Level 3** of the Python Software Engineer Assignment.  
The project builds a **command-line chatbot** that integrates with **Gemini LLM** and evolves from simple Q&A → tool usage → multi-step agentic reasoning.

---

## Level 1 — LLM-Only Smart Assistant
### Problem Statement
- Build a CLI chatbot that:
  - Takes a user question and sends it to an LLM.
  - Enforces **step-by-step reasoning** with prompt engineering.
  - **Refuses math problems** and suggests a calculator tool.

### Features
- Uses **Gemini (`gemini-1.5-flash`)** for responses.
- Clear, step-by-step outputs.
- Refuses math queries with a helpful hint.

### Run Instructions
1. Install dependencies:
   ```bash
   pip install google-generativeai python-dotenv
2. Create a .env file in the project folder and add:
    GEMINI_API_KEY=your_api_key_here
3. Run the chatbot:
    python chatbot.py
### Example Interactions
You: What are the colors in a rainbow?
Assistant:
1. Red
2. Orange
3. Yellow
4. Green
5. Blue
6. Indigo
7. Violet

You: Tell me why the sky is blue?
Assistant:
1. Sunlight contains many wavelengths.
2. The Earth's atmosphere scatters shorter wavelengths (blue).
3. Therefore, the sky looks blue.

You: What is 15 + 23?
Assistant: I cannot solve math problems directly. Please use a calculator tool.
## Level 2 — LLM + Calculator Tool
### Problem Statement
- Extend Level 1 chatbot with:
    - Calculator tool for math queries (addition, multiplication).
    - Direct LLM answers for knowledge queries.
    - Graceful handling of multi-step queries (math + knowledge).
### Features
- Math queries → handled via calculator_tool.py.
- General knowledge → handled by Gemini LLM.
- Mixed queries → gracefully refused with a message.
### Run Instructions
    python chatbot_with_tool.py
### Example Interactions
You: What is 12 times 7?
Assistant: Using calculator tool... Result = 84

You: Add 45 and 30
Assistant: Using calculator tool... Result = 75

You: What is the capital of France?
Assistant:
1. The capital of France is Paris.
2. It is the largest city in France and a major European center.

You: Multiply 9 and 8, and also tell me the capital of Japan.
Assistant: Sorry, I cannot handle multiple tasks yet.

## Level 3 — Multi-Step Agentic Smart Assistant
### Problem Statement
- Extend Level 2 chatbot into a multi-step agent:

    - Break queries into sub-queries (agentic thinking).

    - Use appropriate tools:

        - Calculator (addition, multiplication).

        - Translator (English → German).

    - Combine results into a clear, structured answer.
### Features
- Intelligent query splitting (smart_split).
- Math queries → calculator_tool.py.
- Translation queries → translator_tool.py.
- Knowledge queries → Gemini LLM.
- Handles multi-step workflows automatically.
### Run Instructions
    python full_agent.py
### Example Interactions
1.  You: Translate 'Good Morning' into German and then multiply 5 and 6.
    Assistant:
    Translation: 'Good Morning' → Guten Morgen
    Math Result: 30
2.  You: Add 10 and 20, then translate 'Have a nice day' into German.
    Assistant:
    Math Result: 30
    Translation: 'Have a nice day' → Einen schönen Tag noch
3.  You: Add 10 and 20, then translate 'Have a nice day' into German.
    Assistant:
    Math Result: 30
    Translation: 'Have a nice day' → Einen schönen Tag noch
4.  You: What is the capital of Japan and multiply 8 and 9?
    Assistant:
    General Knowledge: The capital of Japan is Tokyo.
    Math Result: 72
5.  You: Translate 'Sunshine' into German.
    Assistant:
    Translation: 'Sunshine' → Sonnenschein
