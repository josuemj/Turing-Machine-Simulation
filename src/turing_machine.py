class TuringMachine:
    def __init__(self, Q, Sigma, Gamma, delta, q0, q_accept, q_reject):
        """
        Initializes a Turing Machine.
        
        Parameters:
        Q (set): Set of states
        Sigma (set): Input alphabet (does not contain the blank symbol)
        Gamma (set): Tape alphabet (includes the blank symbol)
        delta (dict): Transition function in the form { (state, tape_symbol): (new_state, new_symbol, direction) }
        q0: Initial state
        q_accept: Accept state
        q_reject: Reject state
        """
        self.Q = Q
        self.Sigma = Sigma
        self.Gamma = Gamma
        self.delta = delta
        self.q0 = q0
        self.q_accept = q_accept
        self.q_reject = q_reject
        self.reset()