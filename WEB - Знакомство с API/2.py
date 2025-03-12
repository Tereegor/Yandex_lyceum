import requests

api_key = "8013b162-6b42-4997-9691-77b7074026e0"
cities = ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]

for city in cities:
    url = f"http://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={city}&format=json"
    response = requests.get(url).json()
    toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    metadata = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]

    region = next((comp["name"] for comp in metadata if comp["kind"] == "province"), "Не указан")

    print(f"Город: {city}")
    print(f"Регион: {region}")
    print("-" * 30)