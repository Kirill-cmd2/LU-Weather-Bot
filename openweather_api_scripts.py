from datetime import datetime
import requests
from pprint import pprint

from config import code_to_emoji


async def get_weather(city, token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = r.json()

        # pprint(data)


        city = data['name']
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')

        temperature = data['main']['temp']
        feelslike = data['main']['feels_like']

        humidity = data['main']['humidity']

        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset'])

        sunrise_minute = f"0{sunrise_timestamp.minute}" if sunrise_timestamp.minute < 10 else sunrise_timestamp.minute
        sunrise_second = f"0{sunrise_timestamp.second}" if sunrise_timestamp.second < 10 else sunrise_timestamp.second
        sunset_minute = f"0{sunset_timestamp.minute}" if sunset_timestamp.minute < 10 else sunset_timestamp.minute
        sunset_second = f"0{sunset_timestamp.second}" if sunset_timestamp.second < 10 else sunset_timestamp.second
 
        sunrise_time = f"{sunrise_timestamp.hour}:{sunrise_minute}:{sunrise_second}"
        sunset_time = f"{sunset_timestamp.hour}:{sunset_minute}:{sunset_second}"

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_emoji:
            weather_in_emoji = code_to_emoji[weather_description]
        else:
            weather_in_emoji = "Oynadan qara, ob-havo qandayligini tushunib bo'lmayabdi!"

        text = f"{city}\n{current_time} vaqtiga ko'ra\nHavo harorati {temperature} C° {feelslike} C°dek sezilib turibdi\n{weather_in_emoji}\nHavo namligi {humidity}%\nQuyosh chiqishi {sunrise_time}\nQuyosh botishi {sunset_time}"

        return text

    except:
        text = "⛔️ Shahar nomini xato yozdingiz yoki bu shahar bizning bazamizda yo'q ⛔️"
        return text
