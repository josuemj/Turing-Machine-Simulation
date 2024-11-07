from src.turing_machine import TuringMachine

Q = {'q0', 'q1', 'q_loop', 'q_accept', 'q_reject'}
Sigma = {'1'}
Gamma = {'1', '⊔'}
delta = {
    # State q0
    ('q0', '1'): ('q1', '1', 'R'),          # Move to q1 if reading '1'
    ('q0', '⊔'): ('q_loop', '⊔', 'S'),      # Loop indefinitely if reading blank
    ('q0', '0'): ('q_reject', '0', 'S'),    # Reject if any other character
    
    # State q1
    ('q1', '1'): ('q1', '1', 'R'),          # Stay in q1 if reading '1'
    ('q1', '⊔'): ('q_accept', '⊔', 'S'),    # Accept if end of input (blank symbol)
    
    # State q_loop (infinite loop)
    ('q_loop', '⊔'): ('q_loop', '⊔', 'S'),  # Stay in q_loop indefinitely
}
q0 = 'q0'
q_accept = 'q_accept'
q_reject = 'q_reject'

# Initialize the Turing machine
tm = TuringMachine(Q, Sigma, Gamma, delta, q0, q_accept, q_reject)

# Test cases
test_inputs = ["111", "", "10"]  # Expected: Accept, Loop, Reject
for w in test_inputs:
    print(f"Input: {w}")
    tm.load_input(w)
    result = tm.run()
    if result:
        print("Result: Accepted")
    elif tm.current_state == q_reject:
        print("Result: Rejected")
    else:
        print("Result: Infinite loop detected")
    print("Tape Contents:", tm.get_tape_contents())
    print()
