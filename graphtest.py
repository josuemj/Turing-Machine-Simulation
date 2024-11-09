import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Define the Turing machine (states, transitions, accept/reject states)
class TuringMachine:
    def __init__(self, Q, Sigma, Gamma, delta, q0, q_accept, q_reject):
        self.Q = Q  # States
        self.Sigma = Sigma  # Input symbols
        self.Gamma = Gamma  # Tape symbols
        self.delta = delta  # Transition function
        self.q0 = q0  # Initial state
        self.q_accept = q_accept  # Accept state
        self.q_reject = q_reject  # Reject state

# Example Turing Machine configuration
tm = TuringMachine(
    Q=["q0", "q1", "q_loop", "q_accept", "q_reject"],
    Sigma=["1"],
    Gamma=["1", "0", "B"],
    delta={
        ("q0", "1"): ("q1", "1", "R"),
        ("q0", "B"): ("q_loop", "B", "S"),
        ("q0", "0"): ("q_reject", "0", "S"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "B"): ("q_accept", "B", "S"),
        ("q1", "0"): ("q_reject", "0", "S"),
        ("q_loop", "B"): ("q_loop", "B", "S"),
        ("q_reject", "0"): ("q_reject", "0", "S"),
        ("q_reject", "1"): ("q_reject", "1", "S"),
        ("q_reject", "B"): ("q_reject", "B", "S"),
        ("q_accept", "B"): ("q_accept", "B", "S"),
    },
    q0="q0",
    q_accept="q_accept",
    q_reject="q_reject"
)

# Convert the Turing machine to nodes and edges for streamlit-agraph
nodes = []
edges = []

# Add nodes for each state
for state in tm.Q:
    shape = "ellipse"
    color = "lightgreen" if state == tm.q_accept else "red" if state == tm.q_reject else "lightblue"
    nodes.append(Node(id=state, label=state, color=color, shape=shape))

# Add edges for each transition in delta
for (current_state, symbol), (next_state, write_symbol, direction) in tm.delta.items():
    label = f"{symbol} → {write_symbol}, {direction}"
    edges.append(Edge(source=current_state, target=next_state, label=label))

# Configure the graph display
config = Config(width=750,
                height=750,
                directed=True,
                physics=True,
                hierarchical=False)

# Display the graph in Streamlit
st.title("Turing Machine Graph")
agraph(nodes=nodes, edges=edges, config=config)
