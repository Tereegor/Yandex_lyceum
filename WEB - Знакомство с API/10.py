import requests


def get_coords(address, api_key):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
        "apikey": api_key,
        "format": "json"
    }
    response = requests.get(url, params=params).json()
    pos = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    lst = pos.split()
    return float(lst[0]), float(lst[1])


def find_nearest_metro(coords, api_key):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": f"{coords[0]},{coords[1]}",
        "kind": "metro",
        "apikey": api_key,
        "format": "json",
        "results": 1
    }
    response = requests.get(url, params=params).json()
    return response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]


api_key = "b10a9349-4199-4487-bb51-22fbe04894a8"
address = input("Введите адрес: ")
coords = get_coords(address, api_key)
print(f"Ближайшая станция метро: {find_nearest_metro(coords, api_key)}")
