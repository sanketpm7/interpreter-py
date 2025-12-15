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
        if self.readPosition >= len(self.input):
            self.ch = None # using `None` instead `0` [used in golang]
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def next_token(self) -> token.Token:
        tok = token.Token()
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
        self.read_char()
        return tok


