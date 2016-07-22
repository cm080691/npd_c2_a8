from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Pradeep More"

@app.route('/helloworld')
def helloworld():
    return "Hello, world"

@app.route('/currentservertime')
def currentservertime():
    return str(datetime.now())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
