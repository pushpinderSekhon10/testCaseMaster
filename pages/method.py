import streamlit as st
import pandas as pd
from streamlit_agraph.config import Config, ConfigBuilder
from streamlit_agraph import agraph, Node, Edge, Config
import json

st.title(f"Test {st.session_state['selected_node']}")


with st.form("test_options"):
   st.write("Test Configuration")
   input_num = st.slider('How many cases to run:', 1, 20)
   case_cat = st.selectbox('Case Category', ['General Case','Edge Case','Error Handling'])
   st.markdown("Select the case category to determine what inputs to generate")
   submit = st.form_submit_button('Launch Input')

# This is outside the form
st.write(input_num)
st.write(case_cat)

if submit:
    #run test cases with given config
    pass


# Back button
if st.button("Go Back"):
    st.session_state['selected_node'] = None
    st.switch_page('app.py')
