import ollama

def chat_with_ai(prompt):
    try:
        response = ollama.chat(model="deepseekr1", messages=[{"role": "user", "content": prompt}])
        return response.get("message", {}).get("content", "No response content.")
    except Exception as e:
        return f"Error: {e}"

def main():
    print("AI Chat Assistant - Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_ai(user_input)
        print("AI:", response)

if __name__ == "__main__":
    main()
