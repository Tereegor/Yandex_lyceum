from flask import Flask, render_template

app = Flask(__name__)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return render_template("results.html", nickname=nickname, level=level, rating=rating)


if __name__ == "__main__":
    app.run(debug=True)
