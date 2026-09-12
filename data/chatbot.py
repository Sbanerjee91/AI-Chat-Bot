import ollama

def get_ai_response(user_input):
    """Sends a message to the local Llama model and returns the response."""
    # We use llama3.2:1b matching the exact model you just pulled
    response = ollama.chat(model='llama3.2:1b', messages=[
        {
            'role': 'user',
            'content': user_input
        }
    ])
    
    # Extract and return the actual text from the response object
    return response['message']['content']

# A simple loop to test the function in your terminal
if __name__ == "__main__":
    print("Local AI connected. Type 'quit' to exit.")
    
    while True:
        prompt = input("\nYou: ")
        if prompt.lower() == 'quit':
            break
            
        print("AI is thinking...")
        answer = get_ai_response(prompt)
        print(f"AI: {answer}")