import pytest
from lexer.lexer import Lexer
from monkey_token.token import TokenType


def test_next_token1():
    input_text = "=+(){},;"
    tests = [
        (TokenType.ASSIGN, "="),
        (TokenType.PLUS, "+"),
        (TokenType.LPAREN, "("),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RBRACE, "}"),
        (TokenType.COMMA, ","),
        (TokenType.SEMICOLON, ";"),
        (TokenType.EOF, ""),
    ]

    lex = Lexer(input_text)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()

        assert tok.Type == expected_type, \
                f"tests[{i}] - token type wrong. expected={expected_type}, got={tok.Type}"

        assert tok.Literal == expected_literal, \
                f"tests[{i}] - literal wrong. expected={expected_literal}, got={tok.Literal}"

def test_next_token2():
    input_text = "let x = 10;"
    tests = [
        (TokenType.LET, "let"),
        (TokenType.IDENT, "x"),
        (TokenType.ASSIGN, "="),
        (TokenType.INT, "10"),
        (TokenType.SEMICOLON, ";"),
    ]

    lex = Lexer(input_text)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()

        assert tok.Type == expected_type, \
                f"tests[{i}] - token type wrong. expected='{expected_type}', got='{tok.Type}'"

        assert tok.Literal == expected_literal, \
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{tok.Literal}'"

def test_next_token3():
    input = (
        """
        let five = 5;
        let ten = 10;
        let add = fn(x, y) {
            x + y;
        };
        let result = add(five, ten);
        """
    )

    tests = [
        (TokenType.LET, "let"),
        (TokenType.IDENT, "five"),
        (TokenType.ASSIGN, "="),
        (TokenType.INT, "5"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.LET, "let"),
        (TokenType.IDENT, "ten"),
        (TokenType.ASSIGN, "="),
        (TokenType.INT, "10"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.LET, "let"),
        (TokenType.IDENT, "add"),
        (TokenType.ASSIGN, "="),
        (TokenType.FUNCTION, "fn"),
        (TokenType.LPAREN, "("),
        (TokenType.IDENT, "x"),
        (TokenType.COMMA, ","),
        (TokenType.IDENT, "y"),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.IDENT, "x"),
        (TokenType.PLUS, "+"),
        (TokenType.IDENT, "y"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.RBRACE, "}"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.LET, "let"),
        (TokenType.IDENT, "result"),
        (TokenType.ASSIGN, "="),
        (TokenType.IDENT, "add"),
        (TokenType.LPAREN, "("),
        (TokenType.IDENT, "five"),
        (TokenType.COMMA, ","),
        (TokenType.IDENT, "ten"),
        (TokenType.RPAREN, ")"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.EOF, "")
    ]

    lex = Lexer(input)
    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()

        assert tok.Type == expected_type, \
                f"test[{i}] - token type wrong. expected={expected_type}, got={tok.Type}"
        assert tok.Literal == expected_literal, \
                f"test[{i}] - token Literal wrong. expected={expected_literal}, got={tok.Literal}"


def test_next_token4():
    input_text = "!-/*5; 5 < 10 > 5;"
    tests = [
        (TokenType.BANG, "!"),
        (TokenType.MINUS, "-"),
        (TokenType.SLASH, "/"),
        (TokenType.ASTERISK, "*"),
        (TokenType.INT, "5"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.INT, "5"),
        (TokenType.LT, "<"),
        (TokenType.INT, "10"),
        (TokenType.GT, ">"),
        (TokenType.INT, "5"),
        (TokenType.SEMICOLON, ";"),
    ]

    lex = Lexer(input_text)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()

        assert tok.Type == expected_type, \
                f"tests[{i}] - token type wrong. expected='{expected_type}', got='{tok.Type}'"

        assert tok.Literal == expected_literal, \
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{tok.Literal}'"

def test_next_token5():
    """Added new keyword token - if, else, return, true, false."""
    input_text = (
    """
    if (5 < 10) {
        return true;
    } else {
        return false;
    }
    """)
    tests = [
        (TokenType.IF, "if"),
        (TokenType.LPAREN, "("),
        (TokenType.INT, "5"),
        (TokenType.LT, "<"),
        (TokenType.INT, "10"),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RETURN, "return"),
        (TokenType.TRUE, "true"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.RBRACE, "}"),
        (TokenType.ELSE, "else"),
        (TokenType.LBRACE, "{"),
        (TokenType.RETURN, "return"),
        (TokenType.FALSE, "false"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.RBRACE, "}"),
    ]

    lex = Lexer(input_text)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()

        assert tok.Type == expected_type, \
                f"tests[{i}] - token type wrong. expected='{expected_type}', got='{tok.Type}'"

        assert tok.Literal == expected_literal, \
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{tok.Literal}'"


def test_next_token6():
    """Added new token - == & !=."""
    input_text = (
    """
    10 == 10;
    10 != 9;
    """)
    tests = [
        (TokenType.INT, "10"),
        (TokenType.EQ, "=="),
        (TokenType.INT, "10"),
        (TokenType.SEMICOLON, ";"),
        (TokenType.INT, "10"),
        (TokenType.NOT_EQ, "!="),
        (TokenType.INT, "9"),
        (TokenType.SEMICOLON, ";"),
    ]

    lex = Lexer(input_text)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()
        assert tok.Type == expected_type, \
                f"tests[{i}] - token type wrong. expected='{expected_type}', got='{tok.Type}'"

        assert tok.Literal == expected_literal, \
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{tok.Literal}'"

