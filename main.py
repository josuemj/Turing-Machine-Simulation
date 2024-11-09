import json
from src.turing_machine import TuringMachine
from config.get_data import get_turing, get_turing_json 
import streamlit as st
from streamlit_agraph import agraph
from src.graph import Graph
from src.render_turing import render_turing_machine_graph
    
st.title("Turing Machine simulation")
uploaded_file = st.file_uploader("Upload the turing machine JSON configuration", type="json")

if uploaded_file is not None:
    
    data = json.load(uploaded_file)
    st.subheader("Turing macghine configuration")
    st.json(data)  
    
    turing_machine = get_turing_json(data)

    st.title("Turing Machine Graph")
    turing_machine_graph = Graph(turing_machine_json=data).build()
    agraph(nodes=turing_machine_graph.nodes, edges=turing_machine_graph.edges, config=turing_machine_graph.config)
    
    if st.button("Graphviz"):
        if uploaded_file is not None:
            render_turing_machine_graph(turing_machine) 

#User input for turing machine simulation
input_string = st.text_input("Enter the input string for the Turing machine:", "")

if st.button("Run Simulation"):
    
    if uploaded_file is not None:

        turing_machine.display()
        
        #loading user input
        turing_machine.load_input(input_string)
        result = turing_machine.run()

        # Display the result
        if result:
            st.success("The input was accepted by the Turing machine.")
        elif turing_machine.current_state == turing_machine.q_reject:
            st.error("The input was rejected by the Turing machine.")
        else:
            st.error("Infinte Loop")
        
        # Show the configurations (trace) as long as there's data
        st.subheader("Simulation Trace (Configurations)")
        for config in turing_machine.configurations:
            st.text(config)
        
        # Save configurations to a text file
        turing_machine.save_configurations("output/w_"+input_string+"configurations.txt")  
    
    else:
        st.error("No configuration uploaded")
        
        
    
    

        





    
    
