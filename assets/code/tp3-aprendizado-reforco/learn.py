import random
import itertools

WALL = 'X'

# Q-learning table and initial state
ACTIONS = ['w', 's', 'd', 'a']

def parse_level(map, head, tail, food):
    """ Parses a level from a string.

    Args:
        level_str: A string containing a level.

    Returns:
        The parsed level (dict) containing the locations of walls (set), the locations of spaces 
        (dict), and a mapping of locations to waypoints (dict).
    """
    head = tuple(head)
    food = tuple(food)
    spaces = set()
    walls = set()
    tail = set([tuple(t) for t in tail])

    for j, line in enumerate(map.split('\n')):
        for i, char in enumerate(line):
            if char == '\n':
                continue
            elif char == WALL:
                walls.add((i, j))
            elif char.isnumeric():
                spaces.add((i, j))  

    level = {'walls': walls, 'spaces': spaces, 'head': head, 'food': food, 'tail': tail}
    
    return level

def get_state(level):
    """
    Returns the current state of the game.

    Args:
        level: The current level.

    Returns:
        The current state of the game.
    """
    # ====================
    # SEU CÓDIGO AQUI
    # ====================

    return "000000"

def init_q_table():   
    """"
    Initializes the Q-table.

    Returns:
        The Q-table with zero for each possible state.
    """
    q_table = {}

    # ====================
    # SEU CÓDIGO AQUI
    # ====================
    
    return q_table

def update_q_table(s, a, r, s_prime, q_table, alpha, gamma):
    """
    Updates the Q-table.

    Args:
        s: The current state.
        a: The action taken.
        r: The reward received.
        s_prime: The next state.
        q_table: The Q-table.
        alpha: The learning rate.
        gamma: The discount factor.
    
    Returns:
        None
    """
    # ====================
    # SEU CÓDIGO AQUI
    # ====================

    pass

def choose_action(state, q_table, epsilon):
    """
    Chooses an action based on the current state.

    Args:
        state: The current state.
        q_table: The Q-table.
        epsilon: The epsilon value.
    
    Returns:
        The chosen action (see ACTIONS above).
    """
    # ====================
    # SEU CÓDIGO AQUI
    # ====================

    return random.choice(ACTIONS)

def reward_function(level, level_prime):  
    """
    Returns the reward.

    Args:
        level: The current level.
        level_prime: The next level.

    Returns:
        The reward.
    """
    # ====================
    # SEU CÓDIGO AQUI
    # ====================

    return 0


    