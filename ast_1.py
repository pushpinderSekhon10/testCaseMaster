import ast
import os

def parse_source_file(file_path):
    """Parse the target Python file into an Abstract Syntax Tree."""
    with open(file_path, 'r') as file:
        source_code = file.read()
    return ast.parse(source_code)

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
                class_info['methods'].append(method_info)  # Append only when method_info is defined
        self.classes.append(class_info)  # Append the dictionary, not the node
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


# writing the test file to a specified file path
def write_test_file(test_code, test_file_path):
    """Writes the generated test code to a specified file."""
    with open(test_file_path, 'w') as file:
        file.write(test_code)

def main(target_file):
    """Orchestrates the analysis and test generation process."""
    module_name = os.path.splitext(os.path.basename(target_file))[0]
    tree = parse_source_file(target_file)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    test_code = generate_test_code(analyzer, module_name)
    test_file_name = f'test_{module_name}.py'
    write_test_file(test_code, test_file_name)
    print(f"Generated test file: {test_file_name}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_tests.py <target_python_file.py>")
        sys.exit(1)
    target_file = sys.argv[1]
    main(target_file)
