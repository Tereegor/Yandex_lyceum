from flask import Flask, render_template

app = Flask(__name__)


@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        title = "Инженерные тренажеры"
        image = "engineering_scheme.png"
    else:
        title = "Научные симуляторы"
        image = "science_scheme.png"

    return render_template("training.html", title=title, image=image)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
