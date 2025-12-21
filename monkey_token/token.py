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
EQ = "=="
NOT_EQ = "!="

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
TRUE = "TRUE"
FALSE = "FALSE"
IF = "IF"
ELSE = "ELSE"
RETURN = "RETURN"

keywords = {
    "fn": FUNCTION,
    "let": LET,
    "true": TRUE,
    "false": FALSE,
    "if": IF,
    "else": ELSE,
    "return": RETURN,
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

