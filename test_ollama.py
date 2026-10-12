from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="deepseek-r1:8b",
    temperature=0
)

response = llm.invoke(
    "Сколько будет 7 умножить на 9? Ответь только числом."
)

print("Ответ модели:", response.content)