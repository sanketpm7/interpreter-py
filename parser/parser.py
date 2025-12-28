from lexer.lexer import Lexer
from monkey_token.token import Token, TokenType
from monkey_ast.ast import Program, LetStatement, Identifier


class Parser:
    def __init__(self, lexer: Lexer):
        self.l = lexer

        self.cur_token: Token|None = None
        self.peek_token: Token|None = None

        # Read two token so that cur_token & peek_token are both set
        self.next_token()
        self.next_token()

    def next_token(self):
        self.cur_token = self.peek_token
        self.peek_token = self.l.next_token()

    def cur_token_is(self, token_type: TokenType) -> bool:
        return self.cur_token.Type == token_type

    def peek_token_is(self, token_type: TokenType) -> bool:
        return self.peek_token.Type == token_type

    def expect_peek(self, token_type: TokenType) -> bool:
        if not self.peek_token_is(token_type):
            return False

        self.next_token()
        return True

    def parse_let_statement(self) -> LetStatement:
        """
        This function is called iff `cur_token = <LET>`
        - we create a LetStatement with the  `< <identifer> EQUALS <expression> >`

        """
        stmt = LetStatement(self.cur_token, name=None, value=None)

        # 1. Expect next token to be 'identifer'
        if not self.expect_peek(TokenType.IDENT):
            # raise exception instead of logging
            print(f"Invalid 'identifier' after 'let', got={self.cur_token.Type,self.cur_token.Literal}")
            return None

        stmt.name = Identifier(
            token=self.cur_token,
            value=self.cur_token.Literal
        )

        # 2. Expect next token to be '='(<EQUALS,'='>)
        if not self.expect_peek(TokenType.ASSIGN):
            return None

        # skip expression until semicolon
        while not self.cur_token_is(TokenType.SEMICOLON):
            self.next_token()

        stmt.log()

        return stmt

    def parse_statement(self):
        match self.cur_token.Type:
            case TokenType.LET:
                return self.parse_let_statement()
            case _:
                return None

    def Parse_Program(self) -> Program:
        """
        1. construct the root node of AST
        2. iterate over every token in the input until it encounters an token.EOF token

        Every Iteration:
            1. every iteration it calls parse_statement
            2. 
        """
        program = Program()
        while self.cur_token.Type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                program.statements.append(stmt)
            self.next_token()

        return program


def parse_program():
    program = new_program_ast_node()

    advance_tokens()

    while current_token() != EOF_TOKEN:
        statement = None

        if current_token() == LET_TOKEN:
            statement = parse_let_statement()
        elif current_token() == RETURN_TOKEN:
            statement = parse_return_statement()
        elif current_token() == IF_TOKEN:
            statement = parse_if_statement()

        if statement:
            program.statements.push(statement)

        advance_tokens()

    return program


def parse_identifier():
    identifier = new_identifier_ast_node()
    identifier.token = current_token()
    return identifier

def parse_expression():
    if currentToken() == INTEGER_TOKEN:
        if nextToken() == PLUS_TOKEN:
            return parse_operator_expression()
        elif nextToken() == SEMICOLON_TOKEN:
            return parse_integer_literal()
    elif (currentToken() == LEFT_PAREN):
        return parse_grouped_expression()

def parse_operator_expression():
    operator_expression = new_operator_expression()

    operator_expression.left = parse_integer_literal()
    operator_expression.operator = current_token()
    operator_expression.right = parse_expression()

    return operator_expression()


# FIXME: needs work

