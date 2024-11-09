import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.get_data import get_turing

tm = get_turing('config/turing_machine.json') 
tm.display()
# render_turing_machine_graph(tm) 

# Test cases
test_inputs = [
    "111" # Expected
    ,"", #loop
    "10" # reject
    ]  

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
    tm.save_configurations("tests/test_w_"+w+"configurations.txt") 