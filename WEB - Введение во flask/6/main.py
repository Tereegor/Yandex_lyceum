from flask import Flask, render_template

app = Flask(__name__)

colors = ["secondary", "success", "secondary", "warning", "danger"]


@app.route("/choice/<planet_name>")
def choice(planet_name):
    if planet_name.lower() == "mars":
        return render_template("mars.html", planet_name=planet_name, colors=colors)
    elif planet_name.lower() == "venus":
        return render_template("venus.html", planet_name=planet_name, colors=colors)
    elif planet_name.lower() == "jupiter":
        return render_template("jupiter.html", planet_name=planet_name, colors=colors)
    else:
        return "Планета не найдена", 404


if __name__ == "__main__":
    app.run(debug=True)
