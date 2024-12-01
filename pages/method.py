import streamlit as st
import pandas as pd
from streamlit_agraph.config import Config, ConfigBuilder
from streamlit_agraph import agraph, Node, Edge, Config
import sys
import io, pytest
import dynamic_test, os
from gpt import run_tests
from test_cases import test_cases

#os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

st.title(f"Test {st.session_state['selected_node']}")

# Back button
if st.button("Go Back"):

    st.switch_page('app.py')

with st.form("test_options"):
   st.write("Test Configuration")
   input_num = st.slider('How many cases to run:', 1, 20)
   case_cat = st.selectbox('Case Category', ['General Case','Edge Case','Error Handling'])
   st.markdown("Select the case category to determine what inputs to generate")
   submit = st.form_submit_button('Launch Input')

if submit:
    #get test cases from gpt here
    cases_input1 = [
        {
        'mod_name': 'calculator',
        'class_name': 'Calculator',
        'method_name': 'multiply',
        'args': (3, 2),
        'expected': 6
        },
        {
        'mod_name': 'calculator',
        'class_name': 'Calculator',
        'method_name': 'multiply',
        'args': (4, 8),
        'expected': 32
        },
        {
        'mod_name': 'calculator',
        'class_name': 'Calculator',
        'method_name': 'multiply',
        'args': (1, 0),
        'expected': 0
        },
        {
        'mod_name': 'calculator',
        'class_name': 'Calculator',
        'method_name': 'multiply',
        'args': (5, 1),
        'expected': 5
        },
    ]

    cases_input2 = [
        {
        'mod_name': 'calculator',
        'class_name': 'Calculator',
        'method_name': 'add',
        'args': (3, 2),
        'expected': 1
    }
    ]
    if st.session_state['selected_node'] == 'multiply':
        test_cases = cases_input1
    elif st.session_state['selected_node'] == 'add':
        test_cases = cases_input2
    test_results, exit = run_tests()
    st.text_area("Test Results", test_results, height=400)
    if exit == 0:
        #all tests passed
        st.session_state['node_color'] = "#6aa84f"
        st.session_state['return'] = "true"
    elif exit == 1:
        st.session_state['node_color'] = "#cc0000"
        st.session_state['return'] = "true"
