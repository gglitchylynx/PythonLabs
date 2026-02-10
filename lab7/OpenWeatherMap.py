import requests
import json

def get_weather(city_name):
    api_key = '2f44ab8d94825710392977b37c24d3ac'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric', 
        'lang': 'ru'  
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        data = response.json()
        
        
        print(f"\n{'='*50}")
        print(f"ПОГОДА В ГОРОДЕ: {data['name']}, {data['sys']['country']}")
        print(f"{'='*50}")
        
        print(f" Температура: {data['main']['temp']:.1f}°C")
        print(f"   Ощущается как: {data['main']['feels_like']:.1f}°C")
        print(f"   Минимальная: {data['main']['temp_min']:.1f}°C")
        print(f"   Максимальная: {data['main']['temp_max']:.1f}°C")
        
        print(f" Влажность: {data['main']['humidity']}%")
        print(f" Давление: {data['main']['pressure']} гПа")
        
        weather_desc = data['weather'][0]['description'].capitalize()
        print(f" Погодные условия: {weather_desc}")
        
        print(f" Скорость ветра: {data['wind']['speed']} м/с")
        
        if 'deg' in data['wind']:
            wind_direction = data['wind']['deg']
            directions = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']
            idx = round(wind_direction / 45) % 8
            print(f"   Направление ветра: {wind_direction}° ({directions[idx]})")
        
        print(f" Видимость: {data.get('visibility', 'Н/Д')} метров")
        print(f" Облачность: {data['clouds']['all']}%")
        
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        from datetime import datetime
        sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M')
        sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M')
        print(f" Восход: {sunrise_time}")
        print(f" Закат: {sunset_time}")
        
        print(f"{'='*50}")
        
    except requests.exceptions.HTTPError as err:
        print(f"HTTP ошибка: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка соединения: {err}")
    except (KeyError, json.JSONDecodeError) as err:
        print(f"Ошибка обработки данных: {err}")


city_name = 'Moscow'  
get_weather(city_name)


if __name__ == "__main__":
    while True:
        print("\n=== Программа прогноза погоды ===")
        city = input("Введите название города (или 'exit' для выхода): ")
        
        if city.lower() == 'exit':
            print("До свидания!")
            break
            
        if city.strip():
            get_weather(city)
        else:
            print("Пожалуйста, введите название города.")