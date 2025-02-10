import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize
import threading
import requests

# Define the base URL and API key for the weather service
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "0e3b99179c3bdd74ae6091455ae01d15"

# Initialize the recognizer and the text-to-speech engine globally
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_lock = threading.Lock()

# Ensure NLTK data is downloaded
nltk.download('punkt')

# Set the voice to a male voice if available
def set_male_voice():
    """Set the voice to a male voice if available."""
    voices = engine.getProperty('voices')
    for voice in voices:
        if "David" in voice.name:
            engine.setProperty('voice', voice.id)
            print(f"Voice set to: {voice.name}")
            return
    print("No male voice found. Using default voice.")

# Call the function to set the voice
set_male_voice()

def speak(text):
    """Function to speak text using pyttsx3."""
    with engine_lock: 
        print(f"Speaking: {text}") 
        engine.say(text)
        engine.runAndWait()

def listen():
    """Function to listen to microphone and recognize speech."""
    print("Starting microphone listening...")
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("Listening... Please speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Audio captured.")
            command = recognizer.recognize_google(audio, language='en-GB')
            print(f"User said: {command}")  
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
            speak("Listening timed out. Please speak again.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            print(f"Sorry, my speech service is down. Error: {e}")
            speak("Sorry, my speech service is down.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            speak(f"An unexpected error occurred: {e}")
            return None

def get_weather(city):
    """Fetch weather information for a specific city."""
    complete_url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    try:
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            return f"The temperature in {city} is {temp}°C with {weather_desc}."
        else:
            return f"Sorry, I couldn't find the weather for {city}."
    except Exception as e:
        return f"An error occurred while fetching weather: {e}"

def process_command(command):
    """Function to process the user's command."""
    if not command:
        return "No command received."

    print(f"Processing command: {command}")
    tokens = word_tokenize(command)
    print(f"Tokens: {tokens}") 

    command_lower = command.lower()

    if "hello" in tokens:
        return "Hello! How can I assist you?"
    elif "time" in command_lower or "what is the time" in command_lower or "tell me the time" in command_lower:
        import datetime
        now = datetime.datetime.now()
        return f"The time is {now.strftime('%H:%M')}"
    elif "date" in command_lower:
        import datetime
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}"
    elif "weather" in command_lower:
        words = command_lower.split()
        if "in" in words:
            city = words[words.index("in") + 1]
            return get_weather(city)
        else:
            return "Please specify a city to check the weather."
    elif "exit" in tokens or "quit" in tokens:
        return "Goodbye!"
    else:
        return "I am not sure how to help with that."

def wake_word_listen():
    """Function to listen for the wake word and activate the assistant."""
    print("Listening for the wake word 'Hello'...")
    while True:
        command = listen()
        if command and "hello" in command:
            speak("I am your personal voice assistant. How can I help you?")
            break
        else:
            print("Didn't hear 'Hello'. Listening again...")
            continue

def run_assistant():
    """Function to run the assistant, listen for the wake word, and then process commands."""
    print("Assistant is waiting for wake word...")
    
    # Step 1: Wait for the wake word to start
    wake_word_listen()

    # Step 2: Now the assistant is active and ready to process further commands
    while True:
        print("Waiting for command...")
        command = listen()
        if command:
            response = process_command(command)
            speak(response)
            if response == "Goodbye!":
                break  
        else:
            print("No command received. Listening again...")
            continue

# Function to start the assistant in a separate thread
def start_assistant_thread():
    """Function to start the assistant in a background thread."""
    print("Starting assistant thread...")
    assistant_thread = threading.Thread(target=run_assistant)
    assistant_thread.daemon = True 
    assistant_thread.start()

# Main block to test the voice assistant
if __name__ == "__main__":
    start_assistant_thread()