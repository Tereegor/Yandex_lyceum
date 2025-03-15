from flask import Flask, render_template

app = Flask(__name__)

professions = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер по терраформированию",
    "климатолог",
    "специалист по радиационной защите",
    "астрогеолог",
    "гляциолог",
    "инженер жизнеобеспечения",
    "метеоролог",
    "оператор марсохода",
    "киберинженер",
    "штурман",
    "пилот дронов"
]


@app.route("/list_prof/<list_type>")
def list_prof(list_type):
    return render_template("list_prof.html", list_type=list_type, professions=professions)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
