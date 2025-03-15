import requests


def get_lat(city, api_key):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"geocode": city, "apikey": api_key, "format": "json"}
    response = requests.get(url, params=params).json()
    pos = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    return float(pos.split()[1])


def main():
    api_key = "b10a9349-4199-4487-bb51-22fbe04894a8"
    cities = input("Введите список городов: ").split(",")
    cts = []
    for city in cities:
        city = city.strip()
        lat = get_lat(city, api_key)
        cts.append((city, lat))
    southern_city = cts[0][0]
    min_lat = cts[0][1]
    for city, lat in cts:
        if lat < min_lat:
            southern_city = city
            min_lat = lat
    print(f"Самый южный город: {southern_city}")


if __name__ == "__main__":
    main()
