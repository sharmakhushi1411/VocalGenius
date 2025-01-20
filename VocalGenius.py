import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import random
import subprocess
from threading import Timer
import re  # Import regular expressions for parsing math expressions

# Initialize pyttsx3 for speech synthesis
engine = pyttsx3.init()

# Set Female Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voices[1] is typically female; adjust if necessary
engine.setProperty('rate', 130)  # Adjust speaking speed if needed

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    try:
        print("Listening...")
        speak("Listening...")
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        print("Recognizing...")
        speak("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not get that. Please try again.")
        speak("Sorry, I did not get that. Please try again.")
        return "None"
    except sr.RequestError:
        print("Sorry, the speech recognition service is unavailable.")
        speak("Sorry, the speech recognition service is unavailable.")
        return "None"
    return query.lower()

# Your other functions like time, date, games etc. go here
def time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def date():
    today = datetime.datetime.now()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def open_website(site_name):
    speak(f"Opening {site_name}")
    webbrowser.open(f"{site_name}.com")

def play_random_game():
    games = ["coin_toss.py", "Maze_puzzle.py", "Memory_test_game.py", "Rock_paper_scissors.py", "tictactoe.py"]
    selected_game = random.choice(games)
    subprocess.run(['python', selected_game])

def setReminder(reminder_time, message):
    current_time = datetime.datetime.now()

    # Parse the reminder time
    reminder_hour, reminder_minute = map(int, reminder_time.split(':'))
    target_time = current_time.replace(hour=reminder_hour, minute=reminder_minute, second=0, microsecond=0)

    # If the target time is in the past, set it for the next day
    if target_time < current_time:
        target_time += datetime.timedelta(days=1)

    delay = (target_time - current_time).total_seconds()

    # Schedule the reminder
    Timer(delay, remindUser, [message]).start()

def remindUser(message):
    speak(f"Reminder! Reminder! It is {message} time.")

def play_music(song_name, singer_name):
    # Open Spotify web player and search for the song
    query = f"{song_name} by {singer_name}"
    webbrowser.open(f"https://open.spotify.com/search/{query}")

def check_symptoms(symptoms):
    """Check symptoms and return related information from Wikipedia."""
    speak("Checking symptoms...")
    results = wikipedia.summary(symptoms, sentences=3)  # Retrieve a brief summary from Wikipedia
    speak("According to Wikipedia")
    print(results)
    speak(results)

def today_motivation():
    quotes = [
        "The only way to do great work is to love what you do. Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Your limitation, it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn't just find you. You have to go out and get it.",
        "The harder you work for something, the greater you'll feel when you achieve it.",
        "We cannot solve problems with the kind of thinking we employed when we came up with them.",
        "Learn as if you will live forever, live like you will die tomorrow.",
        "Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.",
        "When you give joy to other people, you get more joy in return. You should give a good thought to the happiness that you can give out.",
        "When you change your thoughts, remember to also change your world.",
        "It is only when we take chances that our lives improve. The initial and the most difficult risk we need to take is to become honest.",
        "Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together."
    ]
    selected_quote = random.choice(quotes)
    speak(f"Today's motivation: {selected_quote}")
    print(selected_quote)

def calculator(expression):
    """Evaluate a simple mathematical expression."""
    try:
        # Remove any invalid characters
        expression = re.sub(r'[^0-9+\-*/().]', '', expression)
        # Evaluate the expression
        result = eval(expression)
        return result
    except Exception as e:
        return "Sorry, I couldn't calculate that."

# Main function to handle commands
if __name__ == "__main__":
    speak("Hello, I am VocalGenius. Would you prefer text or speech commands?")
    command_mode = takeCommand()

    if 'text' in command_mode:
        print("Text mode activated.")
        while True:
            user_input = input("Type your command: ")
            if 'time' in user_input:
                print(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
            elif 'play game' in user_input:
                play_random_game()
            elif 'date' in user_input:
                date()
            elif 'open youtube' in user_input:
                open_website("youtube")
            elif 'open google' in user_input:
                open_website("google")
            elif 'wikipedia' in user_input:
                search_wikipedia(user_input)
            elif 'set reminder' in user_input:
                reminder_time = input("What time should I set the reminder for? Please say it in the format HH:MM: ")
                reminder_message = input("What is the reminder for? ")
                setReminder(reminder_time, reminder_message)
                speak(f"Reminder set for {reminder_time} for {reminder_message}.")
            elif 'play' in user_input and 'by' in user_input:
                # Extract song and singer name from the command
                parts = user_input.split('play ')[1].split(' by ')
                if len(parts) == 2:
                    song_name = parts[0].strip()
                    singer_name = parts[1].strip()
                    play_music(song_name, singer_name)
                    speak(f"Playing {song_name} by {singer_name}.")
                else:
                    print("Please specify the song and singer correctly.")
            elif 'check symptoms' in user_input:
                symptoms = input("Please list your symptoms: ")
                check_symptoms(symptoms)
            elif "today's motivation" in user_input:
                today_motivation()
            elif 'calculator' in user_input:
                expression = input("Please enter the expression you want to calculate: ")
                result = calculator(expression)
                speak(f"The result is {result}.")
                print(f"The result is {result}.")
            elif 'exit' in user_input or 'quit' in user_input:
                speak("Goodbye!")
                break
            else:
                print("I did not understand. Please try again.")

    elif 'speech' in command_mode:
        print("Speech mode activated.")
        speak("Speech mode activated.")
        while True:
            query = takeCommand()

            if 'time' in query:
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                speak(f"The time is {current_time}")
            elif 'play game' in query:
                play_random_game()
            elif 'date' in query:
                date()
            elif 'open youtube' in query:
                open_website("youtube")
            elif 'open google' in query:
                open_website("google")
            elif 'wikipedia' in query:
                search_wikipedia(query)
            elif 'set reminder' in query:
                speak("What time should I set the reminder for? Please say it in the format HH:MM.")
                reminder_time = takeCommand()
                if reminder_time != "none":
                    speak("What is the reminder for?")
                    reminder_message = takeCommand()
                    if reminder_message != "none":
                        setReminder(reminder_time, reminder_message)
                        speak(f"Reminder set for {reminder_time} for {reminder_message}.")
                    else:
                        speak("I didn't catch the reminder message.")
                else:
                    speak("I didn't catch the reminder time.")
            elif 'play' in query and 'by' in query:
                parts = query.split('play ')[1].split(' by ')
                if len(parts) == 2:
                    song_name = parts[0].strip()
                    singer_name = parts[1].strip()
                    play_music(song_name, singer_name)
                    speak(f"Playing {song_name} by {singer_name}.")
                else:
                    speak("Please specify the song and singer correctly.")
            elif 'check symptoms' in query:
                speak("Please list your symptoms.")
                symptoms = takeCommand()
                if symptoms != "none":
                    check_symptoms(symptoms)
                else:
                    speak("I didn't catch the symptoms.")
            elif "today's motivation" in query:
                today_motivation()
            elif 'calculator' in query:
                speak("Please say the expression you want to calculate.")
                expression = takeCommand()
                result = calculator(expression)
                speak(f"The result is {result}.")
                print(f"The result is {result}.")
            elif 'exit' in query or 'quit' in query:
                speak("Goodbye!")
                break
            else:
                speak("I did not understand. Please try again.")