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
        self.functions.append(node)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        """Collect class definitions."""
        self.classes.append(node)
        self.generic_visit(node)

def generate_test_code(analyzer, module_name):
    """Generate test code for the extracted functions and classes."""
    test_methods = []

    for func in analyzer.functions:
        test_method = f'''
    def test_{func.name}(self):
        # TODO: Implement test for {func.name}
        self.assertTrue(False)
'''
        test_methods.append(test_method)

    for class_node in analyzer.classes:
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef):
                test_method = f'''
    def test_{class_node.name}_{node.name}(self):
        # TODO: Implement test for {class_node.name}.{node.name}
        self.assertTrue(False)
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
