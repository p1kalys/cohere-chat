from dotenv import load_dotenv
import os
import cohere

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(api_key)
messages = [{
    "role": "user",
    "content": "Hello"
}, {
    "role": "assistant",
    "content": "Hi, how can I help you today?"
}]

print("Chat with Bot (type 'exit' or 'quit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print('Exiting chat.')
        break

    messages.append({ "role": "user", "content": user_input })

    stream = co.chat_stream(model="command-a-03-2025", messages=messages)
    
    assistant_reply = ""
    print(f"Assistant: ", end="", flush=True)

    for event in stream:
        if event and event.type == "content-delta":
            token = event.delta.message.content.text
            assistant_reply += token
            print(token, end="", flush=True)
    
    print()

    messages.append({ "role": "assistant", "content": assistant_reply })