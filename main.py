from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/python')
def python():
    return render_template("python.html")


if __name__ == "__main__":
    app.run(port=5000, host="localhost")
