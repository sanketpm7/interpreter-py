import pytest
from lexer.lexer import Lexer
from monkey_token.token import (
    ASSIGN,
    PLUS,
    LPAREN,
    RPAREN,
    LBRACE,
    RBRACE,
    COMMA,
    SEMICOLON,
    EOF,
)

def test_next_token():
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

        assert (tok.Type == expected_type,
                f"tests[{i}] - token type wrong. expected={expected_type}, got={tok.Type}")

        assert (tok.Literal == expected_literal,
                f"tests[{i}] - literal wrong. expected={expected_literal}, got={tok.Literal}")
