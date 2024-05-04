import flask
from flask import request
from flask_cors import CORS
from flask import session
from utils.pelaaja import *
import secrets
import string
from data.tehtavan_luonti_algoritmi import luo_tehtava
from utils.easter_eggs import *
from utils.kauppa_valikko import *
from utils.valikko import valikko
from Assets.ASCII_art import game_over
from Assets.animaatio import *
import asyncio


app = flask.Flask(__name__)
CORS(app)


def generate_secret_key(length=20):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))
app.secret_key = generate_secret_key()


missions = []
async def get_missions():
    if pelaaja.tehtava_aktiivinen == False and Tehtava.instance_count < 3:
        tasks = [
            asyncio.create_task(luo_tehtava(pelaaja.location)) for _ in range(3)
        ]
        t1, t2, t3 = await asyncio.gather(*tasks)
        missions.append(t1)
        missions.append(t2)
        missions.append(t3)
    return missions


@app.route('/login', methods=['POST'])
def login():
    login_data = request.json

    username = login_data.get('username')
    password = login_data.get('password')
    user_id = sql_db_lookup_log_in(username, password)

    if user_id:
        global pelaaja
        pelaaja = initialize_player(user_id[0][0])
        initialize_items(pelaaja)
        asyncio.run(get_missions())
        return flask.jsonify({'message': 'Login successful'})
    else:
        return flask.jsonify({'error': 'Invalid username or password'}), 401


@app.route('/complete_mission', methods=['GET'])
def complete_mission():
    if 'pelaaja' in globals():
        mission_index = int(request.args.get('mission_index'))
        if mission_index:
            pelaaja.aseta_tehtava(missions[mission_index - 1])
            pelaaja.suorita_tehtava()
            Tehtava.instance_count -= 3
            missions.clear()
            asyncio.run(get_missions())
            return flask.jsonify({'message': 'Mission completed successfully'})
        else:
            return flask.jsonify({'error': 'Invalid mission index'}), 400
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/get_missions')
def get_mission_info():
    return {
        'mission1': [
            missions[0].lookup_co2_consumed(),
            missions[0].lookup_airport(),
            missions[0].lookup_country()
        ],
        'mission2': [
            missions[1].lookup_co2_consumed(),
            missions[1].lookup_airport(),
            missions[1].lookup_country()
        ],
        'mission3': [
            missions[2].lookup_co2_consumed(),
            missions[2].lookup_airport(),
            missions[2].lookup_country()
        ]
    }


@app.route('/player_info', methods=['GET'])
def get_player_info():
    if 'pelaaja' in globals():
        player_info = {
            'nimi': pelaaja.nimi,
            'id': pelaaja.id,
            'pisteet': pelaaja.pisteet,
            'location': pelaaja.location,
            'country' : pelaaja.hae_pelaaja_Maa(),
            'co2_consumed': pelaaja.co2_consumed,
            'tehtava_aktiivinen': pelaaja.tehtava_aktiivinen,
            'current_tehtava': pelaaja.current_tehtava,
            'co2_budget': pelaaja.co2_budget,
            'co2_kerroin': pelaaja.co2_kerroin,
            'piste_kerroin': pelaaja.piste_kerroin,
            'tiirikka': pelaaja.tiirikka
        }
        return flask.jsonify(player_info)
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/leaderboard_info', methods=['GET'])
def leaderboard_info():
    results = sql_db_lookup_screen_names_pisteet()
    return flask.jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=3000)