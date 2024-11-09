from graphviz import Digraph

def render_turing_machine_graph(tm):
    """
    Renders a graph for the given Turing machine object.

    Parameters:
    tm (object): A Turing machine object that has attributes for Q (states), 
    delta (transition function), q_accept (accept state), and q_reject (reject state).
    """
    # Initialize a directed graph
    dot = Digraph(comment='Turing Machine', format='png')
    
    # Add nodes for each state in Q
    for state in tm.Q:
        if state == tm.q_accept:
            dot.node(state, state, shape='doublecircle')  # Accept state
        elif state == tm.q_reject:
            dot.node(state, state, shape='doublecircle')  # Reject state
        else:
            dot.node(state, state, shape='circle')  # Regular state

    # Add edges for each transition in delta
    for (current_state, symbol), (next_state, write_symbol, direction) in tm.delta.items():
        label = f"{symbol} → {write_symbol}, {direction}"
        dot.edge(current_state, next_state, label=label)

    dot.render('turing_machine_graph', view=True)
    print("Graph saved as 'turing_machine_graph.png' and opened for viewing.")

