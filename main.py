import openai

# fetch API KEY from a text file
with open('API_KEY.txt', 'r') as f:
    key = f.read()

openai.api_key = f"{key}"


messages = []

while True:
    user = input('Enter your question: ')
    if user:
        messages.append({"role": "system", "content": user})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        reply = chat.choices[0].message.content
        print(f'chatGPT: {reply}')
        print('---'*40)

