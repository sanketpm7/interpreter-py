# Special types
ILLEGAL = "ILLEGAL"
EOF = "EOF"
IDENT = "IDENT"
INT = "INT"

# OPERATORS
ASSIGN = "="
PLUS = "+"
MINUS = "-"
BANG = "!"
ASTERISK = "*"
SLASH = "/"
LT = "<"
GT = ">"

# OPERATORS
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

# KEYWORDS 
FUNCTION = "FUNCTION"
LET = "LET"

keywords = {
    "fn": FUNCTION,
    "let": LET
}

def lookup_identifer(ident: str) -> str:
    """ident (str): indentifer string extracted from input."""
    if ident not in keywords:
        return IDENT
    return keywords[ident]

class Token:
    def __init__(self, Type: str="", Literal: str=""):
        self.Type = Type
        self.Literal = Literal

