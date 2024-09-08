import os
import json

import learn
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

# Directory containing the text files
maps_directory = 'maps'

# Q-learning parameters
q_table = {}
state = None
level = None
action = None

alpha = 0.
gamma = 0.
epsilon = 0.
steps = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_maps', methods=['GET'])
def get_maps():
    maps = {}
    try:
        # Check if the directory exists
        if os.path.exists(maps_directory):
            # Get a list of all files with a .txt extension
            txt_files = [f for f in os.listdir(maps_directory) if f.endswith('.txt')]

            for txt_file in txt_files:
                file_path = os.path.join(maps_directory, txt_file)

                # Read the content of the file
                with open(file_path, 'r') as file:
                    content = file.read()

                # Extract the filename without extension
                filename = os.path.splitext(txt_file)[0]

                # Add the content to the dictionary with filename as key
                maps[filename] = content

            response = jsonify({'result': 'success', 'maps': maps})
            response.headers.add("Access-Control-Allow-Origin", "*")

            return response
        else:
            return jsonify({'result': 'error', 'error_details': 'Directory not found'}), 404
        
    except Exception as e:
        error_message = {'result': 'error', 'error_details': str(e)}
        return jsonify(error_message), 500
    
@app.route('/start_search', methods=['GET'])
def start_search():
    # Get map
    map = request.args.get('map')
    head = request.args.get('head')
    head = [int(x) for x in head.split(',')]

    # parte tail in pairs
    tail = request.args.get('tail')
    if tail == '':
        tail = []
    else:
        tail = [int(x) for x in tail.split(',')]
        tail = [(tail[i], tail[i+1]) for i in range(0, len(tail), 2)]

    food = request.args.get('food')
    food = [int(x) for x in food.split(',')]

    global epsilon
    epsilon = float(request.args.get('epsilon'))

    global alpha
    alpha = float(request.args.get('alpha'))

    global gamma
    gamma = float(request.args.get('gamma'))

    # Parse level
    global level
    level = learn.parse_level(map, head, tail, food)

    # Init Q-table
    global q_table
    q_table = learn.init_q_table()
    
    # Set current state
    global state
    state = learn.get_state(level)
    print("state", state)

    # Choose action
    global action
    action = learn.choose_action(state, q_table, epsilon)

    global steps
    steps += 1

    # Perform search algorithm logic here with map_name and algorithm_name
    # For demonstration purposes, just returning a simple response
    response = jsonify({'result': 'success', 'action': action})
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

@app.route('/get_qtable', methods=['GET'])
def get_qtable():
    try:
        response = jsonify({'result': 'success', 'q_table': q_table})
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response

    except Exception as e:
        return jsonify({'result': 'error', 'error_details': str(e)}), 500

@app.route('/save_results', methods=['GET'])
def save_results():
    try:
        # Save Q-table to a json file
        with open('results/q_table.json', 'w') as file:
            file.write(str(q_table))

        # Get experiement restuls   
        results = json.loads(request.args.get('results'))
        
        # Save experiment results to csv file
        with open('results/experiment_results.csv', 'w') as file:
            for experiment in results:
                file.write(','.join([str(x) for x in experiment]) + '\n')

        response = jsonify({'result': 'success'})
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response

    except Exception as e:
        return jsonify({'result': 'error', 'error_details': str(e)}), 500

@socketio.on('message_from_client')
def handle_message(data):
    msg_type = data['type']
    if msg_type == 'q_update':
       q_update(data)
    elif msg_type == 'q_experiment':
       q_experiment(data)

def q_update(data):
    global epsilon
    epsilon = float(data['epsilon'])

    global alpha
    alpha = float(data['alpha'])

    global gamma
    gamma = float(data['gamma'])

    # Get map
    map = data['map']
    head = data['head']
    tail = data['tail']
    food = data['food']

    # Parse level
    level_prime = learn.parse_level(map, head, tail, food)

    # Get state
    state_prime = learn.get_state(level_prime)

    # Reward function
    global level
    reward = learn.reward_function(level, level_prime)
    
    # Update Q-table 
    global state
    global action
    print("[UPDATE]:", state, action, reward, state_prime, epsilon, alpha, gamma)
    learn.update_q_table(state, action, reward, state_prime, q_table, alpha, gamma)
    
    # Choose action
    state = state_prime
    level = level_prime
    
    action = learn.choose_action(state, q_table, epsilon)
    emit('message_from_server', {"type": "action", "action": action})

def q_experiment(data):
    # Get map
    map = data['map']
    head = data['head']
    tail = data['tail']
    food = data['food']

    # Parse level
    level_experiment = learn.parse_level(map, head, tail, food)

    # Get state
    state_experiment = learn.get_state(level_experiment)

    # Get action
    action = learn.choose_action(state_experiment, q_table, epsilon=0)

    print("[EXPERIMENT]:", state_experiment, action)

    emit('message_from_server', {"type": "action", "action": action})

if __name__ == '__main__':
    # Use the SSL context for HTTPS
    socketio.run(app, host="0.0.0.0", port="5001", debug=True)
