import pytest
from gpt import run_func
#from test_cases import test_cases


test_cases = [
    {
        'mod_name': 'samplecode',
        'class_name': 'Calculator',
        'method_name': 'multiply',
        'args': (3, 2),
        'expected': 6
    }
]
    # Add more test cases




@pytest.mark.parametrize("test_case", test_cases)
def test_dynamic_methods(test_case):
    mod_name = test_case['mod_name']
    class_name = test_case['class_name']
    method_name = test_case['method_name']
    args = test_case['args']
    print(f"ARGSSSS {args}")
    expected = test_case['expected']
    result = run_func(mod_name, class_name, method_name, *args)
    print(f"RESULT {result}")
    assert result == expected
