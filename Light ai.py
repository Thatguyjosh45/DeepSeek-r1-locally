import ollama
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# User data (for personalization)
user_data = {}

# Function to speak out the AI's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please say something!")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results.")
            return ""

# Function to chat with AI
def chat_with_ai(prompt):
    try:
        response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt}])
        return response.get("message", {}).get("content", "No response content.")
    except Exception as e:
        return f"Error: {e}"

# Main loop to interact with the user via text or voice
def main():
    print("Hello, Josh! How can i help you today? - Type 'exit' to quit.")
    print("Type 'voice' to use voice interaction or 'text' for text interaction.")
    
    while True:
        # Ask if the user wants to interact with text or voice
        mode = input("Would you like to interact via text or voice? (text/voice): ").strip().lower()

        if mode == "exit":
            speak("Goodbye!")
            print("Goodbye!")
            break

        if mode == "voice":
            user_input = listen()  # Get input via voice
        elif mode == "text":
            user_input = input("You: ")
        else:
            print("Invalid mode, please type 'text' or 'voice'.")
            continue
        
        if user_input.lower() == "exit":
            speak("Goodbye!")
            print("Goodbye!")
            break


        # Get AI response and speak it
        response = chat_with_ai(user_input)
        print("AI:", response)
        speak(response)  # Output response via speech

if __name__ == "__main__":
    main()
