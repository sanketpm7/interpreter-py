# Special types
"""
Tokens are the individual chars in the input

Every character or group of characters can belong to one of the
categories below

1. ILLEGAL
    - special symbols (!@#$%..) - monkey language does not allow these chars
2. EOF
    - denotes the end of file 
3. IDENT
    - identifiers variable names var_name, func_name, ..
4. INT          - 5/10/.

-- OPERATORS
5. ASSIGN       - =
6. PLUS         - +

-- DELIMITERS --
7. COMMA        - ,
8. SEMICOLON    - ;
9. LPAREN       - (
10. RPAREN      - )
11. LBRACE      - {
12. RBRACE      - }

-- KEYWORDS[RESERVED WORDS] --
13. FUNCTION
14. LET         - let
"""

ILLEGAL = "ILLEGAL"
EOF = "EOF"
IDENT = "IDENT"
INT = "INT"
ASSIGN = "="
PLUS = "+"
COMMA = ","
SEMICOLON = ";"
LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"
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

