import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import requests
import webbrowser

# 🔊 Text-to-speech engine setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed
engine.setProperty('volume', 1.0)  # Volume level

# 🗣️ Function to make the assistant speak
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# 🎤 Function to listen and recognize voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand your speech.")
    except sr.RequestError:
        speak("There was a problem connecting to the speech service.")
    except Exception as e:
        print("Error:", e)
        speak("An error occurred.")
    return ""

# 📧 Fake email preview (no actual sending)
def send_email(to, subject, body):
    speak("📝 Here is a preview of your message.")
    speak(f"To: {to}")
    speak(f"Subject: {subject}")
    speak(f"Message: {body}")
    
    # Open Gmail to simulate email sending
    webbrowser.open("https://mail.google.com")
    speak("📨 Gmail has been opened in your browser.")

# 🌦️ Function to fetch and speak the weather report
def get_weather(city="Chennai"):
    api_key = "your_openweather_api_key"  # Replace with your actual OpenWeather API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The weather in {city} is currently {description} with a temperature of {temp} degrees Celsius.")
    except Exception as e:
        speak("❌ Sorry, I couldn't fetch the weather details.")
        print("Weather Error:", e)

# 🧠 Main assistant function
def run_assistant():
    speak("Hi! How can I help you today?")
    while True:
        command = take_command()

        if "hello" in command:
            speak("Hello! How are you?")
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}.")
        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}.")
        elif "search" in command:
            topic = command.replace("search", "").strip()
            if topic:
                speak(f"Searching Google for {topic}.")
                pywhatkit.search(topic)
            else:
                speak("Please tell me what to search for.")
        elif "weather" in command:
            speak("Sure. Which city's weather would you like to know?")
            city = take_command()
            if city:
                get_weather(city)
        elif "send email" in command:
            speak("Please say the recipient's email address.")
            to = take_command()
            speak("What is the subject?")
            subject = take_command()
            speak("What would you like to say in the message?")
            body = take_command()
            if to and subject and body:
                send_email(to, subject, body)
            else:
                speak("⚠️ Sorry, the email information is incomplete.")
        elif "exit" in command or "bye" in command:
            speak("👋 Goodbye! Have a great day.")
            break
        elif command != "":
            speak("😅 Sorry, I didn't understand that. Please try again.")

# 🚀 Start the assistant
run_assistant()