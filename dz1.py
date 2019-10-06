print('Hello World!!!')
import requests
import json
import numpy
from flask import Flask



app = Flask(__name__)
@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    curency = json.loads(text)
    return curency

if __name__ == "__main__":
    app.run()