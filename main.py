from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import multiply


# 1. Подключаем локальную модель
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

# 2. Создаём агента с инструментом
agent = create_agent(
    model=llm,
    tools=[multiply],
    system_prompt=(
        "Ты математический помощник. "
        "Для умножения чисел обязательно используй "
        "инструмент multiply. "
        "Отвечай кратко на русском языке."
    )
)

# 3. Отправляем запрос агенту
result = agent.invoke({
    "messages": [
        {"role": "user", "content": "Сколько будет 7 умножить на 9?"}
    ]
})

# 4. Показываем действия агента
for message in result["messages"]:
    print(f"\nТип сообщения: {message.type}")

    if message.type == "ai" and message.tool_calls:
        print("Вызовы инструментов:", message.tool_calls)

    elif message.type == "tool":
        print("Результат инструмента:", message.content)

    elif message.type == "ai":
        print("Ответ агента:", message.content)