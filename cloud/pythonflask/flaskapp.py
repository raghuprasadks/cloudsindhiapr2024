from flask import Flask

app = Flask(__name__)

@app.route('/')
def init():
    return "flask on docker"    

@app.route('/hello') 
