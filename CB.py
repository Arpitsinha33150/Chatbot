import openai


openai.api_key = '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'

def chat_with_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=prompt,
        max_tokens=150, 
        n=1,  
        stop=None,  
    )

    
    generated_response = response['choices'][0]['text'].strip()
    print("Bot:", generated_response)


def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day.")
            break
        
        
        chat_history = f"You: {user_input}\nBot:"

        
        chat_with_openai(chat_history)


if __name__ == "__main__":
    chat_with_bot()
