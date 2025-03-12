import requests

api_key = "8013b162-6b42-4997-9691-77b7074026e0"
address = "Красная площадь, 1, Москва"

url = f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={address}&format=json"
response = requests.get(url).json()
toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]

print("Полный адрес:", toponym["metaDataProperty"]["GeocoderMetaData"]["text"])
print("Координаты:", toponym["Point"]["pos"])
