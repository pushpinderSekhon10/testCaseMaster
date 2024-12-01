import pytest
from gpt import run_func
#from test_cases import test_cases


test_cases0 = [
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

test_cases = [
        {
        'mod_name': 'calculator',
        'class_name': None,
        'method_name': 'add',
        'args': (3, 2),
        'expected': 5
        }
    ]

@pytest.mark.parametrize("test_case", test_cases)
def test_dynamic_methods(test_case):
    mod_name = test_case['mod_name']
    class_name = test_case['class_name']
    method_name = test_case['method_name']
    args = test_case['args']
    expected = test_case['expected']
    result = run_func(mod_name, class_name, method_name, *args)
    assert result == expected
