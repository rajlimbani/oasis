import requests
import json
import pyttsx3
import datetime
import smtplib
import speech_recognition as sr

def listen_for_command():
    """
    Listens for user voice input and processes the command.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower() 
        print(f"User said: {command}")
        process_command(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please try again.")

def speak(text):
    """
    Converts text to speech and speaks it out.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    """
    Processes user commands based on recognized phrases.
    """
    if "hello" in command:
        greet_user()
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "search" in command:
        search_web(command)
    elif "weather" in command:
        get_weather(command)  
   

def greet_user():
    """
    Responds with a friendly greeting.
    """
    response = "Hello! How can I assist you today?"
    print(response)
    speak(response)

def tell_time():
    """
    Tells the current time.
    """
    current_time = datetime.datetime.now().strftime("%H:%M")
    response = f"The current time is {current_time}."
    print(response)
    speak(response)

def tell_date():
    """
    Tells the current date.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    response = f"Today's date is {current_date}."
    print(response)
    speak(response)

def search_web(query):
    """
    Searches the web for information based on user query.
    """

    pass

def get_weather(city_name):
    """
    Retrieves weather data for a specific city using the OpenWeatherMap API.
    """
    api_key = "Your_API_Key"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main_info = data["main"]
        current_temperature = main_info["temp"]
        current_pressure = main_info["pressure"]
        current_humidity = main_info["humidity"]
        weather_description = data["weather"][0]["description"]

        weather_response = f"Temperature (in Kelvin): {current_temperature}\n"
        weather_response += f"Atmospheric pressure (in hPa): {current_pressure}\n"
        weather_response += f"Humidity (in percentage): {current_humidity}\n"
        weather_response += f"Weather description: {weather_description}"
        print(weather_response)
        speak(weather_response)
    else:
        print("City Not Found")

if __name__ == "__main__":
    listen_for_command()
