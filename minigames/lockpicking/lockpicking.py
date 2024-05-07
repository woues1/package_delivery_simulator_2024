from flask import Flask, Response, request
from flask_cors import CORS
from data.sql_db_query import *

app = Flask(__name__)
CORS(app)

@app.route('/update_points/<int:userid>', methods=['POST'])
def update_points(userid):
    x = random.choice([50, 100, 150])
    sql_db_update_pisteet(userid, x)
    return Response(status=200)

@app.route('/value', methods=['GET'])
def value():
    x = random.choice([True, False])
    result = {
        'value' : x
    }
    return result

@app.route('/random_number', methods=['GET'])
def lockpicking_start():
    x = random.randint(-75, 75)
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