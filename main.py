from flask import Flask
from key import API_KEY
from api import api

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)