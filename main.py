from flask import Flask
import json

app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
    return "Not found."

@app.route('/', methods=['GET'])
def index():
    data = {"api":"hola mundo"}
    return json.dumps(data)

if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
