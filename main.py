from fastapi import FastAPI
from openai_service import ask_chatgpt
from geminiai_service import ask_gemini

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/ask")
def ask(q: str, option: int):
    if option == 1:
        return {"answer": ask_chatgpt(q)}
    else:
        return {"answer": ask_gemini(q)}

