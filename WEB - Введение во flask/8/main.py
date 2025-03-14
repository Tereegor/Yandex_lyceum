import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/img/"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "photo" in request.files:
            photo = request.files["photo"]
            if photo.filename != "":
                photo_path = os.path.join(app.config["UPLOAD_FOLDER"], "uploaded_photo.jpg")
                photo.save(photo_path)
                return redirect(url_for("index"))
    photo_exists = os.path.exists(os.path.join(app.config["UPLOAD_FOLDER"], "uploaded_photo.jpg"))
    return render_template("index.html", photo_exists=photo_exists)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
