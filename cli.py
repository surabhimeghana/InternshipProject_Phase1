import requests

while True:
    option = input("Choose Option 1 for Open AI:, Option 2 for Gemini:")

    question = input("Ask something (type 'exit' or 'quit' to stop): ")


    if question.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = requests.get(
        "http://127.0.0.1:8000/ask",
        params={"q": question, "option": option}
    )

    print("Answer:", response.json()["answer"])
    
