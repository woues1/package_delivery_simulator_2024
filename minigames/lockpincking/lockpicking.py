from flask import Flask, Response, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/value', methods=['GET'])
def value():
    x = random.choice([True, False])
    result = {
        'value' : x
    }
    return result

@app.route('/random_number', methods=['GET'])
def lockpicking_start():
    x = random.randint(-90, 90)
    result = {
        'value' : x
    }
    return result

@app.route('/result', methods=['POST'])
def post_result():
    result = request.json
    print(result)
    return Response(status=200)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)