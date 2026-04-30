from ollama import chat
from ollama import ChatResponse

def prompt_ollama(prompt, post_data):
    response: ChatResponse = chat(model='gemma3', messages=[
      {
        'role': 'user',
        'content': f"{prompt} \n\n {post_data}",
      },
    ])

    return response['message']['content']
