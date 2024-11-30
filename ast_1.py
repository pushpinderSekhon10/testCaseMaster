#Parse target python file code into an Abstract Syntax Tree

import ast
def parse_source_file(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()
    return ast.parse(source_code)

