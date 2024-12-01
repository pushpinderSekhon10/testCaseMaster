from openai import OpenAI
from dotenv import load_dotenv
import os, io, sys, pytest
import re
import importlib
import dynamic_test

load_dotenv()

def prompt():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    method_code = """
    ```python
    # Code of the method (and class if needed)
    def calculate_discount(price, discount_rate):
        if discount_rate < 0 or discount_rate > 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        return price * (1 - discount_rate)
    ```"""


    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant. Expected output format: (val1_value, val2_value). Provide only the output in the specified format. Do not add any additional text or explanation."},
            {
                "role": "user",
                "content": f"""Generate parameter input values for the following Python method to be used for unit testing. The values are to be used in tests that should cover typical use cases, edge cases, and error conditions.
                                {method_code}"""
            }
        ]
    )

    print(completion.choices[0].message)

    # parse output
    # Regular expression to match values inside parentheses
    matches = re.findall(r'\((.*?)\)', completion.choices[0].message.content)

    # Convert each match (a string) into a tuple of values
    result = [tuple(map(eval, match.split(','))) for match in matches]

    print(result)

#


def is_primitive(type_name):
    return type_name in ["int", "float", "str", "bool", "char"]

def process_json(data):
    for entry in data:
        if entry["category"] == "function":
            print(f"Processing function: {entry['title']}")
            create_object_from_params(entry["parameters"])

        elif entry["category"] == "class":
            print(f"Processing class: {entry['title']}")
            for method in entry.get("methods", []):
                create_object_from_params(method["parameters"])
            
            for inner_class in entry.get("inner_classes", []):
                print(f"Processing inner class: {inner_class['title']}")
                for method in inner_class.get("methods", []):
                    create_object_from_params(method["parameters"])


# Recursive function to create objects based on parameter types
def create_object_from_params(parameters, parent_class=None):
    created_objects = []
    for param in parameters:
        param_name = param["name"]
        param_type = param["type"]

        if not is_primitive(param_type):
            # Look for the class in the structure and instantiate it
            if param_type == "Calculator":
                created_objects.append(Calculator())
            elif param_type == "ScientificCalculator":
                created_objects.append(ScientificCalculator())
            else:
                print(f"Unknown class type: {param_type}")
        else:
            print(f"Primitive type detected for parameter {param_name}: {param_type}")

    return created_objects


def find_method(mod_name, class_name, method_name):
        mod = importlib.import_module(mod_name)
        if class_name:
            class_obj = getattr(mod, class_name)
            #get the method from the class
            method = getattr(class_obj, method_name)
            return method, class_obj
        else:
            #get the function from the module
            method = getattr(mod, method_name)
            return method, None

def run_method(method, class_obj, *args):
    if class_obj:
        return method(class_obj, *args)
    else:
        return method(*args)

def run_func(mod_name, class_name, method_name, *args):
        # Expected return value of type Any
        method, class_obj = find_method(mod_name, class_name, method_name)
        return run_method(method, class_obj, *args)

#hardcoded tests
def run_tests():
    # Capture the output of pytest
    buffer = io.StringIO()
    # Redirect stdout to the buffer
    sys.stdout = buffer
    
    # Run pytest
    exit = pytest.main(['dynamic_test.py', '-v'])
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # Get the test results from the buffer
    test_output = buffer.getvalue()
    return test_output, exit
