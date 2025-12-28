from monkey_token.token import TokenType, Token

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

    def next_token(self) -> Token:
        tok = None

        self.skip_whitespace()

        match self.ch:
            case '=':
                if self.peek_char() == "=":
                    ch = self.ch
                    self.read_char()
                    tok = Token(TokenType.EQ, ch+self.ch) # ==
                else:
                    tok = Token(TokenType.ASSIGN, self.ch)
            case '+':
                tok = Token(TokenType.PLUS, self.ch)
            case '-':
                tok = Token(TokenType.MINUS, self.ch)
            case '!':
                if self.peek_char() == "=":
                    ch = self.ch
                    self.read_char()
                    tok = Token(TokenType.NOT_EQ, ch+self.ch) # !=
                else:
                    tok = Token(TokenType.BANG, self.ch)
            case '/':
                tok = Token(TokenType.SLASH, self.ch)
            case '*':
                tok = Token(TokenType.ASTERISK, self.ch)
            case '<':
                tok = Token(TokenType.LT, self.ch)
            case '>':
                tok = Token(TokenType.GT, self.ch)
            case ';':
                tok = Token(TokenType.SEMICOLON, self.ch)
            case ',':
                tok = Token(TokenType.COMMA, self.ch)
            case ';':
                tok = Token(TokenType.SEMICOLON, self.ch)
            case '(':
                tok = Token(TokenType.LPAREN, self.ch)
            case ')':
                tok = Token(TokenType.RPAREN, self.ch)
            case ',':
                tok = Token(TokenType.COMMA, self.ch)
            case '+':
                tok = Token(TokenType.PLUS, self.ch)
            case '{':
                tok = Token(TokenType.LBRACE, self.ch)
            case '}':
                tok = Token(TokenType.RBRACE, self.ch)
            case None:
                # EOF has no specific Literal(char/str)
                # denoted it - hence using "EOF"
                tok = Token(TokenType.EOF, "")
            case _:
                if is_letter(self.ch):
                    token_literal = self.read_identifier()
                    token_type = TokenType.lookup_identifer(token_literal)
                    tok = Token(token_type, token_literal)
                    return tok
                elif is_digit(self.ch):
                    token_type = TokenType.INT
                    token_literal = self.read_number()
                    tok = Token(token_type, token_literal)
                    return tok
                else:
                    tok = Token(TokenType.ILLEGAL, self.ch)
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

