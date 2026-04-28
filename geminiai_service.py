import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(question: str):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(question)
        return response.text

    except Exception as e:
        print("ERROR:", e)
        return "Something went wrong to repond from Gemini."   