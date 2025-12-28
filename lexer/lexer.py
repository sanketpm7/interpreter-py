import monkey_token.token as token

class Lexer:
    def __init__(self, input: str):
        self.input = input
        self.position = -1       # current char
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
        while self.ch in [" ", "\t", "\n", "\r"]:
            self.read_char()

    def read_identifier(self) -> str:
        """let x"""
        start_position = self.position
        while is_letter(self.ch):
            self.read_char()
        return self.input[start_position:self.position]

    def read_number(self) -> str:
        start_position = self.position
        while is_digit(self.ch):
            self.read_char()
        return self.input[start_position: self.position]

    def peek_char(self) -> str:
        """ `peek` ahead in the input and not move around in it."""
        if self.readPosition >= len(self.input):
            return None
        return self.input[self.readPosition]

    def next_token(self) -> token.Token:
        tok = None

        self.skip_whitespace()

        match self.ch:
            case '=':
                if self.peek_char() == "=":
                    ch = self.ch
                    self.read_char()
                    tok = token.Token(token.EQ, ch+self.ch) # ==
                else:
                    tok = token.Token(token.ASSIGN, self.ch)
            case '+':
                tok = token.Token(token.PLUS, self.ch)
            case '-':
                tok = token.Token(token.MINUS, self.ch)
            case '!':
                if self.peek_char() == "=":
                    ch = self.ch
                    self.read_char()
                    tok = token.Token(token.NOT_EQ, ch+self.ch) # !=
                else:
                    tok = token.Token(token.BANG, self.ch)
            case '/':
                tok = token.Token(token.SLASH, self.ch)
            case '*':
                tok = token.Token(token.ASTERISK, self.ch)
            case '<':
                tok = token.Token(token.LT, self.ch)
            case '>':
                tok = token.Token(token.GT, self.ch)
            case ';':
                tok = token.Token(token.SEMICOLON, self.ch)
            case ',':
                tok = token.Token(token.COMMA, self.ch)
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
                # EOF has no specific Literal(char/str) to denote it - hence useing "" (empty string)
                tok = token.Token(token.EOF, "")
            case _:
                if is_letter(self.ch):
                    token_literal = self.read_identifier()
                    token_type = token.lookup_identifer(token_literal)
                    tok = token.Token(token_type, token_literal)
                    return tok
                elif is_digit(self.ch):
                    token_type = token.INT
                    token_literal = self.read_number()
                    tok = token.Token(token_type, token_literal)
                    return tok
                else:
                    tok = token.Token(token.ILLEGAL, self.ch)
        self.read_char()
        return tok


def is_letter(ch: str) -> bool:
    return (
        ch == "_"
        or (ord(ch) >=ord("a") and ord(ch) <= ord("z"))
        or (ord(ch) >=ord("A") and ord(ch) <= ord("Z"))
    )

def is_digit(ch: str) -> bool:
    return ord(ch) >= ord("0") and ord(ch) <= ord("9")

