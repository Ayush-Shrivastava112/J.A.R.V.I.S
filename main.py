import speech_recognition as sr
import webbrowser
import pyttsx3
import sys
import musiclibrary  # Should contain: music = {"song name": "youtube link"}
import requests
from datetime import datetime  # ✅ Added for time/date

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "9d46f3d1b96e4c19b8de733e84ca6e0f"

def speak(text):
    print(f"[Jarvis]: {text}")
    engine.say(text)
    engine.runAndWait()

def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
        response = requests.get(url)
        news_data = response.json()
        if news_data["status"] == "ok":
            speak("Here are the top news headlines.")
            for article in news_data["articles"][:5]:
                title = article.get("title", "No title")
                description = article.get("description", "No description")
                speak(f"Headline: {title}")
                speak(f"Details: {description}")
        else:
            speak("Failed to fetch news.")
    except Exception as e:
        speak("An error occurred while fetching the news.")
        print(e)

def processcommand(c):
    c = c.lower().strip()

    # Web Commands
    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google.")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
    elif "open twitter" in c:
        webbrowser.open("https://www.twitter.com")
        speak("Opening Twitter.")
    elif "open amazon" in c:
        webbrowser.open("https://www.amazon.com")
        speak("Opening Amazon.")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
        # General Search Command
    elif "search for" in c or "search" in c:
        query = c.replace("search for", "").replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("Please say what you want me to search for.")


    # News Command
    elif "news" in c or "headlines" in c:
        get_news()

    # Time and Date Command 
    elif "time" in c or "date" in c:
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        current_date = now.strftime("%A, %d %B %Y")
        if "time" in c:
            speak(f"The current time is {current_time}")
        if "date" in c:
            speak(f"Today's date is {current_date}")

    # Music Command
    elif c.startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) < 2:
            speak("Please say the name of the song after 'play'.")
        else:
            song = parts[1].strip()
            print(f"Requested song: {song}")
            print("Available songs:", list(musiclibrary.music.keys()))
            if song in musiclibrary.music:
                link = musiclibrary.music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find {song} in your music library.")

    # Stop/Exit Command
    elif "stop" in c or "exit" in c:
        speak("Goodbye Ayush!")
        sys.exit()

    # Unknown Command
    else:
        speak("Sorry, I didn't understand that.")
    
    print(f"Command: {c}")

# Main Loop
if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        try:
            with sr.Microphone() as source:
                speak("Say 'Jarvis' to activate.")
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Yes Sir How may I help you?")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=3)
                    command = recognizer.recognize_google(audio)
                    print("Command Heard:", command)
                    processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
