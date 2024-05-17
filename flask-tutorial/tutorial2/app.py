from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/<name>")
def home(name):
    return render_template("index.html", content=name, number=2, list_content=["jim", "lili", "moody"])


@app.route("/home2")
def home2():
    return render_template("index2.html", list_content=["jim", "lili", "moody"])


if __name__ == "__main__":
    app.run()
