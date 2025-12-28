from enum import Enum

class TokenType(str, Enum):
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

    def lookup_identifer(ident: str) -> str:
        """
        ident (str): indentifer string extracted from input.

        To verify in the input string is a reserved-keyword or a variable-name
        """
        return RESERVED_KEYWORDS.get(ident, TokenType.IDENT)

RESERVED_KEYWORDS = {
    "fn"    : TokenType.FUNCTION,
    "let"   : TokenType.LET,
    "true"  : TokenType.TRUE,
    "false" : TokenType.FALSE,
    "if"    : TokenType.IF,
    "else"  : TokenType.ELSE,
    "return": TokenType.RETURN,
}


class Token:
    """Each character of input program is converted to a token."""
    def __init__(self, Type: str, Literal: str):
        self.Type = Type
        self.Literal = Literal

