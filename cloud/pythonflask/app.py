from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Welcome to python"

if (__name__ == "__main__"):
    app.run(port=5000, debug=True)

