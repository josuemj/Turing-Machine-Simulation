class TuringMachine:
    def __init__(self, Q, Sigma, Gamma, delta, q0, q_accept, q_reject):
        """
        Initializes a Turing Machine.
        
        Parameters:
        Q (set): Set of states
        Sigma (set): Input alphabet (does not contain the blank symbol)
        Gamma (set): Tape alphabet (includes the blank symbol) in this case represented as B
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
        
        self.configurations = [] #save configurations
        self.reset()

    def reset(self):
        """Resets the machine to its initial configuration."""
        self.tape = []
        self.head_position = 0
        self.current_state = self.q0
        self.configuratios = []

    def load_input(self, w):
        """
        Loads the input string onto the tape and resets the head position.
        
        Parameters:
        w (str): The input word to be processed by the Turing machine.
        """
        self.tape = list(w) + ["B"]  # Add a blank symbol to the end of the tape
        self.head_position = 0
        self.current_state = self.q0
    
    def print_configuration(self):
        """Prints the current configuration of the Turing machine."""
        # u is the part of the tape to the left of the head, v starts from the head position
        u = ''.join(self.tape[:self.head_position])
        v = ''.join(self.tape[self.head_position:])
        print(f"Configuration: {u} {self.current_state} {v}")
        self.configurations.append(u+self.current_state+v)

    def step(self):
        """Performs a single step of the Turing machine."""
        self.print_configuration()  # Print configuration at each step
        
        if self.current_state == self.q_accept or self.current_state == self.q_reject:
            return  # Machine halts if it is in an accepting or rejecting state

        tape_symbol = self.tape[self.head_position]
        action = self.delta.get((self.current_state, tape_symbol))

        if action is None:
            self.current_state = self.q_reject  # Transition undefined; move to reject state
            return

        new_state, new_symbol, direction = action
        self.tape[self.head_position] = new_symbol  # Write new symbol to tape
        self.current_state = new_state  # Update the current state

        # Move the head left or right
        if direction == 'L':
            self.head_position = max(0, self.head_position - 1)  # Prevents moving left off the tape
        elif direction == 'R':
            self.head_position += 1
            if self.head_position >= len(self.tape):  # Extend tape if necessary
                self.tape.append("B")
        elif direction == 'S':  # Stay in place (used for infinite loop)
            pass

    def run(self):
        """Runs the Turing machine until it halts in either the accept or reject state or loops indefinitely."""
        step_count = 0  # Limit steps to avoid infinite loops in testing
        while self.current_state not in {self.q_accept, self.q_reject} and step_count < 1000:
            self.step()
            step_count += 1

        # Check if it stopped due to reaching the limit, indicating an infinite loop
        if step_count >= 1000:
            print("Infinite loop detected.")
            return False

        return self.current_state == self.q_accept

    def get_tape_contents(self):
        """Returns the current contents of the tape as a string."""
        return ''.join(self.tape).rstrip("B")  # Strip trailing blank symbols

    def display(self):
        print(f'\nQ ->  {self.Q}')
        print(f'Sigma -> {self.Sigma}')
        print(f'Gamma -> {self.Gamma}')
        
        print("\nDelta")
        for i in self.delta:
            print(i)
            
        print(f'\nInitial state (q0) -> {self.q0}')
        print(f'\nAccept state -> {self.q_accept}')

        print(f'\nReject state -> {self.q_reject}')
    
    def save_configurations(self, filename):
        """Saves the recorded configurations to a text file."""
        with open(filename, 'w') as file:
            for configuration in self.configurations:
                file.write(configuration + '\n')
        print(f"Configurations saved to {filename}")
