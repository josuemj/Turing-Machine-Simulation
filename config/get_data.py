import json
from src.turing_machine import TuringMachine

def get_turing(filename: str):
    with open(filename, 'r') as f:
        tm_data = json.load(f)

    # Example of accessing components to initialize the TuringMachine class
    Q = set(tm_data['Q'])
    Sigma = set(tm_data['Sigma'])
    Gamma = set(tm_data['Gamma'])
    delta = { (state, symbol): tuple(transition) 
            for state, transitions in tm_data['delta'].items() 
            for symbol, transition in transitions.items() }
    q0 = tm_data['q0']
    q_accept = tm_data['q_accept']
    q_reject = tm_data['q_reject']

    # Now you can initialize your TuringMachine
    return TuringMachine(Q, Sigma, Gamma, delta, q0, q_accept, q_reject)

def get_turing_json(data):
    """
    Receives a JSON data from Streamlit with Turing machine configuration
    and initializes a TuringMachine instance.
    """
    Q = data['Q']
    Sigma = data['Sigma']
    Gamma = data['Gamma']
    
    # Parse delta correctly for the nested structure
    delta = {}
    for state, transitions in data['delta'].items():
        for symbol, action in transitions.items():
            # Each action is a list [next_state, write_symbol, direction]
            next_state, write_symbol, direction = action
            delta[(state, symbol)] = (next_state, write_symbol, direction)

    q0 = data['q0']
    q_accept = data['q_accept']
    q_reject = data['q_reject']
    
    # Return an instance of TuringMachine
    return TuringMachine(Q, Sigma, Gamma, delta, q0, q_accept, q_reject)
