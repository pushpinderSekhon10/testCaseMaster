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
        'class_name': None,
        'method_name': 'add',
        'args': (3, 2),
        'expected': 1
    }
    ]
    if st.session_state['selected_node'] == 'multiply':
        test_cases = cases_input1
        test_results = '''
        ============================================================== test session starts =============================================================== platform darwin -- Python 3.11.7, pytest-8.3.3, pluggy-1.5.0 -- /Users/hanigherwi/Desktop/HW2024/testCaseMaster/venv/bin/python3.11 cachedir: .pytest_cache rootdir: /Users/hanigherwi/Desktop/HW2024/testCaseMaster plugins: anyio-4.6.2.post1 collecting ... collected 4 items dynamic_test.py::test_dynamic_methods[test_case0] FAILED                                                                                   [ 25%] dynamic_test.py::test_dynamic_methods[test_case1] FAILED                                                                                   [ 50%] dynamic_test.py::test_dynamic_methods[test_case2] FAILED                                                                                   [ 75%] dynamic_test.py::test_dynamic_methods[test_case3] FAILED                                                                                   [100%] ==================================================================== FAILURES ==================================================================== ________________________________________________________ test_dynamic_methods[test_case0] ________________________________________________________ test_case = {'args': (3, 2), 'class_name': 'Calculator', 'expected': 6, 'method_name': 'multiply', ...} @pytest.mark.parametrize("test_case", test_cases) def test_dynamic_methods(test_case): mod_name = test_case['mod_name'] class_name = test_case['class_name'] method_name = test_case['method_name'] args = test_case['args'] expected = test_case['expected'] >       result = run_func(mod_name, class_name, method_name, *args) dynamic_test.py:54: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ gpt.py:111: in run_func return run_method(method, class_obj, *args) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ method = <function Calculator.multiply at 0x118bf7060>, class_obj = <class 'calculator.Calculator'>, args = (3, 2) def run_method(method, class_obj, *args): if class_obj: >           return method(class_obj, *args) E           TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given gpt.py:104: TypeError ________________________________________________________ test_dynamic_methods[test_case1] ________________________________________________________ test_case = {'args': (4, 8), 'class_name': 'Calculator', 'expected': 32, 'method_name': 'multiply', ...} @pytest.mark.parametrize("test_case", test_cases) def test_dynamic_methods(test_case): mod_name = test_case['mod_name'] class_name = test_case['class_name'] method_name = test_case['method_name'] args = test_case['args'] expected = test_case['expected'] >       result = run_func(mod_name, class_name, method_name, *args) dynamic_test.py:54: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ gpt.py:111: in run_func return run_method(method, class_obj, *args) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ method = <function Calculator.multiply at 0x118bf7060>, class_obj = <class 'calculator.Calculator'>, args = (4, 8) def run_method(method, class_obj, *args): if class_obj: >           return method(class_obj, *args) E           TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given gpt.py:104: TypeError ________________________________________________________ test_dynamic_methods[test_case2] ________________________________________________________ test_case = {'args': (1, 0), 'class_name': 'Calculator', 'expected': 0, 'method_name': 'multiply', ...} @pytest.mark.parametrize("test_case", test_cases) def test_dynamic_methods(test_case): mod_name = test_case['mod_name'] class_name = test_case['class_name'] method_name = test_case['method_name'] args = test_case['args'] expected = test_case['expected'] >       result = run_func(mod_name, class_name, method_name, *args) dynamic_test.py:54: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ gpt.py:111: in run_func return run_method(method, class_obj, *args) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ method = <function Calculator.multiply at 0x118bf7060>, class_obj = <class 'calculator.Calculator'>, args = (1, 0) def run_method(method, class_obj, *args): if class_obj: >           return method(class_obj, *args) E           TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given gpt.py:104: TypeError ________________________________________________________ test_dynamic_methods[test_case3] ________________________________________________________ test_case = {'args': (5, 1), 'class_name': 'Calculator', 'expected': 5, 'method_name': 'multiply', ...} @pytest.mark.parametrize("test_case", test_cases) def test_dynamic_methods(test_case): mod_name = test_case['mod_name'] class_name = test_case['class_name'] method_name = test_case['method_name'] args = test_case['args'] expected = test_case['expected'] >       result = run_func(mod_name, class_name, method_name, *args) dynamic_test.py:54: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ gpt.py:111: in run_func return run_method(method, class_obj, *args) _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ method = <function Calculator.multiply at 0x118bf7060>, class_obj = <class 'calculator.Calculator'>, args = (5, 1) def run_method(method, class_obj, *args): if class_obj: >           return method(class_obj, *args) E           TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given gpt.py:104: TypeError ================================================================ warnings summary ================================================================ venv/lib/python3.11/site-packages/_pytest/config/__init__.py:1277 /Users/hanigherwi/Desktop/HW2024/testCaseMaster/venv/lib/python3.11/site-packages/_pytest/config/__init__.py:1277: PytestAssertRewriteWarning: Module already imported so cannot be rewritten: anyio self._mark_plugins_for_rewrite(hook) -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html ============================================================ short test summary info ============================================================= FAILED dynamic_test.py::test_dynamic_methods[test_case0] - TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given FAILED dynamic_test.py::test_dynamic_methods[test_case1] - TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given FAILED dynamic_test.py::test_dynamic_methods[test_case2] - TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given FAILED dynamic_test.py::test_dynamic_methods[test_case3] - TypeError: Calculator.multiply() takes 2 positional arguments but 3 were given ========================================================== 4 failed, 1 warning in 0.04s =========================================================='''
        st.text_area("Test Results", test_results, height=400)
        exit = 1
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
