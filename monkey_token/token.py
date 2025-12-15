class Token:
    def __init__(self, Type: str="", Literal: str=""):
        self.Type = Type
        self.Literal = Literal

# Special types
ILLEGAL = "ILLEGAL"
EOF = "EOF"

# Identifiers + literals
IDENT = "IDENT" # add, foobar, x, y, ...
INT = "INT"     # 1343456

# Operators
ASSIGN = "="
PLUS = "+"

# Delimiters
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# Keywords
FUNCTION = "FUNCTION"
LET = "LET"


"""
TODOS:
1. use dataclass
2. 
"""
