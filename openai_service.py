from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI()

def ask_chatgpt(question: str):
    print("question value is:",question)
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": question}]
            )
        print("RESPONSE:", response)
        return response.choices[0].message.content

    except Exception:
        return "Something went wrong."