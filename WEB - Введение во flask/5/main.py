from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return index


if __name__ == "__main__":
    with open("template/index.html", "r", encoding="UTF-8") as file:
        index = file.read()
    file.close()
    app.run(port=8080, host="127.0.0.1")
