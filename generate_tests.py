import ast
import os
import json

# Code to infer the return types for JSON since not explicitly mentioned
def infer_return_value(node):
    """Checks whether a function has a return value or not."""
    if isinstance(node, ast.FunctionDef):
        for n in node.body:
            if isinstance(n, ast.Return):
                return 'True'  # Return 'True' as soon as a return statement is found
    return 'False' 

def parse_source_file(file_path):
    """Parse the target Python file into an Abstract Syntax Tree."""
    with open(file_path, 'r') as file:
        source_code = file.read()
    return ast.parse(source_code)

# Function to parse the AST into a JSON file
def parse_ast_to_json(file_path):
    """Parse the AST of a Python file and convert it to a JSON-friendly structure."""
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())

    result = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_info = {
                "title": node.name,
                "attributes": [],  # Can be extended if class attributes are needed
                "methods": []
            }

            for class_body in node.body:
                if isinstance(class_body, ast.FunctionDef):
                    method_info = {
                        "title": class_body.name,
                        "parameters": [arg.arg for arg in class_body.args.args[1:]],  # Skip 'self'
                        "return_type": infer_return_value(class_body)  # Infer return type
                    }
                    class_info["methods"].append(method_info)

            result.append(class_info)

        elif isinstance(node, ast.FunctionDef):
            function_info = {
                "title": node.name,
                "parameters": [arg.arg for arg in node.args.args],
                "return_type": infer_return_value(node)  # Infer return type
            }
            result.append(function_info)

    return result

# Function to save the parsed file into a JSON
def save_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

class CodeAnalyzer(ast.NodeVisitor):
    """Traverse the AST to extract functions and classes."""
    def __init__(self):
        self.functions = []
        self.classes = []

    def visit_FunctionDef(self, node):
        """Collect function definitions."""
        function_info = {
            'name': node.name,
            'params': [arg.arg for arg in node.args.args],  # Parameter names
            'returns': ast.unparse(node.returns) if node.returns else None  # Return type
        }
        self.functions.append(function_info)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Collect class definitions."""
        class_info = {
            'name': node.name,
            'methods': []
        }
        # Extract methods from the class
        for child in node.body:
            if isinstance(child, ast.FunctionDef):
                method_info = {
                    'name': child.name,
                    'params': [arg.arg for arg in child.args.args if arg.arg != 'self'],
                    'returns': ast.unparse(child.returns) if child.returns else None
                }
                class_info['methods'].append(method_info)
        self.classes.append(class_info)
        self.generic_visit(node)

def generate_test_code(analyzer, module_name):
    test_methods = []

    # Generate test methods for standalone functions
    for func in analyzer.functions:
        params = ", ".join(f"{param}=None" for param in func['params'])
        return_comment = f"# Expected return value of type {func['returns']}" if func['returns'] else "# Expected return value"
        test_method = f'''
    def test_{func['name']}(self):
        # TODO: Implement test for {func['name']}
        {return_comment}
        result = {module_name}.{func['name']}({params})
        self.assertEqual(result, None)  # Replace None with the expected result
'''
        test_methods.append(test_method)

    # Generate test methods for methods inside classes
    for class_node in analyzer.classes:
        for method in class_node['methods']:
            params = ", ".join(f"{param}=None" for param in method['params'])
            return_comment = f"# Expected return value of type {method['returns']}" if method['returns'] else "# Expected return value"
            test_method = f'''
    def test_{class_node['name']}_{method['name']}(self):
        # TODO: Implement test for {class_node['name']}.{method['name']}
        {return_comment}
        obj = {module_name}.{class_node['name']}()  # Create an instance of the class
        result = obj.{method['name']}({params})
        self.assertEqual(result, None)  # Replace None with the expected result
'''
            test_methods.append(test_method)

    # Combine test methods into a test class
    test_class = f'''import unittest
import {module_name}

class Test{module_name.capitalize()}(unittest.TestCase):{''.join(test_methods)}

if __name__ == "__main__":
    unittest.main()
'''
    return test_class

# Writing the test file to a specified file path
def write_test_file(test_code, test_file_path):
    """Writes the generated test code to a specified file."""
    with open(test_file_path, 'w') as file:
        file.write(test_code)

def process_file(target_file):
    """Processes a single file to generate test code and JSON structure."""
    module_name = os.path.splitext(os.path.basename(target_file))[0]

    # Step 1: Parse the source file and generate test code
    tree = parse_source_file(target_file)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    test_code = generate_test_code(analyzer, module_name)

    # Step 2: Write the test file
    test_file_name = f'test_{module_name}.py'
    write_test_file(test_code, test_file_name)
    print(f"Generated test file: {test_file_name}")

    # Step 3: Parse the original source file into JSON
    json_structure = parse_ast_to_json(target_file)

    # Step 4: Save the JSON structure to a file
    json_output_path = f"{module_name}_ast.json"
    save_json(json_structure, json_output_path)
    print(f"JSON structure saved to {json_output_path}")

def main(target_directory):
    """Processes all .py files in the target directory."""
    if not os.path.isdir(target_directory):
        print(f"The provided path '{target_directory}' is not a directory.")
        return

    # List all files in the directory
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        if os.path.isfile(file_path) and filename.endswith('.py'):
            print(f"Processing file: {file_path}")
            process_file(file_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_tests.py <target_directory>")
        sys.exit(1)
    target_directory = sys.argv[1]
    main(target_directory)
