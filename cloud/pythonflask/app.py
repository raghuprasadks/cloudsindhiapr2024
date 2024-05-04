from flask import Flask

app = Flask(__name__)

@app.route('/')
def init():
    return "flask on docker"


@app.route('/hello')
def hello():
    return "Welcome to python"

@app.route('/welcome')
def welcome():
    return "I am learning flask"


if (__name__ == "__main__"):
    app.run(port=5000, host="0.0.0.0")

