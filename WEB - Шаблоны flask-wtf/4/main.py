from flask import Flask, render_template

app = Flask(__name__)


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    user_data = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True"
    }
    return render_template("auto_answer.html", **user_data)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
