from flask import Flask
import time
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "App is running"

@app.route('/error')
def error():
    return "Error occurred", 500

@app.route('/slow')
def slow():
    time.sleep(5)
    return "Slow response"

@app.route('/random')
def random_error():
    if random.choice([True, False]):
        return "Random failure", 500
    return "Success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
