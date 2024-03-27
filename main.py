import openai

# Инициализация клиента API OpenAI с вашим API ключом
client = openai(
    api_key="введите  API ключ OpenAI",  # Замените на ваш действительный API ключ
    base_url="https://api.proxyapi.ru/openai/v1",  # Убедитесь, что этот URL работает корректно
)

# Список для хранения истории разговора
conversation_history = []

# Контекст персонажа, который будет использоваться для ответов AI
personality_context = "Вы: отвечай как лучший специалист по маркетингу."  # Измените контекст здесь

# Добавление контекста персонажа в историю разговора один раз
conversation_history.append({"role": "user", "content": personality_context})

while True:
    # Запрос ввода пользователя
    user_input = input("Вы: ")

    # Добавление ввода пользователя в историю разговора
    conversation_history.append({"role": "user", "content": user_input})

    # Отправка запроса в нейронную сеть
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=conversation_history
    )

    # Извлечение и вывод ответа нейронной сети
    ai_response_content = chat_completion.choices[0].message.content
    print("AI:", ai_response_content)

    # Добавление ответа нейронной сети в историю разговора
    conversation_history.append({"role": "system", "content": ai_response_content})

    # Опционально: условие для выхода из цикла (например, если пользователь ввел 'exit')
    if user_input.lower() == 'exit':
        break      