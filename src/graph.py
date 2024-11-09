from streamlit_agraph import Node, Edge, Config, agraph

class Graph:
    def __init__(self, turing_machine_json):
        self.nodes = []
        self.edges = []
        self.tm_json = turing_machine_json  # Store JSON directly
        self.config = None
    
    def build(self):
        # Add nodes for each state in Q
        for state in self.tm_json["Q"]:
            shape = "ellipse"
            color = "lightgreen" if state == self.tm_json["q_accept"] else "red" if state == self.tm_json["q_reject"] else "lightblue"
            self.nodes.append(Node(id=state, label=state, color=color, shape=shape))

        # Add edges for each transition in delta
        for current_state, transitions in self.tm_json["delta"].items():
            for symbol, action in transitions.items():
                next_state, write_symbol, direction = action
                label = f"{symbol} → {write_symbol}, {direction}"
                self.edges.append(Edge(source=current_state, target=next_state, label=label))

        # Configure the graph display
        self.config = Config(
            width=750,
            height=750,
            directed=True,
            physics=True,
            hierarchical=False
        )
        
        return self
