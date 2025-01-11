import ollama

# Initialize conversation list
convo = []

while True:
    # Get user input
    prompt = input('USER: \n')
    
    # Add user message to the conversation
    convo.append({'role': 'user', 'content': prompt})
    
    # Get assistant's response
    output = ollama.chat(model='llama3.2', messages=convo)
    response = output['message']['content']
    
    # Print the assistant's response
    print(f'ASSISTANT: \n{response} \n')
