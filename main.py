import openai

messages = []

while True:
    user = input('Enter your question: ')
    if user:
        messages.append({"role": "system", "content": user})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, api_key="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")

        reply = chat.choices[0].message.content
        print(f'chatGPT: {reply}')

