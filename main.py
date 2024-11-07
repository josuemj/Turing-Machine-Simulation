import json
from src.turing_machine import TuringMachine
from config.get_data import get_turing  # Assuming your function is in `src/get_data.py`

# Load Turing machine configuration from JSON file
tm = get_turing('config/turing_machine.json')  # Provide the path to your JSON file
tm.display()

# Test cases
test_inputs = ["111", "", "10"]  # Expected: Accept, Loop, Reject
for w in test_inputs:
    print(f"Input: {w}")
    tm.load_input(w)
    result = tm.run()
    if result:
        print("Result: Accepted")
    elif tm.current_state == tm.q_reject:
        print("Result: Rejected")
    else:
        print("Result: Infinite loop detected")
    print("Tape Contents:", tm.get_tape_contents())
    print()
