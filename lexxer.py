from ply import lex
import tabulate
import re

# TOKENS
types: dict[str, str] = {
    'txt': 'TEXT',
    'date': 'DATE',
    'num': 'NUMBER',
    'cardinal': 'CARDINAL'
}

other: list[str] = [
    'ID',
    'TYPE',
    'ASSIGN_OP'
]

tokens: list[str] = (
    other +
    list(types.values())
)

# SIMPLE REGEX RULES
t_TEXT = r'(\"[^\"\n\r]*\")'
t_DATE = r'(\d{1,2}(?P<separator>\/|-|\.)\d{1,2}(?P=separator)\d{4})'
t_NUMBER = r'([+-]?(?:(?:\d+)?\.?)\d+)'
t_CARDINAL = r'((?:north|south)(?:east|west)?|(?:east|west))'

t_ASSIGN_OP = r'='

t_ignore  = ' \t'
#t_LINE_BREAK = r'\n|\r'

# COMPLEX REGEX RULES
def t_ID(t):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    value: str = str(t.value)
    if types.__contains__(t.value):
        t.type = 'TYPE'
    elif re.fullmatch(t_CARDINAL, t.value):
        t.type = 'CARDINAL'
    return t

#Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
#== TESTS ==
lexer: lex.Lexer = lex.lex()
lexer.input('txt test = "lex testing"')
token_data = []
'''
'''
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    token_data.append({"Type": tok.type, "Value":tok.value})

print(tabulate.tabulate(token_data, headers="keys", tablefmt="grid"))