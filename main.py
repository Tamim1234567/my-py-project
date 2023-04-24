import requests
import pyttsx3


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
city = input("Enter the name of your city : ")
querystring = {"city": city}

headers = {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": "9ca47a7a77msh10c4d73084f8c1ap1779b3jsnece42c204434",
    "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

temp = response.json()['temp']
humidity = response.json()['humidity']
mintemp = response.json()['min_temp']
maxtemp = response.json()['max_temp']
fell_temp = response.json()['feels_like']
wind_speed = response.json()['wind_speed']

say(f"Corrent temperature is {mintemp} degrees to {maxtemp} but it feels like {fell_temp} and wind speed is {wind_speed} kilometers per hour and humidity is {humidity}%")
