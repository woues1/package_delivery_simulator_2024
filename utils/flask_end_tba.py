import flask
from flask_cors import CORS
from data.sql_db_query import *


app = flask.Flask(__name__)
CORS(app)

@app.route('/leaderboard_info', methods=['GET'])
def leaderboard_info():
    results = sql_db_lookup_screen_names_pisteet()
    return flask.jsonify(results)

@app.route('/login', methods=['POST'])
def login():

    login_data = flask.request.json

    username = login_data.get('username')
    password = login_data.get('password')
    user_id = sql_db_lookup_log_in(username, password)
    if user_id is not None:
        return flask.jsonify({'message': 'Login successful'})
    else:

        return flask.jsonify({'error': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)