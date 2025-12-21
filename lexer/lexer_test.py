import pytest
from lexer.lexer import Lexer
from monkey_token.token import (
    LET,
    FUNCTION,
    TRUE,
    FALSE,
    IF,
    ELSE,
    RETURN,
    IDENT,
    INT,

    ASSIGN,
    PLUS,
    MINUS,
    BANG,
    ASTERISK,
    SLASH,
    LT,
    GT,

    LPAREN,
    RPAREN,
    LBRACE,
    RBRACE,
    COMMA,
    SEMICOLON,
    EOF,
)

def test_next_token1():
    input_text = "=+(){},;"
    tests = [
        (ASSIGN, "="),
        (PLUS, "+"),
        (LPAREN, "("),
        (RPAREN, ")"),
        (LBRACE, "{"),
        (RBRACE, "}"),
        (COMMA, ","),
        (SEMICOLON, ";"),
        (EOF, ""),
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
        (LET, "let"),
        (IDENT, "x"),
        (ASSIGN, "="),
        (INT, "10"),
        (SEMICOLON, ";"),
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
        (LET, "let"),
        (IDENT, "five"),
        (ASSIGN, "="),
        (INT, "5"),
        (SEMICOLON, ";"),
        (LET, "let"),
        (IDENT, "ten"),
        (ASSIGN, "="),
        (INT, "10"),
        (SEMICOLON, ";"),
        (LET, "let"),
        (IDENT, "add"),
        (ASSIGN, "="),
        (FUNCTION, "fn"),
        (LPAREN, "("),
        (IDENT, "x"),
        (COMMA, ","),
        (IDENT, "y"),
        (RPAREN, ")"),
        (LBRACE, "{"),
        (IDENT, "x"),
        (PLUS, "+"),
        (IDENT, "y"),
        (SEMICOLON, ";"),
        (RBRACE, "}"),
        (SEMICOLON, ";"),
        (LET, "let"),
        (IDENT, "result"),
        (ASSIGN, "="),
        (IDENT, "add"),
        (LPAREN, "("),
        (IDENT, "five"),
        (COMMA, ","),
        (IDENT, "ten"),
        (RPAREN, ")"),
        (SEMICOLON, ";"),
        (EOF, "")
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
        (BANG, "!"),
        (MINUS, "-"),
        (SLASH, "/"),
        (ASTERISK, "*"),
        (INT, "5"),
        (SEMICOLON, ";"),
        (INT, "5"),
        (LT, "<"),
        (INT, "10"),
        (GT, ">"),
        (INT, "5"),
        (SEMICOLON, ";"),
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
        (IF, "if"),
        (LPAREN, "("),
        (INT, "5"),
        (LT, "<"),
        (INT, "10"),
        (RPAREN, ")"),
        (LBRACE, "{"),
        (RETURN, "return"),
        (TRUE, "true"),
        (SEMICOLON, ";"),
        (RBRACE, "}"),
        (ELSE, "else"),
        (LBRACE, "{"),
        (RETURN, "return"),
        (FALSE, "false"),
        (SEMICOLON, ";"),
        (RBRACE, "}"),
    ]

    lex = Lexer(input_text)

    for i, (expected_type, expected_literal) in enumerate(tests):
        tok = lex.next_token()

        assert tok.Type == expected_type, \
                f"tests[{i}] - token type wrong. expected='{expected_type}', got='{tok.Type}'"

        assert tok.Literal == expected_literal, \
                f"tests[{i}] - literal wrong. expected='{expected_literal}', got='{tok.Literal}'"
