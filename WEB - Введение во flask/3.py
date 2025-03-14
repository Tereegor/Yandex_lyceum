from flask import Flask

lst = ["Человечество вырастает из детства.",
       "Человечеству мала одна планета.",
       "Мы сделаем обитаемыми безжизненные пока планеты.",
       "И начнем с Марса!",
       "Присоединяйся!"]

IMAGE_URL = "https://avatars.mds.yandex.net/i?id=8acf03fb25a73bbf9777e648f1a3c3b4_l-4470294-images-thumbs&n=13"
app = Flask(__name__)


@app.route("/")
def header():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    string = ""
    for i in lst:
        string += i + "<br>"
    return string[:-5]


@app.route("/image_mars")
def image_mars():
    return f"""<!DOCTYPE html>
    <head>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{IMAGE_URL}" width="300"/>
        <p>Вот она какая, красная планета</p>
    </body>"""


if __name__ == "__main__":
    app.run(port="8080", host="127.0.0.1")
