import requests
import json

def main():
    print("Welcome to the weather app.")
    user_location = input('Which city would you like the current weather for?\n')

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_location}&units=metric&appid=59abeaf902cbe89fece94e4fbcb1074f')

    data = res.json()
    weather_report(data)


def weather_report(data):
    print(f"The current temperature in {data['name']} is {data['main']['temp']}°c with {data['weather'][0]['description']}.")

if __name__ == '__main__':
    main()