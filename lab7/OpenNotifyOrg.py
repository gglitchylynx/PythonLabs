import requests
import json
import datetime

def save_json_data():
    """Просто получает данные и сохраняет их в JSON файлы"""
    
    print("Начинаю получение данных с open-notify.org...")
    print("-" * 50)
    
    #данные о космонавтах
    print("1. Получаю данные о космонавтах в космосе...")
    try:
        response = requests.get("http://api.open-notify.org/astros.json", timeout=10)
        if response.status_code == 200:
            astronauts_data = response.json()
            
            # время получения
            astronauts_data['retrieved_at'] = datetime.datetime.now().isoformat()
            astronauts_data['source'] = 'open-notify.org/astros.json'
            
            # сохранение
            with open('astronauts_in_space.json', 'w', encoding='utf-8') as f:
                json.dump(astronauts_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Сохранено: astronauts_in_space.json")
            print(f"   Космонавтов: {astronauts_data.get('number', 0)}")
            print(f"   Сообщение: {astronauts_data.get('message', 'N/A')}")
        else:
            print(f"❌ Ошибка HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    print("-" * 50)
    
    # положение МКС
    print("2. Получаю данные о положении МКС...")
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
        if response.status_code == 200:
            iss_data = response.json()
            
            #время
            iss_data['retrieved_at'] = datetime.datetime.now().isoformat()
            
            # timestamp
            if 'timestamp' in iss_data:
                timestamp = iss_data['timestamp']
                dt = datetime.datetime.fromtimestamp(timestamp)
                iss_data['readable_time'] = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
            
            iss_data['source'] = 'open-notify.org/iss-now.json'
            
            # сохранение
            with open('iss_position.json', 'w', encoding='utf-8') as f:
                json.dump(iss_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Сохранено: iss_position.json")
            
            if 'iss_position' in iss_data:
                pos = iss_data['iss_position']
                print(f"   Координаты МКС:")
                print(f"     Широта: {pos.get('latitude', 'N/A')}°")
                print(f"     Долгота: {pos.get('longitude', 'N/A')}°")
            
            if 'timestamp' in iss_data:
                print(f"   Время данных: {iss_data.get('readable_time', 'N/A')}")
        else:
            print(f"❌ Ошибка HTTP: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    
    print("-" * 50)
    print("Готово! JSON файлы созданы в текущей папке.")
    print("Созданные файлы:")
    print("  - astronauts_in_space.json")
    print("  - iss_position.json")

if __name__ == "__main__":
    save_json_data()