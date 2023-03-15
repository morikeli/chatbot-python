"""
    ©️ 2023 MORI KELI | ALLRIGHTS RESERVED.
    This is a simple chatbot integrated with OpenAI's chatGPT library.
    The program uses commend-line interface (CLI), hence 
    all questions and responses are asked and displayed at the terminal or CMD respectively.
"""

import openai


# This script strictly requires one to have a functional API KEY. 
# You can generate your API KEY at https://platform.openai.com/account/api-keys


# After generating your API KEY, create API_KEY.txt file and store your key in the file.
with open('API_KEY.txt', 'r') as f:     # fetch API KEY in the file.
    key = f.read()

openai.api_key = f"{key}"

messages = []

while True:
    """
        Create an infinite loop so that the user can askm questions as long as he/she wants.
        A user can terminate the process by pressing Ctrl + C or Ctrl + Z at the terminal/CMD.
    """
    user = input('Enter your question: ')
    if user:

        """
            You can refer to the OpenAI's documentation for further details:
            https://platform.openai.com/docs/api-reference/introduction
        """
        messages.append({"role": "system", "content": user})    # append user's question to the list
        
        # This method also works; comment line 24 and uncomment the following line to see results.
        # messages = [{"role": "system", "content": user}] 

        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        reply = chat.choices[0].message.content
        print(f'chatGPT: {reply}')
        print('---'*40)

