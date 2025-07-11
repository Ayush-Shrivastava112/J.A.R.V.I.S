import pygame
import math
import sys
import multiprocessing
import time
from multiprocessing import Value

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Marcos Listening Orb")

# Colors
NAVY_BLUE = (10, 10, 40)
GLOW_COLOR = (0, 150, 255)

# Orb details
center = (WIDTH // 2, HEIGHT // 2)
orb_radius = 60
particle_count = 20
rotation_speed = 0.03
angle = 0

def run_orb(is_listening):
    global angle
    clock = pygame.time.Clock()

    while True:
        screen.fill(NAVY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Glow effect if listening
        if is_listening.value:
            glow_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            for i in range(4):
                pygame.draw.circle(glow_surface, (0, 150, 255, 50 - i * 10), center, orb_radius + 30 + i * 10)
            screen.blit(glow_surface, (0, 0))

        # Draw central orb
        pygame.draw.circle(screen, GLOW_COLOR, center, orb_radius)

        # Draw rotating particles (orbit rings)
        for i in range(particle_count):
            particle_angle = angle + i * (360 / particle_count)
            radian = math.radians(particle_angle)
            x = center[0] + math.cos(radian) * (orb_radius + 30)
            y = center[1] + math.sin(radian) * (orb_radius + 10)
            pygame.draw.circle(screen, (0, 255, 255), (int(x), int(y)), 3)

        # Update rotation angle
        if is_listening.value:
            angle += rotation_speed * 60
            angle %= 360

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    is_listening = Value('b', False)
    orb_process = multiprocessing.Process(target=run_orb, args=(is_listening,))
    orb_process.start()

    # Simulated Marcos voice assistant loop
    import speech_recognition as sr
    import pyttsx3
    import webbrowser
    import requests
    from datetime import datetime

    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    def speak(text):
        print(f"[Marcos]: {text}")
        engine.say(text)
        engine.runAndWait()

    def processcommand(c):
        c = c.lower().strip()

        if "open google" in c:
            webbrowser.open("https://google.com")
            speak("Opening Google.")
        elif "open youtube" in c:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        elif "search" in c:
            query = c.replace("search for", "").replace("search", "").strip()
            if query:
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("Please say what you want me to search for.")
        elif "time" in c or "date" in c:
            now = datetime.now()
            current_time = now.strftime("%I:%M %p")
            current_date = now.strftime("%A, %d %B %Y")
            if "time" in c:
                speak(f"The current time is {current_time}")
            if "date" in c:
                speak(f"Today's date is {current_date}")
        elif "stop" in c or "exit" in c:
            speak("Goodbye Sir!")
            sys.exit()
        else:
            speak("Sorry, I didn't understand that.")

    while True:
        try:
            with sr.Microphone() as source:
                speak("Say 'Marcos' to activate.")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source)
            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if "marcos" in word.lower():
                is_listening.value = True
                speak("Yes Sir. How may I help you?")

                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(audio)
                    print("Command Heard:", command)

                processcommand(command)
                is_listening.value = False

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
