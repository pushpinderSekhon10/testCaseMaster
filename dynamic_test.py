import pytest
from gpt import run_func
from test_cases import test_cases

@pytest.mark.parametrize("test_case", test_cases)
def test_dynamic_methods(test_case):
    mod_name = test_case['mod_name']
    class_name = test_case['class_name']
    method_name = test_case['method_name']
    args = test_case['args']
    expected = test_case['expected']
    result = run_func(mod_name, class_name, method_name, *args)
    assert result == expected
