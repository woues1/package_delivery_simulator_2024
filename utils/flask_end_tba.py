import flask
import requests
from flask import request
from flask_cors import CORS
from flask import session
from utils.pelaaja import *
import secrets
import string
from data.tehtavan_luonti_algoritmi import luo_tehtava
import asyncio
import re

app = flask.Flask(__name__)
CORS(app)

app.config['PERMANENT_SESSION_LIFETIME'] = 86400

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


@app.route('/get_public_ip', methods=['GET'])
def get_public_ip():
    try:
        # Fetch public IP
        response = requests.get('https://api64.ipify.org/?format=json')
        if response.ok:
            ip_data = response.json()
            public_ip = ip_data['ip']

            # Fetch current time using WorldTimeAPI
            world_time_response = requests.get(f'https://worldtimeapi.org/api/ip?{public_ip}')
            if world_time_response.ok:
                world_time_data = world_time_response.json()
                current_time = world_time_data['datetime']

                # Return both public IP and current time
                return flask.jsonify({'public_ip': public_ip, 'current_time': current_time}), 200
            else:
                return flask.jsonify({'error': 'Failed to fetch current time'}), world_time_response.status_code
        else:
            return flask.jsonify({'error': 'Failed to fetch public IP'}), response.status_code
    except Exception as e:
        return flask.jsonify({'error': str(e)}), 500


items = []
@app.route('/login', methods=['POST'])
def login():

    login_data = request.json
    username = login_data.get('username')
    password = login_data.get('password')
    user_id = sql_db_lookup_log_in(username, password)

    if user_id:
        session.clear()
        global pelaaja
        pelaaja = initialize_player(user_id[0][0])
        init_items = initialize_items(pelaaja)
        if len(items) > 0:
            items.clear()
        list = [*init_items]
        items.extend(list)
        list.clear()
        session.permanent = True
        asyncio.run(get_missions())
        return flask.jsonify({'message': 'Login successful', 'user_id': user_id[0][0]})
    else:
        return flask.jsonify({'error': 'Invalid username or password'}), 401


@app.route('/new_game', methods=['POST'])
def new_game():
    new_game_data = request.json
    username = new_game_data.get('username')
    password = new_game_data.get('password')
    screen_names = sql_db_lookup_screen_names(username)

    if screen_names:
        return flask.jsonify({'error': 'Username is already in use'}), 400
    if re.search(r'[\'\"]', password):
        return flask.jsonify({'error': 'Invalid character in password'}), 400
    else:
        user_id = sql_db_update_new_game(username, password)
        if user_id:
            session.clear()
            sql_db_update_new_player_items(user_id[0][0])
            global pelaaja
            pelaaja = initialize_player(user_id[0][0])
            init_items = initialize_items(pelaaja)
            if len(items) > 0:
                items.clear()
            list = [*init_items]
            items.extend(list)
            list.clear()
            session.permanent = True
            asyncio.run(get_missions())
            return flask.jsonify({'message': 'Login successful', 'user_id': user_id[0][0]})
        else:
            return flask.jsonify({'error': 'Invalid username or password'}), 401


@app.route('/set_mission', methods=['GET'])
def set_mission():
    if 'pelaaja' in globals():
        mission_index = int(request.args.get('mission_index'))
        if mission_index:
            pelaaja.aseta_tehtava(missions[mission_index - 1])
            return flask.jsonify({'message': 'Mission set successfully'})
        else:
            return flask.jsonify({'error': 'Invalid mission index'}), 400
    return flask.jsonify({'error': 'Invalid player session'}), 400


@app.route('/complete_mission')
def complete_mission():
    if 'pelaaja' in globals() and pelaaja.tehtava_aktiivinen == True:
        pelaaja.suorita_tehtava()
        Tehtava.instance_count -= 3
        missions.clear()
        asyncio.run(get_missions())
        sql_db_update_exit_game(pelaaja.nimi, pelaaja.co2_consumed, pelaaja.location, pelaaja.pisteet)
        return flask.jsonify({'message': 'Mission completed successfully'})
    else:
        return flask.jsonify({'error': 'Invalid mission index'}), 400


@app.route('/get_missions_info')
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
            'pisteet': pelaaja.pisteet,
            'location': pelaaja.location,
            'country' : pelaaja.hae_pelaaja_Maa(),
            'co2_consumed': pelaaja.co2_consumed,
            'co2_budget': pelaaja.co2_budget
        }
        return flask.jsonify(player_info)
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/item_info', methods=['GET'])
def get_item_info():
    if 'pelaaja' in globals():
        item_info = []

        for item in items:
            item_data = {
                'id': item.id,
                'name': item.name,
                'price': item.price,
                'attribute': item.attribute,
                'purchased': item.purchased
            }
            item_info.append(item_data)
        return flask.jsonify(item_info)
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/buy_item', methods=['GET'])
def buy_item():
    if 'pelaaja' in globals():
        item_index = int(request.args.get('item_id'))
        purchase = items[item_index - 1].purchase(pelaaja)
        if purchase == True:
            pelaaja.add_item(items[item_index - 1])
            return flask.jsonify({'message': 'Item bought successfully'})
        else:
            return flask.jsonify({'message': f'{purchase}'})


@app.route('/leaderboard_info', methods=['GET'])
def leaderboard_info():
    results = sql_db_lookup_screen_names_pisteet()
    return flask.jsonify(results)


@app.route('/reset_game', methods=['GET'])
def reset_game():
    if 'pelaaja' in globals():
        pelaaja.reset_game()
        for item in items:
            item.purchased = False
        return flask.jsonify({'message': 'Game reset successfully'})
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/exit_game', methods=['GET'])
def exit_game():
    if 'pelaaja' in globals():
        sql_db_update_exit_game(pelaaja.nimi, pelaaja.co2_consumed, pelaaja.location, pelaaja.pisteet)
        return flask.jsonify({'message': 'Game exited successfully'})
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/update_leaderboard', methods=['GET'])
def update_leaderboard():
    if 'pelaaja' in globals():
        sql_db_update_leaderboard(pelaaja.nimi, pelaaja.pisteet)
        return flask.jsonify({'message': 'Leaderboard updated successfully'})
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/update_points', methods=['POST'])
def update_points():
    x = random.choice([50, 100, 150])
    if 'pelaaja' in globals():
        sql_db_update_pisteet(pelaaja.id, x)
        return flask.jsonify({'message': 'Points updated successfully'})
    else:
        return flask.jsonify({'error': 'Player information not available'}), 404


@app.route('/value', methods=['GET'])
def value():
    lockpick_check = items[3].purchased
    result = {
        'value' : lockpick_check
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
    return flask.Response(status=200)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='127.0.0.1', port=3000)