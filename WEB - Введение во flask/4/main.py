from flask import Flask

lst = ["Человечество вырастает из детства.",
       "Человечеству мала одна планета.",
       "Мы сделаем обитаемыми безжизненные пока планеты.",
       "И начнем с Марса!",
       "Присоединяйся!"]

BOOTSTRAP = ('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"'
             ' integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" '
             'crossorigin="anonymous">')
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
def image():
    return f"""
    <!DOCTYPE html>
    <head>
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="/static/img/mars.png" width="300"/>
        <p>Вот она какая, красная планета</p>
    </body>
    """


@app.route("/promotion_image")
def promotion_image():
    string = f"""<!DOCTYPE html>
    <head>
        <title>Колонизация</title>
        {BOOTSTRAP}
        <link rel="stylesheet" href="static/css/style.css"/>
    </head>
    <body>
        <h1 class="red-title">Жди нас, Марс!</h1>
        <img src="/static/img/Mars.jpg" width="300"/>
    """
    colors = ["secondary", "success", "secondary", "warning", "danger"]
    for txt, clr in zip(lst, colors):
        div = f'<div class="alert alert-{clr}" role="alert">{txt}</div>'
        string += div
    string += "</body>"
    return string


if __name__ == "__main__":
    app.run(port="8080", host="127.0.0.1")
