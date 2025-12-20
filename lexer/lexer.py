import monkey_token.token as token

class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.position = 0       # current char
        self.readPosition = 0   # next char to process
        self.ch = ""
        self.read_char()

    def read_char(self):
        """give us the next character and advance our position in the input string."""
        if self.readPosition >= len(self.input): # EOF reached
            self.ch = None # using `None` instead `0` [used in golang]
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def skip_whitespace(self) -> None:
        if self.ch in [" ", "\t", "\n", "\r"]:
            self.read_char()

    def read_number(self) -> str:
        start_position = self.position
        while is_digit(self.ch):
            self.read_char()
        return self.input[start_position: self.position]

    def next_token(self) -> token.Token:
        tok = token.Token()
        
        self.skip_whitespace()

        match self.ch:
            case '=':
                tok = token.Token(token.ASSIGN, self.ch)
            case ';':
                tok = token.Token(token.SEMICOLON, self.ch)
            case '(':
                tok = token.Token(token.LPAREN, self.ch)
            case ')':
                tok = token.Token(token.RPAREN, self.ch)
            case ',':
                tok = token.Token(token.COMMA, self.ch)
            case '+':
                tok = token.Token(token.PLUS, self.ch)
            case '{':
                tok = token.Token(token.LBRACE, self.ch)
            case '}':
                tok = token.Token(token.RBRACE, self.ch)
            case None:
                tok.Literal = ""
                tok.Type = token.EOF
            case _:
                if is_letter(self.ch):
                    tok.Literal = self.read_identifier()
                    tok.Type = token.lookup_identifer(tok.Literal)
                    return tok
                elif is_digit(self.ch):
                    tok.Type = token.INT
                    tok.Literal = self.read_number()
                    return tok
                else:
                    tok = token.Token(token.ILLEGAL, self.ch)
        self.read_char()
        return tok

    def read_identifier(self) -> str:
        """let x"""
        start_position = self.position
        while is_letter(self.ch):
            self.read_char()
        return self.input[start_position:self.position]

def is_letter(ch: str) -> bool:
    return (
        ch == "_"
        or (ord(ch) >=ord("a") and ord(ch) <= ord("z"))
        or (ord(ch) >=ord("A") and ord(ch) <= ord("Z"))
    )

def is_digit(ch: str) -> bool:
    return ord(ch) >= ord("0") and ord(ch) <= ord("9")

