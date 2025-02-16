import tabulate
import os
from ply import yacc
from lexxer import tokens
from lexxer import lexer

def set_error_message(expected_type: str, problem_token):
    global error_message
    type_formats: dict[str, str] = {
        'txt': 'text(txt)',
        'num': 'number(num)'
    }
    expected_type = type_formats.get(expected_type, expected_type)
    error_message = f"Semantic Error: {problem_token} isn't a {expected_type} value"

# GRAMMAR RULES
def p_assignment_ex(p):
    '''assignment_expression : text_assignment
        | date_assignment
        | number_assignment
        | cardinal_assignment'''
    
    p[0] = p[1]
    
def p_error(p):
    global errors
    errors += 1
    
def p_text_assignment(p):
    'text_assignment : TYPE ID ASSIGN_OP TEXT'
    if p[1] != 'txt':
        set_error_message(p[1], p[4])
        #raise TypeError
    
def p_date_assignment(p):
    'date_assignment : TYPE ID ASSIGN_OP DATE'
    if p[1] != 'date':
        set_error_message(p[1], p[4])
        #raise TypeError
        
def p_number_assignment(p):
    'number_assignment : TYPE ID ASSIGN_OP NUMBER'
    if p[1] != 'num':
        set_error_message(p[1], p[4])
        #raise TypeError
        
def p_cardinal_assignment(p):
    'cardinal_assignment : TYPE ID ASSIGN_OP CARDINAL'
    if p[1] != 'cardinal':
        set_error_message(p[1], p[4])
        #raise TypeError
    
# Build the parser
parser: yacc = yacc.yacc(debug=True)

while True:
    errors: int = 0
    error_message: str = "No semantic errors"
    os.system('cls')
    
    print("Write an expression: ")
    expression = input()
    parser.parse(expression)
    result = "Valid syntactic expression\n" if errors == 0 else "Invalid syntactic expression\n"
    lexer.input(expression)
    token_data = []
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        token_data.append({"Type": tok.type, "Value":tok.value})

    print(tabulate.tabulate(token_data, headers="keys", tablefmt="grid"))
    print(result + error_message)
    
    input("Enter to continue...")