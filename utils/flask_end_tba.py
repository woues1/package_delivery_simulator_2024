import flask
from flask_cors import CORS
from data.sql_db_query import *


app = flask.Flask(__name__)
CORS(app)

@app.route('/leaderboard_info', methods=['GET'])
def leaderboard_info():
    results = sql_db_lookup_screen_names_pisteet()
    return flask.jsonify(results)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)