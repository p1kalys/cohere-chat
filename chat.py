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
    response = co.chat(model="command", messages=messages, max_tokens=150, temperature=0.1)

    assistant_reply = response.message.content[0].text
    print(f"Assistant: {assistant_reply}")

    messages.append({ "role": "assistant", "content": assistant_reply })